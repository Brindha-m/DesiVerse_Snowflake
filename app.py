import streamlit as st
import snowflake.connector
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from snowflake_config import SNOWFLAKE_CONFIG
from streamlit_option_menu import option_menu

# Import utility modules
from utils.image_utils import get_art_form_images, get_cached_art_form_images
from components.styling import load_css

# Import page modules
from pages.heritage_explorer import show_heritage_explorer
from pages.tourism_analytics import show_tourism_analytics
from pages.responsible_tourism import show_responsible_tourism
from pages.cultural_gallery import show_cultural_gallery
from pages.cultural_quiz import show_quiz

# Set page config
st.set_page_config(
    page_title="DesiVerse Analytics",
    page_icon="🌏",
    layout="wide"
)

# Load custom CSS
load_css()

# Initialize Snowflake connection
@st.cache_resource(ttl=3600)  # Cache for 1 hour
def init_connection():
    try:
        conn = snowflake.connector.connect(
            user=SNOWFLAKE_CONFIG['user'],
            password=SNOWFLAKE_CONFIG['password'],
            account=SNOWFLAKE_CONFIG['account'],
            warehouse=SNOWFLAKE_CONFIG['warehouse'],
            database=SNOWFLAKE_CONFIG['database'],
            schema=SNOWFLAKE_CONFIG['schema']
        )
        return conn
    except Exception as e:
        st.error(f"Failed to connect to Snowflake: {str(e)}")
        return None

# Function to run queries
@st.cache_data(ttl=600)  # Cache for 10 minutes
def run_query(query):
    conn = None
    try:
        conn = init_connection()
        if conn is None:
            return pd.DataFrame()  # Return empty DataFrame if connection failed
        
        # Test if connection is still alive
        try:
            conn.cursor().execute("SELECT 1")
        except:
            # If connection is dead, clear the cache and get a new one
            st.cache_resource.clear()
            conn = init_connection()
            if conn is None:
                return pd.DataFrame()
        
        return pd.read_sql(query, conn)
    except Exception as e:
        st.error(f"Error executing query: {str(e)}")
        return pd.DataFrame()
    finally:
        if conn is not None:
            try:
                conn.close()
            except:
                pass


def main():
    if 'df' not in st.session_state:
        query = """
        SELECT DISTINCT
            STATE as state,
            ART_FORM as art_form,
            TOURIST_VISITS as tourist_visits,
            MONTH as month,
            YEAR as year,
            REGION as region,
            FUNDING_RECEIVED as funding_received,
            LATITUDE as latitude,
            LONGITUDE as longitude
        FROM HERITAGE_TOURISM_DATA
        """
        
        # Store the query result in session state
        st.session_state.df = run_query(query)
        
        # Debug 
        # st.write("Available columns:", st.session_state.df.columns.tolist())
    
    left_co, cent_co,last_co = st.columns(3)

    with cent_co:
        st.image("components/desiverse.png")

    st.markdown('<p style="font-size:20px; color:#AAAAAA; font-style:italic; text-align:center; margin-bottom:20px;"><b>Journey through India\'s Art, Culture & Tourism</b></p>', unsafe_allow_html=True)
    
    # Navigation menu 
    selected = option_menu(
        menu_title=None,
        options=["Heritage Walks", "Tourism Trends", "Responsible Tourism", "Desi Gallery", "Culture Quest"],
        icons=["🏛️", "📊", "🌱", "🎨", "🎯"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {
                "padding": "0.5rem!important", 
                "background": "linear-gradient(90deg, rgba(29,29,29,0.8) 0%, rgba(45,45,45,0.9) 50%, rgba(29,29,29,0.8) 100%)",
                "border-radius": "10px",
                "box-shadow": "0 4px 15px 0 rgba(0, 0, 0, 0.3)",
                "margin-bottom": "1rem"
            },
            "icon": {
                "color": "white", 
                "font-size": "25px",
                "margin-bottom": "5px",
                "text-shadow": "0 0 10px rgba(255,255,255,0.3)"
            },
            "nav-link": {
                "font-size": "16px",
                "text-align": "center",
                "margin": "0px 5px",
                "padding": "10px 5px",
                "border-radius": "7px",
                "transition": "all 0.3s ease-in-out",
                "background": "transparent",
                "font-weight": "normal",
                "color": "rgba(255, 255, 255, 0.8)",
                "--hover-color": "rgba(78, 205, 196, 0.2)",
                "border-bottom": "2px solid transparent"
            },
            "nav-link-selected": {
                "background": "linear-gradient(135deg, rgba(78, 205, 196, 0.5) 0%, rgba(255, 107, 107, 0.2) 100%)",
                "color": "white",
                "font-weight": "bold",
                "box-shadow": "0 2px 10px 0 rgba(78, 205, 196, 0.3)",
                "border-bottom": "2px solid rgba(255, 255, 255, 0.5)"
            }
        }
    )
    
    # Display selected page
    if selected == "Heritage Walks":
        show_heritage_explorer(st.session_state.df)
    elif selected == "Tourism Trends":
        show_tourism_analytics(st.session_state.df)
    elif selected == "Responsible Tourism":
        show_responsible_tourism()
    elif selected == "Desi Gallery":
        show_cultural_gallery()
    elif selected == "Culture Quest":
        show_quiz()

    # Footer with data source attribution
    st.markdown("---")
    st.markdown("""
        <div style='text-align: center; color: #666; font-size: 0.8em;'>
            Data Source: <a href='https://data.gov.in' target='_blank'>data.gov.in</a> | 
            Processed and stored in Snowflake | 
            Last Updated: {last_updated}
        </div>
    """.format(last_updated=pd.Timestamp.now().strftime('%Y-%m-%d')), unsafe_allow_html=True)

if __name__ == "__main__":
    main()