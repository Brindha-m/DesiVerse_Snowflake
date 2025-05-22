import pandas as pd
import os
from datetime import datetime
import json
import numpy as np

def export_all_project_data(df, export_dir='exports'):
    """
    Export all project data in various formats and breakdowns.
    
    Args:
        df (pandas.DataFrame): The main dataset
        export_dir (str): Base directory to save the exports
    """
    # Create timestamp for file names
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Create main export directory structure
    base_dir = f'{export_dir}/project_data_{timestamp}'
    os.makedirs(base_dir, exist_ok=True)
    
    # Create subdirectories for different data categories
    categories = {
        'tourism': f'{base_dir}/tourism_data',
        'heritage': f'{base_dir}/heritage_data',
        'art_forms': f'{base_dir}/art_forms_data',
        'analytics': f'{base_dir}/analytics_data',
        'raw': f'{base_dir}/raw_data'
    }
    
    for category_dir in categories.values():
        os.makedirs(category_dir, exist_ok=True)
    
    # 1. Export complete raw dataset
    df.to_csv(f'{categories["raw"]}/complete_dataset_{timestamp}.csv', index=False)
    
    # 2. Tourism Data Exports
    tourism_data = {
        'yearly_summary': df.groupby('year').agg({
            'tourist_visits': 'sum',
            'funding_received': 'sum',
            'state': 'nunique',
            'art_form': 'nunique'
        }).reset_index(),
        
        'regional_analysis': df.groupby(['year', 'region']).agg({
            'tourist_visits': 'sum',
            'funding_received': 'sum'
        }).reset_index(),
        
        'state_analysis': df.groupby(['year', 'state']).agg({
            'tourist_visits': 'sum',
            'funding_received': 'sum'
        }).reset_index(),
        
        'monthly_trends': df.groupby(['year', 'month']).agg({
            'tourist_visits': 'sum',
            'funding_received': 'sum'
        }).reset_index()
    }
    
    for name, data in tourism_data.items():
        data.to_csv(f'{categories["tourism"]}/{name}_{timestamp}.csv', index=False)
    
    # 3. Heritage Data Exports (only if 'heritage_site' column exists)
    heritage_exports = []
    if 'heritage_site' in df.columns:
        heritage_data = {
            'site_analysis': df.groupby(['state', 'heritage_site']).agg({
                'tourist_visits': 'sum',
                'funding_received': 'sum'
            }).reset_index(),
            'heritage_by_region': df.groupby(['region', 'heritage_site']).agg({
                'tourist_visits': 'sum',
                'funding_received': 'sum'
            }).reset_index()
        }
        for name, data in heritage_data.items():
            data.to_csv(f'{categories["heritage"]}/{name}_{timestamp}.csv', index=False)
            heritage_exports.append(name)
    else:
        heritage_exports = None
    
    # 4. Art Forms Data Exports
    art_forms_data = {
        'art_form_analysis': df.groupby(['year', 'art_form']).agg({
            'tourist_visits': 'sum',
            'funding_received': 'sum'
        }).reset_index(),
        
        'art_forms_by_region': df.groupby(['region', 'art_form']).agg({
            'tourist_visits': 'sum',
            'funding_received': 'sum'
        }).reset_index(),
        
        'art_forms_by_state': df.groupby(['state', 'art_form']).agg({
            'tourist_visits': 'sum',
            'funding_received': 'sum'
        }).reset_index()
    }
    
    for name, data in art_forms_data.items():
        data.to_csv(f'{categories["art_forms"]}/{name}_{timestamp}.csv', index=False)
    
    # 5. Analytics Data Exports
    analytics_data = {
        'correlation_analysis': df[['tourist_visits', 'funding_received']].corr(),
        'seasonal_analysis': df.groupby(['year', 'month']).agg({
            'tourist_visits': ['mean', 'std', 'min', 'max'],
            'funding_received': ['mean', 'std', 'min', 'max']
        }).reset_index(),
        'growth_metrics': df.groupby('year').agg({
            'tourist_visits': ['sum', 'mean', 'std'],
            'funding_received': ['sum', 'mean', 'std']
        }).reset_index()
    }
    
    for name, data in analytics_data.items():
        data.to_csv(f'{categories["analytics"]}/{name}_{timestamp}.csv', index=False)
    
    # 6. Create a metadata file
    def to_py(obj):
        if isinstance(obj, (np.integer, pd.Int64Dtype, np.int64)):
            return int(obj)
        if isinstance(obj, (np.floating, pd.Float64Dtype, np.float64)):
            return float(obj)
        if isinstance(obj, (np.ndarray,)):
            return obj.tolist()
        return obj

    metadata = {
        'export_timestamp': str(timestamp),
        'data_categories': list(categories.keys()),
        'total_records': int(len(df)),
        'date_range': {
            'start_year': int(df['year'].min()),
            'end_year': int(df['year'].max())
        },
        'regions_covered': sorted([str(x) for x in df['region'].unique().tolist()]),
        'states_covered': sorted([str(x) for x in df['state'].unique().tolist()]),
        'art_forms_covered': sorted([str(x) for x in df['art_form'].unique().tolist()]),
        'heritage_exports': heritage_exports if heritage_exports else 'heritage_site column not found, heritage exports skipped.'
    }

    with open(f'{base_dir}/metadata_{timestamp}.json', 'w') as f:
        json.dump(metadata, f, indent=4, default=to_py)
    
    return {
        'base_directory': base_dir,
        'timestamp': timestamp,
        'categories': categories,
        'metadata_file': f'metadata_{timestamp}.json'
    } 