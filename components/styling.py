"""
Styling module for DesiVerse application.
Contains CSS styles and UI components.
"""

import streamlit as st

def load_css():
    """
    Load custom CSS styles for the application.
    """
    st.markdown("""
    <style>
        /* Hide sidebar completely - enhanced version */
        [data-testid="stSidebar"] {
            width: 0px !important;
            display: none !important;
            visibility: hidden !important;
            opacity: 0 !important;
            position: absolute !important;
            left: -9999px !important;
        }
        
        /* Hide the sidebar collapse button - enhanced version */
        button[kind="sidebar"] {
            display: none !important;
            visibility: hidden !important;
            opacity: 0 !important;
        }
        
        /* Additional sidebar hiding for older Streamlit versions */
        .css-1d391kg, .css-12oz5g7 {
            display: none !important;
        }
        
        .main {
            background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
            color: white;
        }
        .main-header {
            font-size: 2.5rem;
            background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
        }
        .sub-header {
            font-size: 1.8rem;
            color: white;
            border-bottom: 2px solid rgba(78, 205, 196, 0.5);
            padding-bottom: 10px;
        }
        
        /* Nav menu animations and effects */
        .nav-item:hover {
            transform: translateY(-2px);
            transition: all 0.3s ease;
        }
        
        /* Custom nav menu styling */
        .stOptionMenu .nav {
            gap: 5px;
            padding: 5px;
        }
        
        .stOptionMenu .nav-link {
            position: relative;
            overflow: hidden;
        }
        
        .stOptionMenu .nav-link::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 100%);
            opacity: 0;
            transition: opacity 0.3s ease;
            z-index: 0;
        }
        
        .stOptionMenu .nav-link:hover::before {
            opacity: 1;
        }
        
        .stOptionMenu .nav-link-selected::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 30%;
            height: 3px;
            background: white;
            border-radius: 3px;
            box-shadow: 0 0 10px rgba(255,255,255,0.5);
        }
        
        /* Add a subtle pulsing animation to selected nav item */
        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(78, 205, 196, 0.4); }
            70% { box-shadow: 0 0 0 10px rgba(78, 205, 196, 0); }
            100% { box-shadow: 0 0 0 0 rgba(78, 205, 196, 0); }
        }
        
        .stOptionMenu .nav-link-selected {
            animation: pulse 2s infinite;
        }
        
        /* Icon glow effect on hover */
        .stOptionMenu .nav-link:hover .nav-link-icon {
            text-shadow: 0 0 15px rgba(255,255,255,0.8);
            transition: all 0.3s ease;
        }
        
        /* Metric cards styling */
        .metric-card {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .metric-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        }
        .metric-value {
            font-size: 2rem;
            font-weight: bold;
            margin-bottom: 5px;
            background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .metric-label {
            font-size: 1rem;
            color: #ddd;
        }
        
        /* Insights card styling */
        .insights-card {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .insights-card h3 {
            color: #4ECDC4;
            margin-bottom: 15px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            padding-bottom: 10px;
        }
        .insights-card ul {
            padding-left: 20px;
        }
        .insights-card li {
            margin-bottom: 10px;
            line-height: 1.6;
        }
        
        /* Art form card styling */
        .art-card {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            padding: 20px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            height: 100%;
            margin-bottom: 20px;
            position: relative;
            overflow: hidden;
        }
        .art-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        }
        .art-card img {
            border-radius: 5px;
            margin-bottom: 15px;
            width: 100%;
            object-fit: cover;
            height: auto;
        }
        .art-card h4 {
            margin-bottom: 10px;
            color: #FF6B6B;
        }
        .card-content {
            padding: 5px 0;
        }
        .card-title {
            font-size: 1.2rem;
            font-weight: bold;
            color: #FF6B6B;
            margin-bottom: 10px;
        }
        .card-description {
            margin-bottom: 10px;
            line-height: 1.5;
        }
        .card-details {
            font-size: 0.9rem;
            margin-bottom: 8px;
            color: rgba(255, 255, 255, 0.8);
        }
        .card-tips {
            font-size: 0.9rem;
            margin-top: 10px;
            color: rgba(78, 205, 196, 0.9);
        }
    </style>
    """, unsafe_allow_html=True)


