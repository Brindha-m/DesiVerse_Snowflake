# DesiVerse: Indian Heritage Tourism Analytics

DesiVerse is a Streamlit application that showcases Indian cultural heritage and tourism data through interactive visualizations and educational content.

![DesiVerse Screenshot](https://placehold.co/600x400?text=DesiVerse+Screenshot)

## Features

- **Heritage Explorer**: Interactive map of heritage sites with detailed information on art forms
- **Tourism Analytics**: Data visualizations showing tourism trends and patterns
- **Responsible Tourism**: Information on sustainable tourism practices and lesser-known heritage sites
- **Cultural Gallery**: Collection of images showcasing Indian festivals, dance forms, heritage sites, and crafts
- **Cultural Quiz**: Interactive quiz testing knowledge of Indian art and culture

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

4. Run the application:
```bash
streamlit run app.py
```

## Project Structure

```
DesiVerse/
├── app.py                  # Main application file
├── data/                   # Data-related modules
│   ├── constants.py        # Constants and shared data
│   └── data_generator.py   # Mock data generation functions
├── components/             # UI components
│   └── styling.py          # CSS styles and UI helper functions
├── pages/                  # Individual application pages
│   ├── heritage_explorer.py
│   ├── tourism_analytics.py
│   ├── responsible_tourism.py 
│   ├── cultural_gallery.py
│   └── cultural_quiz.py
├── utils/                  # Utility functions
│   ├── image_utils.py      # Image fetching and processing
│   └── visualization.py    # Data visualization functions
└── requirements.txt        # Project dependencies
```

## Dependencies

The application requires the following main packages:
- Streamlit
- Pandas
- NumPy
- Plotly
- Matplotlib
- Seaborn
- WordCloud

A complete list is available in `requirements.txt`.

## API Keys

The application uses the following external APIs:
- Pexels API for image retrieval
- Pixabay API as a fallback for images

You'll need to obtain API keys and add them to the `data/constants.py` file.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Data sources: Mock data is generated for demonstration purposes
- Images: Retrieved from Pexels API
- Indian heritage information: Based on publicly available information 