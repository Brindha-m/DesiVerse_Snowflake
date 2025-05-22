"""
Visualization functions for DesiVerse application.
"""

import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap
from wordcloud import WordCloud
from data.constants import INDIAN_COLORS

# Create custom colormaps
indian_cmap = LinearSegmentedColormap.from_list('indian_cmap', INDIAN_COLORS['gradient'])
earth_cmap = LinearSegmentedColormap.from_list('earth_cmap', INDIAN_COLORS['earth'])

def create_map_visualization(data, title="Cultural Heritage Sites Across India"):
    """
    Create an interactive map visualization with cultural heritage sites.
    
    Args:
        data (DataFrame): DataFrame containing latitude, longitude, and other site data
        title (str): Title for the map
        
    Returns:
        plotly.graph_objects.Figure: The map figure
    """
    # Determine which columns to include in hover data
    hover_data = []
    if 'tourist_visits' in data.columns:
        hover_data.append('tourist_visits')
    if 'art_form' in data.columns:
        hover_data.append('art_form')
    
    fig = px.scatter_mapbox(
        data,
        lat='latitude',
        lon='longitude',
        hover_name='state',
        hover_data=hover_data,
        size='tourist_visits',
        color='tourist_visits',
        color_continuous_scale='Viridis',
        size_max=15,
        zoom=3,
        mapbox_style="carto-darkmatter",
        title=title
    )
    
    fig.update_layout(
        margin={"r":0,"t":30,"l":0,"b":0},
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', size=12),
        title_font=dict(size=20),
        height=500
    )
    
    return fig

def create_pie_chart(data, values_col, names_col, title):
    """
    Create a pie chart visualization.
    
    Args:
        data (DataFrame): DataFrame containing the data
        values_col (str): Column name for pie chart values
        names_col (str): Column name for pie chart category names
        title (str): Title for the chart
        
    Returns:
        plotly.graph_objects.Figure: The pie chart figure
    """
    fig = px.pie(
        data,
        values=values_col,
        names=names_col,
        title=title,
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', size=12),
        title_font=dict(size=16),
        height=400,
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
    
    return fig

def create_bar_chart(data, x_col, y_col, title, color_col=None):
    """
    Create a bar chart visualization.
    
    Args:
        data (DataFrame): DataFrame containing the data
        x_col (str): Column name for x-axis
        y_col (str): Column name for y-axis values
        title (str): Title for the chart
        color_col (str, optional): Column name for color encoding
        
    Returns:
        plotly.graph_objects.Figure: The bar chart figure
    """
    if color_col:
        fig = px.bar(
            data,
            x=x_col,
            y=y_col,
            title=title,
            color=color_col,
            color_continuous_scale='Viridis'
        )
    else:
        fig = px.bar(
            data,
            x=x_col,
            y=y_col,
            title=title,
            color_discrete_sequence=INDIAN_COLORS['secondary']
        )
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', size=12),
        title_font=dict(size=16),
        height=400,
        margin=dict(t=50, b=50, l=50, r=50),
        xaxis=dict(tickangle=45),
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
    
    return fig

def create_grouped_bar_chart(data, x_col, y_cols, title):
    """
    Create a grouped bar chart visualization.
    
    Args:
        data (DataFrame): DataFrame containing the data
        x_col (str): Column name for x-axis
        y_cols (list): List of column names for y-axis values
        title (str): Title for the chart
        
    Returns:
        plotly.graph_objects.Figure: The grouped bar chart figure
    """
    fig = px.bar(
        data,
        x=x_col,
        y=y_cols,
        barmode='group',
        title=title,
        color_discrete_sequence=['#138808', '#FF9933'],  # Green for domestic, Saffron for foreign
        labels={'value': 'Number of Visitors', 'variable': 'Visitor Type'},
        template='plotly_dark'
    )
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', size=12),
        title_font=dict(size=20),
        height=500,
        margin=dict(t=50, b=50, l=50, r=50),
        legend=dict(
            title='Visitor Type',
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99,
            bgcolor='rgba(0,0,0,0.5)',
            bordercolor='rgba(255,255,255,0.2)',
            borderwidth=1
        )
    )
    
    return fig