def display_metric(label, value, formatter=None):
    """
    Display a metric in a card.
    
    Args:
        label (str): The label for the metric
        value: The value of the metric
        formatter (callable, optional): Function to format the value. Defaults to None.
    """
    if formatter:
        formatted_value = formatter(value)
    else:
        formatted_value = value
        
    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-value'>{formatted_value}</div>
        <div class='metric-label'>{label}</div>
    </div>
    """, unsafe_allow_html=True)


def display_card(title, description, details=None, tips=None):
    """
    Display content in a card.
    
    Args:
        title (str): The title of the card
        description (str): The description for the card
        details (str, optional): Additional details. Defaults to None.
        tips (str, optional): Tips related to the card content. Defaults to None.
    """
    st.markdown(f"""
    <div class='card'>
        <div class='card-content'>
            <div class='card-title'>{title}</div>
            <div class='card-description'>{description}</div>
            {f"<div class='card-details'>{details}</div>" if details else ""}
            {f"<div class='card-tips'>{tips}</div>" if tips else ""}
        </div>
    </div>
    """, unsafe_allow_html=True)


def display_insights(title, insights_list):
    """
    Display insights in a card.
    
    Args:
        title (str): The title for the insights
        insights_list (list): List of insights to display
    """
    insights_html = "".join([f"<li>{insight}</li>" for insight in insights_list])
    
    st.markdown(f"""
    <div class='insights-card'>
        <h3>{title}</h3>
        <ul>
            {insights_html}
        </ul>
    </div>
    """, unsafe_allow_html=True)


def display_art_book(art_form, art_details, image_url=None):
    """
    Display art form details in a book-like layout.
    
    Args:
        art_form (str): The name of the art form
        art_details (dict): Dictionary containing art form details
        image_url (str, optional): URL for the art form image. Defaults to None.
    """
    st.markdown("<div class='art-book'>", unsafe_allow_html=True)
    st.markdown("<div class='art-book-header'>", unsafe_allow_html=True)
    st.markdown(f"<div class='art-book-title'>{art_form}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='art-book-content'>", unsafe_allow_html=True)
    
    # Left column - Image
    st.markdown("<div class='art-book-image'>", unsafe_allow_html=True)
    if image_url:
        try:
            st.image(image_url, use_container_width=True)
        except Exception as e:
            st.error(f"Error displaying image: {str(e)}")
            st.error("Image not available")
    else:
        st.error("No images available")
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Right column - Information
    st.markdown("<div class='art-book-info'>", unsafe_allow_html=True)
    
    # Description section
    st.markdown("<div class='art-book-section'>", unsafe_allow_html=True)
    st.markdown("<div class='art-book-section-title'>Description</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='art-book-section-content'>{art_details['description']}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # History section
    st.markdown("<div class='art-book-section'>", unsafe_allow_html=True)
    st.markdown("<div class='art-book-section-title'>History</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='art-book-section-content'>{art_details['history']}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Techniques section
    st.markdown("<div class='art-book-section'>", unsafe_allow_html=True)
    st.markdown("<div class='art-book-section-title'>Techniques</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='art-book-section-content'>{art_details['techniques']}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Costume section
    st.markdown("<div class='art-book-section'>", unsafe_allow_html=True)
    st.markdown("<div class='art-book-section-title'>Costume</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='art-book-section-content'>{art_details['costume']}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Famous practitioners section
    st.markdown("<div class='art-book-section'>", unsafe_allow_html=True)
    st.markdown("<div class='art-book-section-title'>Famous Practitioners</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='art-book-section-content'>{art_details['famous_practitioners']}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)  # End art-book-info
    st.markdown("</div>", unsafe_allow_html=True)  # End art-book-content
    st.markdown("</div>", unsafe_allow_html=True)  # End art-book 