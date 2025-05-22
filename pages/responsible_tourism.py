"""
Responsible Tourism page for DesiVerse application.
Displays information about sustainable tourism practices and lesser-known heritage sites.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import sys
import os

# Add the project root to the path so imports work correctly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.constants import lesser_known_sites, responsible_tourism_tips
from components.styling import display_insights

def show_responsible_tourism():
    """Display the Responsible Tourism page with interactive visualizations."""
    st.markdown("<h1 class='main-header'>Responsible Tourism</h1>", unsafe_allow_html=True)
    
    # Add Bubble Chart Section at the top
    st.markdown("<h2 class='sub-header'>📊 Tourism Impact Analysis</h2>", unsafe_allow_html=True)
    
    # Create sample data for the bubble chart
    tourism_data = pd.DataFrame({
        'site': [
            'Taj Mahal', 'Qutub Minar', 'Konark Sun Temple', 
            'Champaner-Pavagadh', 'Majuli Island', 'Chettinad',
            'Ziro Valley', 'Shekhawati', 'Hampi', 'Khajuraho'
        ],
        'visitors': [
            8000000, 4000000, 3500000,  # Popular sites
            800000, 500000, 600000,     # Lesser-known sites
            300000, 400000, 2500000, 2000000  # Mixed popularity
        ],
        'revenue': [
            1200000000, 800000000, 700000000,  # Popular sites
            120000000, 75000000, 90000000,     # Lesser-known sites
            45000000, 60000000, 500000000, 400000000  # Mixed popularity
        ],
        'prominence': [
            95, 85, 80,  # Popular sites
            40, 35, 45,  # Lesser-known sites
            30, 35, 70, 65  # Mixed popularity
        ],
        'category': [
            'Popular Site', 'Popular Site', 'Popular Site',
            'Hidden Gem', 'Hidden Gem', 'Hidden Gem',
            'Hidden Gem', 'Hidden Gem', 'Popular Site', 'Popular Site'
        ]
    })
    
    # Create bubble chart
    fig = px.scatter(
        tourism_data,
        x='visitors',
        y='revenue',
        size='prominence',
        color='category',
        hover_name='site',
        title='Tourism Impact: Popular Sites vs Hidden Gems',
        labels={
            'visitors': 'Annual Visitors',
            'revenue': 'Annual Revenue (₹)',
            'prominence': 'Site Prominence',
            'category': 'Site Category'
        },
        color_discrete_sequence=['#FF6B6B', '#4ECDC4'],
        template='plotly_dark'
    )
    
    # Update layout for better visibility
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', size=12),
        title_font=dict(size=20),
        height=600,
        margin=dict(t=50, b=50, l=50, r=50),
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99,
            bgcolor='rgba(0,0,0,0.5)',
            bordercolor='rgba(255,255,255,0.2)',
            borderwidth=1
        ),
        xaxis=dict(
            title=dict(font=dict(size=14)),
            tickformat=",d"
        ),
        yaxis=dict(
            title=dict(font=dict(size=14)),
            tickformat=",d"
        )
    )
    
    # Add annotations for key insights
    fig.add_annotation(
        x=8000000,
        y=1200000000,
        text="High Impact Sites",
        showarrow=True,
        arrowhead=1,
        ax=50,
        ay=-50,
        font=dict(color='white', size=12)
    )
    
    fig.add_annotation(
        x=800000,
        y=120000000,
        text="Sustainable Tourism Opportunities",
        showarrow=True,
        arrowhead=1,
        ax=-50,
        ay=50,
        font=dict(color='white', size=12)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Add insights below the chart
    display_insights("Key Insights", [
        "Popular sites (red bubbles) show significantly higher visitor numbers and revenue",
        "Hidden gems (teal bubbles) offer sustainable tourism opportunities with lower environmental impact",
        "Site prominence (bubble size) correlates with visitor numbers but not necessarily with cultural significance",
        "Lesser-known sites provide opportunities for more authentic cultural experiences"
    ])
    
    # Add spacing after the section
    st.markdown("<div style='margin-bottom: 40px;'></div>", unsafe_allow_html=True)
    
    # NEW: Sankey Diagram - Flow of Tourism Revenue
    st.markdown("<h2 class='sub-header'>💰 Flow of Tourism Revenue: Hotspots vs. Untouched Sites</h2>", unsafe_allow_html=True)
    
    # Create sample data for the Sankey diagram
    popular_sites = ['Taj Mahal', 'Qutub Minar', 'Konark Sun Temple']
    lesser_sites = ['Champaner-Pavagadh', 'Majuli Island', 'Chettinad']
    destinations = ['Infrastructure', 'Local Communities', 'Preservation', 'Administration', 'Marketing']
    
    # Generate labels for Sankey diagram
    labels = popular_sites + lesser_sites + destinations
    
    # Define source, target, and value for popular sites
    source_popular = []
    target_popular = []
    value_popular = []
    
    # Taj Mahal: 70% infrastructure, 10% local communities, 15% preservation, 5% admin
    source_popular.extend([0, 0, 0, 0, 0])
    target_popular.extend([6, 7, 8, 9, 10])  # Indices of destinations
    value_popular.extend([70, 10, 15, 3, 2])  # Percentages
    
    # Qutub Minar: 65% infrastructure, 15% local communities, 10% preservation, 10% admin
    source_popular.extend([1, 1, 1, 1, 1])
    target_popular.extend([6, 7, 8, 9, 10])
    value_popular.extend([65, 15, 10, 5, 5])
    
    # Konark: 60% infrastructure, 20% local communities, 15% preservation, 5% admin
    source_popular.extend([2, 2, 2, 2, 2])
    target_popular.extend([6, 7, 8, 9, 10])
    value_popular.extend([60, 20, 15, 3, 2])
    
    # Define source, target, and value for lesser-known sites
    source_lesser = []
    target_lesser = []
    value_lesser = []
    
    # Champaner: 20% infrastructure, 50% local communities, 20% preservation, 10% admin
    source_lesser.extend([3, 3, 3, 3, 3])
    target_lesser.extend([6, 7, 8, 9, 10])
    value_lesser.extend([20, 50, 20, 7, 3])
    
    # Majuli: 15% infrastructure, 60% local communities, 15% preservation, 10% admin
    source_lesser.extend([4, 4, 4, 4, 4])
    target_lesser.extend([6, 7, 8, 9, 10])
    value_lesser.extend([15, 60, 15, 8, 2])
    
    # Chettinad: 25% infrastructure, 55% local communities, 10% preservation, 10% admin
    source_lesser.extend([5, 5, 5, 5, 5])
    target_lesser.extend([6, 7, 8, 9, 10])
    value_lesser.extend([25, 55, 10, 7, 3])
    
    # Combine all data
    source = source_popular + source_lesser
    target = target_popular + target_lesser
    value = value_popular + value_lesser
    
    # Scale values for better visualization (values are percentages, but need absolute numbers for visual impact)
    # Popular sites have much higher revenue, so scale accordingly
    for i in range(len(source_popular)):
        value[i] = value[i] * 10  # Scale popular sites by factor of 10
    
    # Create array of colors for links - using different semi-transparent shades
    link_colors = [
        # Popular sites - different red/orange shades
        'rgba(255,107,107,0.6)', 'rgba(255,107,107,0.6)', 'rgba(255,107,107,0.6)', 'rgba(255,107,107,0.6)', 'rgba(255,107,107,0.6)',  # Taj Mahal
        'rgba(255,159,107,0.6)', 'rgba(255,159,107,0.6)', 'rgba(255,159,107,0.6)', 'rgba(255,159,107,0.6)', 'rgba(255,159,107,0.6)',  # Qutub Minar
        'rgba(255,191,107,0.6)', 'rgba(255,191,107,0.6)', 'rgba(255,191,107,0.6)', 'rgba(255,191,107,0.6)', 'rgba(255,191,107,0.6)',  # Konark
        
        # Lesser sites - different teal/blue shades
        'rgba(78,205,196,0.6)', 'rgba(78,205,196,0.6)', 'rgba(78,205,196,0.6)', 'rgba(78,205,196,0.6)', 'rgba(78,205,196,0.6)',  # Champaner
        'rgba(78,196,205,0.6)', 'rgba(78,196,205,0.6)', 'rgba(78,196,205,0.6)', 'rgba(78,196,205,0.6)', 'rgba(78,196,205,0.6)',  # Majuli
        'rgba(78,170,205,0.6)', 'rgba(78,170,205,0.6)', 'rgba(78,170,205,0.6)', 'rgba(78,170,205,0.6)', 'rgba(78,170,205,0.6)'   # Chettinad
    ]
    
    # Create Sankey diagram
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=labels,
            color=["#FF6B6B", "#FF9F6B", "#FFB56B",  # Popular sites (red/orange shades)
                   "#4ECDC4", "#4EC5DC", "#4EAADA",  # Lesser sites (teal/blue shades)
                   "#FFD166", "#06D6A0", "#118AB2", "#073B4C", "#EF476F"]  # Destinations (varied)
        ),
        link=dict(
            source=source,
            target=target,
            value=value,
            color=link_colors
        )
    )])
    
    fig.update_layout(
        title_text="Revenue Flow from Heritage Sites to Local Economy",
        font_size=12,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        title_font=dict(size=20),
        height=600,
        margin=dict(t=50, b=50, l=50, r=50)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Add insights below the Sankey chart
    display_insights("Key Insights", [
        "Popular sites like Taj Mahal direct most revenue (70%) toward infrastructure development",
        "Lesser-known sites like Champaner-Pavagadh allocate significantly more revenue (50-60%) to local communities",
        "Preservation efforts receive similar proportions from both types of sites (10-20%)",
        "Hidden gems create more sustainable economic benefits for local artisans and communities"
    ])
    
    # Add spacing after the section
    st.markdown("<div style='margin-bottom: 40px;'></div>", unsafe_allow_html=True)
    
    # NEW: Stacked Area Chart - Visitor Distribution Over Time
    st.markdown("<h2 class='sub-header'>👥 Visitor Distribution Over Time: Hotspots vs. Untouched Sites</h2>", unsafe_allow_html=True)
    
    # Create sample data for monthly visitor counts
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    # Popular sites have seasonal peaks
    taj_mahal = [600000, 700000, 800000, 500000, 400000, 300000, 650000, 700000, 800000, 900000, 1000000, 750000]
    qutub_minar = [300000, 350000, 400000, 250000, 200000, 150000, 300000, 350000, 400000, 450000, 500000, 350000]
    konark = [250000, 280000, 300000, 200000, 150000, 120000, 250000, 300000, 350000, 380000, 400000, 320000]
    
    # Lesser-known sites have more consistent visitor numbers
    champaner = [60000, 65000, 70000, 62000, 58000, 55000, 60000, 68000, 72000, 75000, 80000, 70000]
    majuli = [40000, 42000, 45000, 41000, 38000, 35000, 40000, 43000, 48000, 50000, 52000, 45000]
    chettinad = [45000, 48000, 52000, 46000, 43000, 40000, 45000, 50000, 55000, 58000, 60000, 50000]
    
    # Create DataFrame for the stacked area chart
    visitor_data = pd.DataFrame({
        'Month': months * 6,
        'Site': ['Taj Mahal'] * 12 + ['Qutub Minar'] * 12 + ['Konark Sun Temple'] * 12 +
               ['Champaner-Pavagadh'] * 12 + ['Majuli Island'] * 12 + ['Chettinad'] * 12,
        'Visitors': taj_mahal + qutub_minar + konark + champaner + majuli + chettinad,
        'Category': ['Popular Site'] * 36 + ['Hidden Gem'] * 36
    })
    
    # stacked area chart
    fig = px.area(
        visitor_data,
        x='Month',
        y='Visitors',
        color='Site',
        line_group='Site',
        title='Monthly Visitor Distribution Across Heritage Sites',
        labels={'Visitors': 'Number of Visitors', 'Month': 'Month'},
        color_discrete_sequence=['#FF6B6B', '#FF9F80', '#FFBF80', '#4ECDC4', '#A2FAE8', '#80CBC4'],
        template='plotly_dark'
    )
    
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', size=12),
        title_font=dict(size=20),
        height=600,
        margin=dict(t=50, b=50, l=50, r=50),
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99,
            bgcolor='rgba(0,0,0,0.5)',
            bordercolor='rgba(255,255,255,0.2)',
            borderwidth=1
        )
    )
    
    
    fig.add_annotation(
        x='Nov',
        y=1000000,
        text="Peak Season",
        showarrow=True,
        arrowhead=1,
        ax=0,
        ay=-40,
        font=dict(color='white', size=12)
    )
    
    fig.add_annotation(
        x='Jun',
        y=300000,
        text="Off-Season Opportunity",
        showarrow=True,
        arrowhead=1,
        ax=0,
        ay=40,
        font=dict(color='white', size=12)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Add insights below the chart
    display_insights("Key Insights", [
        "Popular sites show significant seasonality with visitor peaks in October-November",
        "Hidden gems maintain relatively steady visitor numbers throughout the year",
        "Off-season months (May-June) present opportunities to redirect tourists to lesser-known sites",
        "Distributing tourism across sites and seasons can reduce over-tourism impacts"
    ])
    
 
    st.markdown("<div style='margin-bottom: 40px;'></div>", unsafe_allow_html=True)
   
    st.markdown("<h2 class='sub-header'>🌍 Environmental Impact Analysis</h2>", unsafe_allow_html=True)
    
    # Create sample environmental impact data
    impact_data = pd.DataFrame({
        'site': ['Taj Mahal', 'Qutub Minar', 'Konark Sun Temple', 'Champaner-Pavagadh', 'Majuli Island'],
        'carbon_footprint': [1200, 800, 600, 300, 200],
        'water_usage': [5000, 3000, 2000, 1000, 800],
        'waste_generation': [800, 500, 400, 200, 150]
    })
    
    # Create a bar chart for environmental impact
    fig = px.bar(
        impact_data,
        x='site',
        y=['carbon_footprint', 'water_usage', 'waste_generation'],
        title='Environmental Impact Comparison',
        labels={'value': 'Impact Units', 'site': 'Heritage Site'},
        color_discrete_sequence=['#2E8B57', '#4169E1', '#8B4513'],  # Green for carbon, Blue for water, Brown for waste
        template='plotly_dark',
        barmode='group'
    )
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', size=12),
        title_font=dict(size=20),
        height=500,
        margin=dict(t=50, b=50, l=50, r=50),
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99,
            bgcolor='rgba(0,0,0,0.5)',
            bordercolor='rgba(255,255,255,0.2)',
            borderwidth=1
        )
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Add insights below the chart
    display_insights("Key Insights", [
        "Taj Mahal shows the highest environmental impact across all metrics due to high visitor numbers",
        "Lesser-known sites like Majuli Island demonstrate significantly lower environmental impact",
        "Water usage is the most significant environmental factor across all sites",
        "Sustainable tourism initiatives have reduced waste generation by 20-30% at participating sites"
    ])
    
    # Add spacing after the section
    st.markdown("<div style='margin-bottom: 40px;'></div>", unsafe_allow_html=True)
    
    # Responsible Tourism Tips Section
    st.markdown("<h2 class='sub-header'>💡 Responsible Tourism Tips</h2>", unsafe_allow_html=True)
    
    # Create a grid of cards for tips
    cols = st.columns(2)
    for idx, category in enumerate(responsible_tourism_tips):
        with cols[idx % 2]:
            tips_list = "".join([f"<li>{tip}</li>" for tip in category['tips']])
            st.markdown(f"""
            <div class='art-card' style='margin-bottom: 20px;'>
                <div class='card-content'>
                    <div class='card-title'>{category['category']}</div>
                    <ul>{tips_list}</ul>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Add spacing after the cards section
    st.markdown("<div style='margin-bottom: 40px;'></div>", unsafe_allow_html=True)
    
    # Sustainable Tourism Impact
    st.markdown("<h2 class='sub-header'>📊 Sustainable Tourism Impact</h2>", unsafe_allow_html=True)
    
    # Create sample data for sustainable tourism impact
    metrics = ['Local Employment', 'Cultural Preservation', 'Environmental Conservation', 'Community Development', 'Economic Growth']
    traditional_values = [60, 40, 30, 45, 70]
    sustainable_values = [85, 90, 80, 75, 65]
    
    # Create the radar chart
    fig = go.Figure()
    
    # Add traditional tourism trace
    fig.add_trace(go.Scatterpolar(
        r=traditional_values,
        theta=metrics,
        fill='toself',
        name='Traditional Tourism',
        line_color='#FF6B6B',
        fillcolor='rgba(255, 107, 107, 0.3)'
    ))
    
    # Add sustainable tourism trace
    fig.add_trace(go.Scatterpolar(
        r=sustainable_values,
        theta=metrics,
        fill='toself',
        name='Sustainable Tourism',
        line_color='#4ECDC4',
        fillcolor='rgba(78, 205, 196, 0.3)'
    ))
    
    # Update layout
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                showticklabels=True,
                tickfont=dict(color='white'),
                gridcolor='rgba(255, 255, 255, 0.1)'
            ),
            angularaxis=dict(
                tickfont=dict(color='white'),
                gridcolor='rgba(255, 255, 255, 0.1)'
            ),
            bgcolor='rgba(0,0,0,0)'
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', size=12),
        title_font=dict(size=20),
        height=500,
        margin=dict(t=50, b=50, l=50, r=50),
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99,
            bgcolor='rgba(0,0,0,0.5)',
            bordercolor='rgba(255,255,255,0.2)',
            borderwidth=1
        ),
        title='Impact of Sustainable Tourism Practices'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Add insights below the chart
    display_insights("Key Insights", [
        "Sustainable tourism shows higher impact in cultural preservation and environmental conservation",
        "Traditional tourism still leads in economic growth but at the cost of environmental impact",
        "Community development and local employment are significantly better with sustainable practices",
        "Balanced approach needed to maintain economic benefits while improving sustainability"
    ]) 