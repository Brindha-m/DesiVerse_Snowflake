"""
Data generator module for DesiVerse application.
Contains functions for generating mock data for the application.
"""

import pandas as pd
import numpy as np
import random

def generate_mock_data():
    """
    Generate mock data for the application.
    Returns a pandas DataFrame with state, art form, tourist visits, etc.
    """
    # Indian states and union territories
    states = [
        'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh',
        'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka',
        'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram',
        'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana',
        'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Delhi', 'Jammu and Kashmir',
        'Lakshadweep'
    ]
    
    # Define regions for each state
    regions = {
        'North': ['Delhi', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Punjab', 'Rajasthan', 'Uttar Pradesh', 'Uttarakhand'],
        'South': ['Andhra Pradesh', 'Karnataka', 'Kerala', 'Tamil Nadu', 'Telangana', 'Lakshadweep'],
        'East': ['Bihar', 'Jharkhand', 'Odisha', 'West Bengal'],
        'West': ['Goa', 'Gujarat', 'Maharashtra'],
        'Central': ['Chhattisgarh', 'Madhya Pradesh'],
        'Northeast': ['Arunachal Pradesh', 'Assam', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Sikkim', 'Tripura']
    }
    
    # Map states to their regions
    state_to_region = {}
    for region, region_states in regions.items():
        for state in region_states:
            state_to_region[state] = region
    
    # Traditional art forms by state
    art_forms = {
        'Andhra Pradesh': ['Kuchipudi', 'Kalamkari', 'Budithi Brass Craft'],
        'Arunachal Pradesh': ['Monpa Mask', 'Thangka Paintings', 'Wancho Wood Carving'],
        'Assam': ['Bihu Dance', 'Sattriya Dance', 'Assam Silk Weaving'],
        'Bihar': ['Madhubani Painting', 'Manjusha Art', 'Sujni Embroidery'],
        'Chhattisgarh': ['Panthi Dance', 'Godna Art', 'Bell Metal Craft'],
        'Goa': ['Dekni Dance', 'Fugdi Dance', 'Goan Lacework'],
        'Gujarat': ['Garba', 'Patola Weaving', 'Rogan Art'],
        'Haryana': ['Phag Dance', 'Embroidery Craft', 'Charpai Weaving'],
        'Himachal Pradesh': ['Kullu Shawl Weaving', 'Chamba Rumal', 'Kangra Painting'],
        'Jharkhand': ['Sohrai Painting', 'Chhau Dance', 'Dokra Metal Craft'],
        'Karnataka': ['Yakshagana', 'Bidri Ware', 'Mysore Painting'],
        'Kerala': ['Kathakali', 'Mohiniyattam', 'Aranmula Kannadi'],
        'Madhya Pradesh': ['Gond Art', 'Bagh Print', 'Chanderi Weaving'],
        'Maharashtra': ['Lavani Dance', 'Warli Painting', 'Paithani Sarees'],
        'Manipur': ['Manipuri Dance', 'Longpi Pottery', 'Phanek Weaving'],
        'Meghalaya': ['Nongkrem Dance', 'Bamboo Craft', 'Garo Wangala Dance'],
        'Mizoram': ['Cheraw Dance', 'Mizo Bamboo Dance', 'Puanchei Textiles'],
        'Nagaland': ['Hornbill Festival Dances', 'Naga Shawl Weaving', 'Wood Carving'],
        'Odisha': ['Odissi Dance', 'Pattachitra', 'Applique Work'],
        'Punjab': ['Bhangra', 'Phulkari Embroidery', 'Jutti Making'],
        'Rajasthan': ['Ghoomar Dance', 'Blue Pottery', 'Miniature Painting'],
        'Sikkim': ['Mask Dance', 'Thangka Painting', 'Carpet Weaving'],
        'Tamil Nadu': ['Bharatanatyam', 'Tanjore Painting', 'Stone Carving'],
        'Telangana': ['Perini Shivatandavam', 'Nirmal Paintings', 'Bidri Craft'],
        'Tripura': ['Hojagiri Dance', 'Bamboo Craft', 'Risa Textile Weaving'],
        'Uttar Pradesh': ['Kathak Dance', 'Chikankari', 'Lucknow Zardozi'],
        'Uttarakhand': ['Choliya Dance', 'Aipan Art', 'Ringal Craft'],
        'West Bengal': ['Durga Puja Art', 'Kantha Stitch', 'Patachitra'],
        'Delhi': ['Kathak Dance', 'Zardozi Work', 'Meenakari Craft'],
        'Jammu and Kashmir': ['Rauf Dance', 'Pashmina Weaving', 'Walnut Wood Carving'],
        'Lakshadweep': ['Lava Dance', 'Parichakali', 'Coral Craft', 'Shell Craft']
    }
    
    # Latitude and longitude for each state (approximate centers)
    state_coordinates = {
        'Andhra Pradesh': (15.9129, 79.7400),
        'Arunachal Pradesh': (28.2180, 94.7278),
        'Assam': (26.2006, 92.9376),
        'Bihar': (25.0961, 85.3131),
        'Chhattisgarh': (21.2787, 81.8661),
        'Goa': (15.2993, 74.1240),
        'Gujarat': (22.2587, 71.1924),
        'Haryana': (29.0588, 76.0856),
        'Himachal Pradesh': (31.1048, 77.1734),
        'Jharkhand': (23.6102, 85.2799),
        'Karnataka': (15.3173, 75.7139),
        'Kerala': (10.8505, 76.2711),
        'Madhya Pradesh': (23.4733, 77.9470),
        'Maharashtra': (19.7515, 75.7139),
        'Manipur': (24.6637, 93.9063),
        'Meghalaya': (25.4670, 91.3662),
        'Mizoram': (23.1645, 92.9376),
        'Nagaland': (26.1584, 94.5624),
        'Odisha': (20.9517, 85.0985),
        'Punjab': (31.1471, 75.3412),
        'Rajasthan': (27.0238, 74.2179),
        'Sikkim': (27.5330, 88.5122),
        'Tamil Nadu': (11.1271, 78.6569),
        'Telangana': (18.1124, 79.0193),
        'Tripura': (23.9408, 91.9882),
        'Uttar Pradesh': (26.8467, 80.9462),
        'Uttarakhand': (30.0668, 79.0193),
        'West Bengal': (22.9868, 87.8550),
        'Delhi': (28.7041, 77.1025),
        'Jammu and Kashmir': (33.7782, 76.5762),
        'Lakshadweep': (10.5667, 72.6417)
    }
    
    # Create empty list to store data
    data = []
    
    # Generate data for the last 5 years (2020-2024) and for each month
    years = range(2020, 2025)
    months = range(1, 13)
    
    # Seasonal trends - higher tourism in different regions based on season
    seasonal_multipliers = {
        'North': [0.8, 0.7, 0.9, 1.0, 1.1, 1.2, 0.7, 0.6, 0.8, 1.0, 1.5, 1.7],
        'South': [1.3, 1.2, 1.0, 0.8, 0.7, 0.6, 0.8, 1.0, 1.2, 1.4, 1.3, 1.5],
        'East': [1.2, 1.0, 0.9, 0.8, 0.7, 0.6, 0.9, 1.1, 1.3, 1.4, 1.2, 1.3],
        'West': [1.1, 1.0, 0.9, 0.7, 0.6, 0.5, 0.8, 1.2, 1.4, 1.3, 1.2, 1.3],
        'Central': [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.5],
        'Northeast': [0.6, 0.7, 0.9, 1.1, 1.3, 1.4, 0.9, 0.7, 0.8, 1.0, 0.8, 0.7]
    }
    
    # Year-on-year growth trend (tourism recovery after COVID)
    yearly_growth = {
        2020: 0.4,  # COVID impact
        2021: 0.6,  # Partial recovery
        2022: 0.8,  # Further recovery
        2023: 0.9,  # Almost back to normal
        2024: 1.1,  # Beyond pre-COVID levels
        2025: 1.1 * 1.15  # 15% growth over 2024
    }
    
    # Base popularity factors for states
    popularity_factor = {
        'Rajasthan': 1.8, 'Kerala': 1.7, 'Goa': 1.6, 'Tamil Nadu': 1.7, 'Uttar Pradesh': 1.7,
        'Maharashtra': 1.6, 'Delhi': 1.6, 'Gujarat': 1.4, 'Karnataka': 1.5, 'Himachal Pradesh': 1.4,
        'Uttarakhand': 1.4, 'Jammu and Kashmir': 1.3, 'West Bengal': 1.4, 'Madhya Pradesh': 1.3,
        'Odisha': 1.2, 'Andhra Pradesh': 1.2, 'Telangana': 1.2, 'Assam': 1.1, 'Punjab': 1.1,
        'Bihar': 0.9, 'Chhattisgarh': 0.9, 'Jharkhand': 0.8, 'Manipur': 0.8, 'Meghalaya': 0.9,
        'Tripura': 0.8, 'Nagaland': 0.8, 'Mizoram': 0.7, 'Sikkim': 1.0, 'Arunachal Pradesh': 0.9,
        'Haryana': 0.9, 'Lakshadweep': 1.3
    }
    
    for year in list(years) + [2025]:
        for month in months:
            for state in states:
                region = state_to_region.get(state, 'Other')
                state_pop_factor = popularity_factor.get(state, 1.0)
                seasonal_factor = seasonal_multipliers.get(region, [1.0] * 12)[month - 1]
                year_factor = yearly_growth.get(year, 1.0)
                
                # Generate tourist visits with some randomness and factors
                base_visits = np.random.gamma(shape=10, scale=state_pop_factor * 10000)
                tourist_visits = int(base_visits * seasonal_factor * year_factor * (1 + np.random.normal(0, 0.1)))
                
                # Random art form selection for this record
                if state in art_forms:
                    art_form = random.choice(art_forms[state])
                else:
                    art_form = "Traditional Dance"
                
                # Generate funding received with correlation to tourist visits but with variability
                if year == 2025:
                    # 12% growth in funding over 2024
                    funding_base = tourist_visits * random.uniform(0.5, 2.0) * 1.12
                else:
                    funding_base = tourist_visits * random.uniform(0.5, 2.0)
                funding_received = int(funding_base * (1 + np.random.normal(0, 0.2)))
                
                # Get coordinates
                lat, lon = state_coordinates.get(state, (0, 0))
                
                # Append data
                data.append({
                    'state': state,
                    'art_form': art_form,
                    'tourist_visits': tourist_visits,
                    'month': month,
                    'year': year,
                    'region': region,
                    'funding_received': funding_received,
                    'latitude': lat,
                    'longitude': lon
                })
    
    return pd.DataFrame(data)

if __name__ == "__main__":
    # Example of generating mock data and saving to CSV
    df = generate_mock_data()
    df.to_csv('data/heritage_tourism_data.csv', index=False)
    print(f"Generated mock data with {len(df)} rows.") 