def create_line_chart(data, x_col, y_col, title):
    """
    Create a line chart visualization.
    
    Args:
        data (DataFrame): DataFrame containing the data
        x_col (str): Column name for x-axis
        y_col (str or list): Column name(s) for y-axis values
        title (str): Title for the chart
        
    Returns:
        plotly.graph_objects.Figure: The line chart figure
    """
    fig = px.line(
        data,
        x=x_col,
        y=y_col,
        title=title,
        labels={'value': 'Count', 'variable': 'Metric'},
        color_discrete_sequence=['#FF6B6B', '#4ECDC4']
    )
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', size=12),
        title_font=dict(size=16),
        height=400,
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
    
    return fig

def create_heatmap(data, x_labels, title):
    """
    Create a heatmap visualization.
    
    Args:
        data (DataFrame): DataFrame containing the heatmap data
        x_labels (list): List of labels for x-axis
        title (str): Title for the chart
        
    Returns:
        plotly.graph_objects.Figure: The heatmap figure
    """
    fig = px.imshow(
        data,
        labels=dict(x="Month", y="Region", color="Tourist Visits"),
        x=x_labels,
        aspect="auto",
        color_continuous_scale='Viridis',
        title=title
    )
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', size=12),
        title_font=dict(size=16),
        height=400,
        margin=dict(t=50, b=50, l=50, r=50)
    )
    
    return fig

def create_scatter_plot(data, x_col, y_col, color_col, title, hover_data=None):
    """
    Create a scatter plot visualization.
    
    Args:
        data (DataFrame): DataFrame containing the data
        x_col (str): Column name for x-axis
        y_col (str): Column name for y-axis
        color_col (str): Column name for color encoding
        title (str): Title for the chart
        hover_data (list, optional): List of column names to include in hover data
        
    Returns:
        plotly.graph_objects.Figure: The scatter plot figure
    """
    fig = px.scatter(
        data,
        x=x_col,
        y=y_col,
        color=color_col,
        hover_data=hover_data,
        title=title,
        template='plotly_dark'
    )
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', size=12),
        title_font=dict(size=16),
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
    
    return fig

def create_bubble_chart(data, x_col, y_col, size_col, color_col, title):
    """
    Create a bubble chart visualization.
    
    Args:
        data (DataFrame): DataFrame containing the data
        x_col (str): Column name for x-axis
        y_col (str): Column name for y-axis
        size_col (str): Column name for bubble size
        color_col (str): Column name for bubble color
        title (str): Title for the chart
        
    Returns:
        plotly.graph_objects.Figure: The bubble chart figure
    """
    fig = px.scatter(
        data,
        x=x_col,
        y=y_col,
        size=size_col,
        color=color_col,
        hover_name='site' if 'site' in data.columns else None,
        title=title,
        size_max=50,
        color_discrete_sequence=['#FF6B6B', '#4ECDC4'],
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
    
    return fig

def create_radar_chart(categories, values1, values2, names, title):
    """
    Create a radar chart visualization.
    
    Args:
        categories (list): List of category labels
        values1 (list): Values for the first series
        values2 (list): Values for the second series
        names (list): Names for the two series
        title (str): Title for the chart
        
    Returns:
        plotly.graph_objects.Figure: The radar chart figure
    """
    fig = go.Figure()
    
    # Add first trace
    fig.add_trace(go.Scatterpolar(
        r=values1,
        theta=categories,
        fill='toself',
        name=names[0],
        line_color='#FF6B6B',
        fillcolor='rgba(255, 107, 107, 0.3)'
    ))
    
    # Add second trace
    fig.add_trace(go.Scatterpolar(
        r=values2,
        theta=categories,
        fill='toself',
        name=names[1],
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
        title=title
    )
    
    return fig

def create_correlation_heatmap(data, title="Correlation Analysis"):
    """
    Create a correlation heatmap visualization using seaborn and matplotlib.
    
    Args:
        data (DataFrame): DataFrame containing the correlation data
        title (str): Title for the chart
        
    Returns:
        matplotlib.figure.Figure: The heatmap figure
    """
    plt.figure(figsize=(10, 6), facecolor='black')
    ax = plt.gca()
    ax.set_facecolor('black')
    
    sns.heatmap(
        data,
        annot=True,
        cmap=indian_cmap,
        center=0,
        fmt='.2f',
        linewidths=0.5,
        cbar_kws={'label': 'Correlation Coefficient'},
        annot_kws={'color': 'white'},
        xticklabels=True,
        yticklabels=True
    )
    
    plt.title(title, pad=20, color='white')
    plt.xticks(rotation=45, ha='right', color='white')
    plt.yticks(rotation=0, color='white')
    
    # Remove white background
    plt.gcf().set_facecolor('black')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    return plt.gcf()

def create_wordcloud(word_frequencies, title="Popular Indian Art Forms"):
    """
    Create a word cloud visualization.
    
    Args:
        word_frequencies (dict): Dictionary mapping words to their frequencies
        title (str): Title for the chart
        
    Returns:
        matplotlib.figure.Figure: The wordcloud figure
    """
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='black',
        colormap=earth_cmap,
        prefer_horizontal=0.9,
        min_font_size=10,
        max_font_size=100,
        relative_scaling=0.5
    ).generate_from_frequencies(word_frequencies)
    
    plt.figure(figsize=(10, 5), facecolor='black')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title, pad=20, color='white')
    
    # Remove white background
    plt.gcf().set_facecolor('black')
    
    return plt.gcf()

