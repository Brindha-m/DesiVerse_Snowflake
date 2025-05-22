-- Create database
CREATE DATABASE IF NOT EXISTS DESIVERSE;

-- Use the database
USE DATABASE DESIVERSE;

-- Create schema
CREATE SCHEMA IF NOT EXISTS HERITAGE_DATA;

-- Use the schema
USE SCHEMA HERITAGE_DATA;

-- Create warehouse if it doesn't exist
CREATE WAREHOUSE IF NOT EXISTS HERITAGE_WH
    WITH WAREHOUSE_SIZE = 'XSMALL'
    AUTO_SUSPEND = 60
    AUTO_RESUME = TRUE;

-- Create the main heritage tourism data table
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
);

-- Create a view for state-wise summary
CREATE OR REPLACE VIEW STATE_SUMMARY AS
SELECT 
    state,
    SUM(tourist_visits) as total_tourist_visits,
    SUM(funding_received) as total_funding,
    FIRST_VALUE(latitude) as latitude,
    FIRST_VALUE(longitude) as longitude,
    FIRST_VALUE(region) as region
FROM HERITAGE_TOURISM_DATA
GROUP BY state;

-- Create a view for art form summary
CREATE OR REPLACE VIEW ART_FORM_SUMMARY AS
SELECT 
    state,
    art_form,
    SUM(tourist_visits) as total_tourist_visits,
    SUM(funding_received) as total_funding
FROM HERITAGE_TOURISM_DATA
GROUP BY state, art_form;

-- Create a view for yearly trends
CREATE OR REPLACE VIEW YEARLY_TRENDS AS
SELECT 
    year,
    SUM(tourist_visits) as total_tourist_visits,
    SUM(funding_received) as total_funding
FROM HERITAGE_TOURISM_DATA
GROUP BY year;

-- Create a view for monthly trends
CREATE OR REPLACE VIEW MONTHLY_TRENDS AS
SELECT 
    year,
    month,
    SUM(tourist_visits) as total_tourist_visits,
    SUM(funding_received) as total_funding
FROM HERITAGE_TOURISM_DATA
GROUP BY year, month;

-- Create a view for regional summary
CREATE OR REPLACE VIEW REGIONAL_SUMMARY AS
SELECT 
    region,
    SUM(tourist_visits) as total_tourist_visits,
    SUM(funding_received) as total_funding
FROM HERITAGE_TOURISM_DATA
GROUP BY region; 