import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
from snowflake_config import SNOWFLAKE_CONFIG
import os
import tempfile
import shutil

def load_csv_to_snowflake(csv_file_path, cur, table_name):
    """Load data from CSV file into Snowflake using PUT command"""
    try:
        # Verify file exists
        if not os.path.exists(csv_file_path):
            print(f"Error: File not found: {csv_file_path}")
            return False

        # Read the CSV file
        print(f"Reading CSV file: {csv_file_path}")
        df = pd.read_csv(csv_file_path)
        
        # Create a temporary directory for staging
        with tempfile.TemporaryDirectory() as temp_dir:
            # Save DataFrame to a temporary CSV file
            temp_file = os.path.join(temp_dir, 'temp_data.csv')
            df.to_csv(temp_file, index=False)
            
            # Create a stage for the file
            stage_name = 'TEMP_STAGE'
            cur.execute(f"CREATE OR REPLACE TEMPORARY STAGE {stage_name}")
            
            # Put the file into the stage
            print("Uploading file to Snowflake stage...")
            cur.execute(f"PUT file://{temp_file} @{stage_name}")
            
            # Copy data from stage to table
            print("Loading data into table...")
            if table_name == 'HERITAGE_TOURISM_DATA':
                # Special handling for main table to include created_at
                cur.execute(f"""
                    COPY INTO {table_name} (
                        state, art_form, tourist_visits, month, year, 
                        region, funding_received, latitude, longitude, 
                        created_at
                    )
                    FROM (
                        SELECT 
                            $1, $2, $3, $4, $5, $6, $7, $8, $9, 
                            CURRENT_TIMESTAMP()
                        FROM @{stage_name}
                    )
                    FILE_FORMAT = (TYPE = CSV FIELD_DELIMITER = ',' SKIP_HEADER = 1)
                """)
            else:
                # Normal copy for other tables
                cur.execute(f"""
                    COPY INTO {table_name}
                    FROM @{stage_name}
                    FILE_FORMAT = (TYPE = CSV FIELD_DELIMITER = ',' SKIP_HEADER = 1)
                """)
            
            # Get the number of rows loaded
            cur.execute(f"SELECT COUNT(*) FROM {table_name}")
            row_count = cur.fetchone()[0]
            print(f"Successfully loaded data. Total rows in table: {row_count}")
            return True
        
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    # First, let's verify the Snowflake connection and setup
    try:
        conn = snowflake.connector.connect(
            user=SNOWFLAKE_CONFIG['user'],
            password=SNOWFLAKE_CONFIG['password'],
            account=SNOWFLAKE_CONFIG['account']
        )
        cur = conn.cursor()
        
        # Verify database exists
        cur.execute(f"SHOW DATABASES LIKE '{SNOWFLAKE_CONFIG['database']}'")
        if not cur.fetchone():
            print(f"Creating database {SNOWFLAKE_CONFIG['database']}...")
            cur.execute(f"CREATE DATABASE IF NOT EXISTS {SNOWFLAKE_CONFIG['database']}")
        
        # Use database
        cur.execute(f"USE DATABASE {SNOWFLAKE_CONFIG['database']}")
        
        # Verify schema exists
        cur.execute(f"SHOW SCHEMAS LIKE '{SNOWFLAKE_CONFIG['schema']}'")
        if not cur.fetchone():
            print(f"Creating schema {SNOWFLAKE_CONFIG['schema']}...")
            cur.execute(f"CREATE SCHEMA IF NOT EXISTS {SNOWFLAKE_CONFIG['schema']}")
        
        # Use schema
        cur.execute(f"USE SCHEMA {SNOWFLAKE_CONFIG['schema']}")
        
        # Verify warehouse exists
        cur.execute(f"SHOW WAREHOUSES LIKE '{SNOWFLAKE_CONFIG['warehouse']}'")
        if not cur.fetchone():
            print(f"Creating warehouse {SNOWFLAKE_CONFIG['warehouse']}...")
            cur.execute(f"""
                CREATE WAREHOUSE IF NOT EXISTS {SNOWFLAKE_CONFIG['warehouse']}
                WITH WAREHOUSE_SIZE = 'XSMALL'
                AUTO_SUSPEND = 60
                AUTO_RESUME = TRUE
            """)
        
        # Drop existing views if they exist
        print("Dropping existing views...")
        views_to_drop = [
            'STATE_SUMMARY',
            'ART_FORM_SUMMARY',
            'YEARLY_TRENDS',
            'MONTHLY_TRENDS',
            'REGIONAL_SUMMARY'
        ]
        
        for view in views_to_drop:
            try:
                cur.execute(f"DROP VIEW IF EXISTS {view}")
            except Exception as e:
                print(f"Warning: Could not drop view {view}: {e}")
        
        # Create tables for each type of data
        print("Creating tables...")
        
        # Main heritage tourism data table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS HERITAGE_TOURISM_DATA (
                state VARCHAR(50),
                art_form VARCHAR(100),
                tourist_visits INTEGER,
                month INTEGER,
                year INTEGER,
                region VARCHAR(50),
                funding_received DECIMAL(15,2),
                latitude DECIMAL(10,6),
                longitude DECIMAL(10,6),
                created_at TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
            )
        """)
        
        # State summary table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS STATE_SUMMARY (
                state VARCHAR(50),
                total_tourist_visits INTEGER,
                total_funding DECIMAL(15,2),
                latitude DECIMAL(10,6),
                longitude DECIMAL(10,6),
                region VARCHAR(50)
            )
        """)
        
        # Art forms data table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS ART_FORMS_DATA (
                state VARCHAR(50),
                art_form VARCHAR(100),
                total_tourist_visits INTEGER,
                total_funding DECIMAL(15,2)
            )
        """)
        
        # Yearly trends table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS YEARLY_TRENDS (
                year INTEGER,
                total_tourist_visits INTEGER,
                total_funding DECIMAL(15,2)
            )
        """)
        
        # Monthly trends table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS MONTHLY_TRENDS (
                year INTEGER,
                month INTEGER,
                total_tourist_visits INTEGER,
                total_funding DECIMAL(15,2)
            )
        """)
        
        # Regional summary table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS REGIONAL_SUMMARY (
                region VARCHAR(50),
                total_tourist_visits INTEGER,
                total_funding DECIMAL(15,2)
            )
        """)
        
        # Map of CSV files to their corresponding tables
        file_table_map = {
            'exports/heritage_tourism_data.csv': 'HERITAGE_TOURISM_DATA',
            'exports/state_summary.csv': 'STATE_SUMMARY',
            'exports/art_forms_data.csv': 'ART_FORMS_DATA',
            'exports/yearly_trends.csv': 'YEARLY_TRENDS',
            'exports/monthly_trends.csv': 'MONTHLY_TRENDS',
            'exports/regional_summary.csv': 'REGIONAL_SUMMARY'
        }
        
        # Load each CSV file into its corresponding table
        for csv_file, table_name in file_table_map.items():
            print(f"\nProcessing {csv_file}...")
            if load_csv_to_snowflake(csv_file, cur, table_name):
                print(f"Successfully loaded {csv_file} into {table_name}")
            else:
                print(f"Failed to load {csv_file} into {table_name}")
                
    except Exception as e:
        print(f"Error during setup: {e}")
    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close() 