def create_tourism_bar_chart(domestic_data, foreign_data, sites, title="Visitor Distribution at Top Heritage Sites"):
    """
    Create a bar chart comparing domestic and foreign visitors at top heritage sites.
    
    Args:
        domestic_data (list): List of domestic visitor numbers
        foreign_data (list): List of foreign visitor numbers
        sites (list): List of heritage site names
        title (str): Title for the chart
        
    Returns:
        plotly.graph_objects.Figure: The bar chart figure
    """
    # Create DataFrame
    df = pd.DataFrame({
        'site': sites,
        'domestic_visitors': domestic_data,
        'foreign_visitors': foreign_data
    })
    
    fig = px.bar(
        df,
        x='site',
        y=['domestic_visitors', 'foreign_visitors'],
        barmode='group',
        title=title,
        color_discrete_sequence=['#1f77b4', '#ff7f0e'],  # Blue for domestic, orange for foreign
        labels={
            'value': 'Number of Visitors', 
            'variable': 'Visitor Type',
            'site': 'Heritage Site'
        }
    )
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', size=12),
        title_font=dict(size=20),
        height=500,
        margin=dict(t=50, b=50, l=50, r=50),
        legend=dict(
            title='Visitor Type',
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99,
            bgcolor='rgba(0,0,0,0.5)',
            bordercolor='rgba(255,255,255,0.2)',
            borderwidth=1
        )
    )
    
    return fig

def create_seasonal_line_chart(months, domestic_data, foreign_data, title="Monthly Tourism Trends"):
    """
    Create a line chart showing seasonal tourism trends.
    
    Args:
        months (list): List of month names
        domestic_data (list): List of domestic visitor numbers by month
        foreign_data (list): List of foreign visitor numbers by month
        title (str): Title for the chart
        
    Returns:
        plotly.graph_objects.Figure: The line chart figure
    """
    # Create DataFrame
    df = pd.DataFrame({
        'Month': months * 2,
        'Visitors': domestic_data + foreign_data,
        'Type': ['Domestic'] * len(months) + ['Foreign'] * len(months)
    })
    
    # Create figure using plotly.graph_objects for more control
    fig = go.Figure()
    
    # Add domestic visitors line
    fig.add_trace(go.Scatter(
        x=df[df['Type'] == 'Domestic']['Month'],
        y=df[df['Type'] == 'Domestic']['Visitors'],
        mode='lines+markers',
        name='Domestic Visitors',
        line=dict(color='#2ca02c', width=3),
        marker=dict(size=8)
    ))
    
    # Add foreign visitors line
    fig.add_trace(go.Scatter(
        x=df[df['Type'] == 'Foreign']['Month'],
        y=df[df['Type'] == 'Foreign']['Visitors'],
        mode='lines+markers',
        name='Foreign Visitors',
        line=dict(color='#d62728', width=3),
        marker=dict(size=8)
    ))
    
    # Update layout
    fig.update_layout(
        title=title,
        xaxis_title='Month',
        yaxis_title='Number of Visitors',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', size=12),
        title_font=dict(size=20),
        height=500,
        margin=dict(t=50, b=50, l=50, r=50),
        legend=dict(
            title='Visitor Type',
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99,
            bgcolor='rgba(0,0,0,0.5)',
            bordercolor='rgba(255,255,255,0.2)',
            borderwidth=1
        ),
        xaxis=dict(
            gridcolor='rgba(255,255,255,0.1)',
            tickfont=dict(color='white')
        ),
        yaxis=dict(
            gridcolor='rgba(255,255,255,0.1)',
            tickfont=dict(color='white')
        )
    )
    
    return fig

