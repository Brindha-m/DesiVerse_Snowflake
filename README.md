<img src="https://github.com/user-attachments/assets/c8382ec5-6b96-44e7-9faa-2f654ee75281" width=250/>

## Indian cultural Heritage and Tourism Analytics

### YourStory | Snowflake - Hero Challenge dashboard - Team Bindas Code

<br>

> **DesiVerse weaves data and passion to celebrate India’s art, guide you to soulful places, and help you travel kindly. It’s about feeling India’s heartbeat, finding secret gems, and leaving a gentle footprint while supporting local artisans.**

>  **Built with Streamlit, data sourced from data.gov.in and stored in Snowflake.**

## Features - What You Can Get from DesiVerse

- **Heritage Walks**: Interactive maps of cultural sites, showcasing art forms with visitors count and funding data.
  
   <img src="https://github.com/user-attachments/assets/28534af2-26c9-4cf0-af96-da96e3d4825e" width=750/>
   

- **Tourism Analytics**: Data visualizations of trends, highlighting top states, seasonal peaks, and growth.

  <img width="750" alt="Screenshot_20250523_061322" src="https://github.com/user-attachments/assets/7a844dfc-bcad-4b7e-9069-077d1cfc677c" />

  <img width="750" alt="Screenshot_20250523_043807" src="https://github.com/user-attachments/assets/83374502-5c61-4efb-a785-590e0b44b755" />

- **Responsible Tourism**: Guides on reducing carbon footprints, water usage, and waste, plus sustainable practices, comparing hotspots (e.g., Rajasthan) to untouched sites (e.g., Northeast).

  <img width="750" alt="Screenshot_20250523_061601" src="https://github.com/user-attachments/assets/632eec41-5fe5-412a-899f-8d16a21cf135" />

- **Desi Gallery**: Vibrant showcase of hidden gem spots, festivals, and art forms with images sourced from pexels.
  
   <img width="750" alt="Screenshot_20250523_011050" src="https://github.com/user-attachments/assets/6cf2ffd2-ecf1-443b-bc7e-68328b173f99" />

- **Culture Quest**: Engaging quizzes on Indian art and culture.
  
  <img width="750" alt="Screenshot_20250523_044533" src="https://github.com/user-attachments/assets/62fb2745-49f4-445a-9723-18127d6e9c48" />


## Installation

1. Clone the repository:
```bash
git clone https://github.com/Brindha-m/DesiVerse_Snowflake.git
cd DesiVerse
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
streamlit run app.py
```

## Project Structure

```
DesiVerse/
├── app.py                  # Main file
├── snowflake_config.py     # Snowflake database setup
├── data/                   # Data-related modules
│   ├── constants.py        # Constants and shared data
│   └── data_generator.py   # Data sourced from data.gov.in
├── components/            
│   └── styling.py          
├── pages/                  # application pages
│   ├── heritage_explorer.py
│   ├── tourism_analytics.py
│   ├── responsible_tourism.py 
│   ├── cultural_gallery.py
│   └── cultural_quiz.py
├── utils/                  
│   ├── image_utils.py      
│   └── visualization.py    
└── requirements.txt        
```

## Tech Stack

The application requires the following packages / libraries:

- Streamlit
- Snowflake-connector-python
- Pandas
- NumPy
- Plotly
- Matplotlib
- Seaborn
- WordCloud
- Folium maps
- Beautifulsoup4



## API Keys

The application uses the following external APIs:
- Pexels API for image retrieval
- Pixabay API as a fallback for images

You'll need to obtain API keys and add them to the `data/constants.py` file.

## Data Source:
```
    The data is inspired by and sourced from https://www.data.gov.in, 
    specifically datasets like 'Domestic and Foreign Tourist Visits to States/UTs' and 'India TourismStatistics'.
    Additional data may include simulated or projected values for cultural tourism (e.g., art-form-specific visits, 2020–2025 trends) to support DesiVerse's analytics. 

```
## License

This project is licensed under the MIT License - see the LICENSE file for details.
