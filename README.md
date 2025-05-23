# DesiVerse: Indian Heritage Tourism Analytics

DesiVerse is a Streamlit application that showcases Indian cultural heritage and tourism data through interactive visualizations and educational content.

![DesiVerse Screenshot](https://placehold.co/600x400?text=DesiVerse+Screenshot)

## Features

- **Heritage Explorer**: Interactive map of heritage sites with detailed information on art forms
- **Tourism Analytics**: Data visualizations showing tourism trends and patterns
- **Responsible Tourism**: Information on sustainable tourism practices and lesser-known heritage sites
- **Cultural Gallery**: Collection of images showcasing Indian festivals, dance forms, heritage sites, and crafts
- **Cultural Quiz**: Interactive quiz testing knowledge of Indian art and culture

## Project Structure

```
DesiVerse/
├── app.py                  # Main file
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

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/DesiVerse.git
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

4. Set up Snowflake credentials:
   - Create a `snowflake_config.py` file in the root directory
   - Add your Snowflake credentials:
   ```python
   # Snowflake Configuration
   SNOWFLAKE_CONFIG = {
       'user': 'brindhamanickavasakan',
       'password': '28NDBnCKvXnjriH',
       'account': 'aj44614.ap-southeast-1', 
       'warehouse': 'HERITAGE_WH',
       'database': 'DESIVERSE',
       'schema': 'HERITAGE_DATA'
   }
   ```

5. Run the application:
```bash
streamlit run app.py
```

## Data Sources

The application uses data from various sources:
- Tourism statistics from data.gov.in
- Heritage site information from Archaeological Survey of India
- Art form data from Ministry of Culture
- Regional tourism data from state tourism departments

## Features in Detail

### Heritage Explorer
- Interactive map showing heritage sites across India
- Detailed information about each site
- Art forms associated with each region
- Historical significance and cultural importance

### Tourism Analytics
- Year-wise tourism trends
- Regional analysis
- Seasonal patterns
- Funding distribution
- Art form popularity metrics

### Responsible Tourism
- Sustainable tourism practices
- Lesser-known heritage sites
- Community impact
- Conservation efforts
- Cultural preservation initiatives

### Cultural Gallery
- High-quality images of Indian art forms
- Festival celebrations
- Heritage sites
- Traditional crafts
- Dance forms

### Cultural Quiz
- Interactive quiz on Indian heritage
- Multiple choice questions
- Score tracking
- Educational content
- Cultural facts

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Data.gov.in for tourism statistics
- Archaeological Survey of India for heritage site information
- Ministry of Culture for art form data
- State tourism departments for regional data 