def create_tourism_pie_chart(categories, values, title="Distribution of Tourism Types"):
    """
    Create a pie chart showing distribution of tourism types.
    
    Args:
        categories (list): List of tourism type categories
        values (list): List of percentage values for each category
        title (str): Title for the chart
        
    Returns:
        plotly.graph_objects.Figure: The pie chart figure
    """
    # Create DataFrame
    df = pd.DataFrame({
        'type': categories,
        'percentage': values
    })
    
    # Use vibrant Indian-inspired color palette
    color_sequence = ['#FF9933', '#138808', '#000080', '#DAA520', '#800080']  # Saffron, green, blue, mustard, purple
    
    fig = px.pie(
        df,
        values='percentage',
        names='type',
        title=title,
        color_discrete_sequence=color_sequence
    )
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', size=12),
        title_font=dict(size=20),
        height=500,
        margin=dict(t=50, b=50, l=50, r=50),
        legend=dict(
            title='Tourism Type',
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01,
            bgcolor='rgba(0,0,0,0.5)',
            bordercolor='rgba(255,255,255,0.2)',
            borderwidth=1
        )
    )
    
    return fig

def create_funding_heatmap(data, x_labels, y_labels, title="Funding Impact Correlation"):
    """
    Create a correlation heatmap showing impact of government initiatives.
    
    Args:
        data (numpy.ndarray): 2D array of correlation values
        x_labels (list): Labels for x-axis (columns)
        y_labels (list): Labels for y-axis (rows)
        title (str): Title for the chart
        
    Returns:
        matplotlib.figure.Figure: The heatmap figure
    """
    plt.figure(figsize=(10, 8), facecolor='black')
    ax = plt.gca()
    ax.set_facecolor('black')
    
    # Blue to red gradient for correlation
    cmap = sns.diverging_palette(240, 10, as_cmap=True)
    
    sns.heatmap(
        data,
        annot=True,
        cmap=cmap,
        center=0,
        fmt='.2f',
        linewidths=0.5,
        cbar_kws={'label': 'Correlation Coefficient'},
        annot_kws={'color': 'white'},
        xticklabels=x_labels,
        yticklabels=y_labels
    )
    
    plt.title(title, pad=20, color='white', fontsize=20)
    plt.xticks(rotation=45, ha='right', color='white')
    plt.yticks(rotation=0, color='white')
    
    # Remove white background
    plt.gcf().set_facecolor('black')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    return plt.gcf()

def create_art_forms_wordcloud(word_frequencies, title="Popular Indian Art Forms"):
    """
    Create a word cloud visualization of popular art forms.
    
    Args:
        word_frequencies (dict): Dictionary mapping words to their frequencies
        title (str): Title for the chart
        
    Returns:
        matplotlib.figure.Figure: The wordcloud figure
    """
    # Create a custom color map with earthy tones and saffron highlights
    earthy_colors = [(0, '#8B4513'), (0.3, '#A0522D'), (0.5, '#CD853F'), (0.8, '#DEB887'), (1.0, '#FF9933')]
    earthy_cmap = LinearSegmentedColormap.from_list('earthy_cmap', earthy_colors)
    
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='black',
        colormap=earthy_cmap,
        prefer_horizontal=0.9,
        min_font_size=10,
        max_font_size=100,
        relative_scaling=0.5
    ).generate_from_frequencies(word_frequencies)
    
    plt.figure(figsize=(12, 6), facecolor='black')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title, pad=20, color='white', fontsize=20)
    
    # Remove white background
    plt.gcf().set_facecolor('black')
    
    return plt.gcf()

def create_state_choropleth(df, geo_json, title="Tourist Footfall by State"):
    """
    Create a choropleth map showing tourism data by state.
    
    Args:
        df (DataFrame): DataFrame with state-wise data
        geo_json (dict): GeoJSON data for India states
        title (str): Title for the chart
        
    Returns:
        plotly.graph_objects.Figure: The choropleth map figure
    """
    fig = px.choropleth_mapbox(
        df,
        geojson=geo_json,
        locations='state',
        color='visitors',
        featureidkey="properties.ST_NM",
        center={"lat": 23.5937, "lon": 78.9629},
        mapbox_style="carto-darkmatter",
        zoom=3.5,
        opacity=0.7,
        labels={'visitors': 'Visitors'},
        color_continuous_scale="Viridis",
        title=title
    )
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', size=12),
        title_font=dict(size=20),
        margin={"r":0,"t":50,"l":0,"b":0},
        height=600
    )
    
    return fig 