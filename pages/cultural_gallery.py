"""
Desi Gallery page for DesiVerse application.
Displays galleries of cultural images organized by categories and hidden gems of India.
"""

import streamlit as st
import urllib.parse
import requests
import sys
import os
import random

# Add the project root to the path so imports work correctly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.constants import CULTURAL_CATEGORIES, PEXELS_API_KEY
from utils.image_utils import get_cultural_images, verify_image_accessibility, get_istock_images

# Define hidden gems of India with structured information
HIDDEN_GEMS = [
    {
        "name": "Majuli Island",
        "location": "Assam",
        "description": "Location: Assam\nWorld's largest river island and a hub of Assamese culture and Vaishnavite monasteries.",
        "significance": "Significance: Home to unique mask-making traditions and traditional dance forms.",
        "travel_tips": "Travel Tips: Stay in local homestays and participate in traditional craft workshops.",
        "image_search": "majuli island assam river"
    },
    {
        "name": "Ziro Valley",
        "location": "Arunachal Pradesh",
        "description": "Location: Arunachal Pradesh\nTerraced rice fields and home to the Apatani tribe.",
        "significance": "Significance: Known for the Apatani people's distinctive facial tattoos and nose plugs tradition.",
        "travel_tips": "Travel Tips: Visit during the Ziro Music Festival in September for a cultural experience.",
        "image_search": "ziro valley arunachal pradesh"
    },
    {
        "name": "Champaner-Pavagadh",
        "location": "Gujarat",
        "description": "Location: Gujarat\nA UNESCO World Heritage site featuring a unique blend of Hindu and Islamic architecture.",
        "significance": "Significance: Ancient capital of Gujarat with well-preserved 16th-century architecture.",
        "travel_tips": "Travel Tips: Best visited during monsoon for lush greenery. Support local guides for authentic experiences.",
        "image_search": "champaner pavagadh gujarat"
    },
    {
        "name": "Gurez Valley",
        "location": "Jammu & Kashmir",
        "description": "Location: Jammu & Kashmir\nRemote Himalayan valley with Dard-Shin culture.",
        "significance": "Significance: One of the few places where the ancient Shina language is still spoken.",
        "travel_tips": "Travel Tips: Visit between June and September as the area remains cut off in winter.",
        "image_search": "gurez valley kashmir"
    },
    {
        "name": "Mawlynnong",
        "location": "Meghalaya",
        "description": "Location: Meghalaya\nKnown as 'Asia's Cleanest Village'.",
        "significance": "Significance: Famous for its community-based sanitation system and living root bridges.",
        "travel_tips": "Travel Tips: Visit the Sky View platform for panoramic views of the Bangladesh plains.",
        "image_search": "mawlynnong meghalaya clean village"
    },
    {
        "name": "Chettinad",
        "location": "Tamil Nadu",
        "description": "Location: Tamil Nadu\nMansions with unique architectural style.",
        "significance": "Significance: Preserves traditional Tamil merchant heritage and famous for its spicy cuisine.",
        "travel_tips": "Travel Tips: Take a guided mansion tour and try authentic Chettinad cuisine.",
        "image_search": "chettinad mansions tamil nadu"
    },
    {
        "name": "Orchha",
        "location": "Madhya Pradesh",
        "description": "Location: Madhya Pradesh\nMedieval city with exceptional Bundela architecture.",
        "significance": "Significance: Home to the unique Ram Raja Temple where Lord Rama is worshipped as a king.",
        "travel_tips": "Travel Tips: Attend the evening prayer ceremony at the Ram Raja Temple.",
        "image_search": "orchha madhya pradesh palace"
    },
    {
        "name": "Nubra Valley",
        "location": "Ladakh",
        "description": "Location: Ladakh\nHigh-altitude desert with double-humped Bactrian camels.",
        "significance": "Significance: Junction of the Shyok and Nubra rivers with a unique cold desert ecosystem.",
        "travel_tips": "Travel Tips: Visit Diskit Monastery and stay in traditional Ladakhi homestays.",
        "image_search": "nubra valley ladakh camel"
    },
    {
        "name": "Spiti Valley",
        "location": "Himachal Pradesh",
        "description": "Location: Himachal Pradesh\nTibetan Buddhist culture in a high desert mountain valley.",
        "significance": "Significance: Home to some of the oldest monasteries in the world, including Key and Tabo.",
        "travel_tips": "Travel Tips: Acclimatize properly to the high altitude and visit during summer months.",
        "image_search": "spiti valley key monastery"
    },
    {
        "name": "Unakoti",
        "location": "Tripura",
        "description": "Location: Tripura\nAncient rock-cut carvings and stone sculptures.",
        "significance": "Significance: Contains nearly one crore less one (99,99,999) rock carvings, hence the name.",
        "travel_tips": "Travel Tips: Combine with a visit to Tripura's bamboo handicraft villages.",
        "image_search": "unakoti rock carvings tripura"
    },
    {
        "name": "Gandikota",
        "location": "Andhra Pradesh",
        "description": "Location: Andhra Pradesh\nIndia's 'Grand Canyon' with a 12th-century fort.",
        "significance": "Significance: Spectacular gorge formed by the Pennar River cutting through Erramala hills.",
        "travel_tips": "Travel Tips: Camp overnight to witness the stunning sunrise and sunset over the canyon.",
        "image_search": "gandikota grand canyon india"
    },
    {
        "name": "Mechuka",
        "location": "Arunachal Pradesh",
        "description": "Location: Arunachal Pradesh\nRemote valley near the China border with Buddhist culture.",
        "significance": "Significance: Name means 'medicinal water of snow' due to its healing spring waters.",
        "travel_tips": "Travel Tips: Obtain Inner Line Permit before visiting and respect local tribal customs.",
        "image_search": "mechuka valley arunachal pradesh"
    },
    {
        "name": "Longwa Village",
        "location": "Nagaland",
        "description": "Location: Nagaland\nHome to Konyak tribe and headhunting traditions.",
        "significance": "Significance: The chief's house straddles the India-Myanmar border, with half in each country.",
        "travel_tips": "Travel Tips: Visit during the Aoling Festival in April to experience Konyak culture.",
        "image_search": "longwa village nagaland konyak"
    },
    {
        "name": "Kinnaur",
        "location": "Himachal Pradesh",
        "description": "Location: Himachal Pradesh\nApple orchards and ancient Buddhist temples.",
        "significance": "Significance: Known for unique polyandrous social customs and Kinnauri shawls.",
        "travel_tips": "Travel Tips: Try local apple products and visit during apple harvest season (Sept-Oct).",
        "image_search": "kinnaur himachal pradesh"
    },
    {
        "name": "Dhanushkodi",
        "location": "Tamil Nadu",
        "description": "Location: Tamil Nadu\nGhost town at the convergence of two seas.",
        "significance": "Significance: Mentioned in the Ramayana as the place where Lord Rama built a bridge to Lanka.",
        "travel_tips": "Travel Tips: Visit early morning or sunset for the best views where Bay of Bengal meets Indian Ocean.",
        "image_search": "dhanushkodi ghost town tamil nadu"
    },
    {
        "name": "Tawang",
        "location": "Arunachal Pradesh",
        "description": "Location: Arunachal Pradesh\nHome to one of the largest Buddhist monasteries.",
        "significance": "Significance: Birthplace of the 6th Dalai Lama and important center for Mahayana Buddhism.",
        "travel_tips": "Travel Tips: Visit during Tawang Festival (Oct-Nov) to experience local culture and traditions.",
        "image_search": "tawang monastery arunachal pradesh"
    },
    {
        "name": "Mandu",
        "location": "Madhya Pradesh", 
        "description": "Location: Madhya Pradesh\nAncient city of ruins with Afghan architecture.",
        "significance": "Significance: Known as the 'City of Joy' and home to the ship palace (Jahaz Mahal).",
        "travel_tips": "Travel Tips: Visit during monsoon when the monuments appear to float on surrounding ponds.",
        "image_search": "mandu madhya pradesh jahaz mahal"
    },
    {
        "name": "Wayanad",
        "location": "Kerala",
        "description": "Location: Kerala\nSpice plantations and ancient cave paintings.",
        "significance": "Significance: The Edakkal Caves contain petroglyphs dating back to 6000 BCE.",
        "travel_tips": "Travel Tips: Take a guided spice plantation tour and trek to the Edakkal Caves.",
        "image_search": "wayanad kerala edakkal caves"
    },
    {
        "name": "Hemis",
        "location": "Ladakh",
        "description": "Location: Ladakh\nHome to the largest Buddhist monastery in Ladakh.",
        "significance": "Significance: Famous for the annual Hemis Festival celebrating Guru Padmasambhava.",
        "travel_tips": "Travel Tips: Visit during the Hemis Festival in June/July to see the colorful masked dances.",
        "image_search": "hemis monastery ladakh festival"
    }
]

def get_image_for_hidden_gem(gem):
    """Get an image for a hidden gem using existing image utility functions."""
    try:
        # Try to get images from iStock first (more relevant for hidden places)
        images = get_istock_images(gem["image_search"])
        
        # If no images from iStock, try Pexels API with error handling
        if not images or len(images) == 0:
            try:
                images = get_cultural_images(gem["image_search"], count=1)
            except Exception as e:
                if "429" in str(e):  # Rate limit error
                    st.warning("Image loading temporarily limited. Please try again in a few minutes.")
                return {
                    'url': "https://media.istockphoto.com/id/1147544807/vector/thumbnail-image-vector-graphic.jpg?s=612x612&w=0&k=20&c=rnCKVbdxqkjlcs3xH87-9gocETqpspHFXu5dIGB4wuM=",
                    'photographer': "Unknown",
                    'photographer_url': "#",
                    'source': "Placeholder"
                }
        
        # Return the first image URL if available, or a placeholder
        if images and len(images) > 0 and 'url' in images[0]:
            return images[0]
        
        return {
            'url': "https://media.istockphoto.com/id/1147544807/vector/thumbnail-image-vector-graphic.jpg?s=612x612&w=0&k=20&c=rnCKVbdxqkjlcs3xH87-9gocETqpspHFXu5dIGB4wuM=",
            'photographer': "Unknown",
            'photographer_url': "#",
            'source': "Placeholder"
        }
    except Exception as e:
        st.error(f"Error loading image: {str(e)}")
        return {
            'url': "https://media.istockphoto.com/id/1147544807/vector/thumbnail-image-vector-graphic.jpg?s=612x612&w=0&k=20&c=rnCKVbdxqkjlcs3xH87-9gocETqpspHFXu5dIGB4wuM=",
            'photographer': "Unknown",
            'photographer_url': "#",
            'source': "Placeholder"
        }

def display_cultural_gallery(category, subcategory=None):
    """Display a gallery of cultural images with proper attribution."""
    st.markdown(f"### 🖼️ {category.title()} Gallery")
    
    # Get images
    images = get_cultural_images(category, subcategory)
    
    if not images:
        st.warning(f"No images found for {category}. Please try another category.")
        return
    
    # Create a grid of images with captions and attribution - improved layout
    cols = st.columns(3)
    for idx, img_data in enumerate(images):
        with cols[idx % 3]:
            try:
                # Verify image URL is accessible
                if verify_image_accessibility(img_data['url']):
                    # Use a consistent description if none is provided
                    image_description = img_data['description'] or f'Traditional Indian {category}'
                    
                    # Check if the description contains irrelevant content
                    irrelevant_keywords = ['headphone', 'audio device', 'earphone', 'speaker', 'electronic']
                    if any(keyword in image_description.lower() for keyword in irrelevant_keywords):
                        image_description = f'Traditional Indian {category}'
                    
                    # Create an improved card with better styling
                    st.markdown("""
                    <div class='art-card' style='margin-bottom: 20px; background: linear-gradient(135deg, rgba(0,0,0,0.2), rgba(50,50,50,0.4)); 
                                border-radius: 12px; overflow: hidden; box-shadow: 0 4px 8px rgba(0,0,0,0.3);'>
                    """, unsafe_allow_html=True)
                    
                    # Display image with proper aspect ratio
                    st.image(img_data['url'], use_container_width=True)
                    
                    # Improved content section with better typography
                    st.markdown(f"""
                    <div class='card-content' style='padding: 12px 15px;'>
                        <div class='card-description' style='font-size: 1rem; line-height: 1.4; margin-bottom: 10px; 
                                    color: rgba(255,255,255,0.9); font-weight: 500;'>{image_description}</div>
                        <div class='card-details' style='font-size: 0.8rem; color: rgba(255,255,255,0.7);'>
                            Photo by <a href='{img_data['photographer_url']}' target='_blank' 
                            style='color: #FF9933; text-decoration: none;'>{img_data['photographer']}</a> 
                            on {img_data.get('source', 'Pexels')}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.markdown("</div>", unsafe_allow_html=True)
                else:
                    # Skip displaying this image but don't show an error
                    continue
            except Exception as e:
                # Skip displaying this image but don't show an error
                continue
    
    # Add spacing after gallery
    st.markdown("<div style='margin-bottom: 30px;'></div>", unsafe_allow_html=True)

def display_hidden_gems():
    """Display a curated list of hidden gems of India with images and facts."""
    st.markdown("<h2 class='sub-header'>💎 Hidden Gems of India</h2>", unsafe_allow_html=True)
    
    # Add intro text with better styling
    st.markdown("""
    <div style='margin-bottom: 20px; background: linear-gradient(135deg, rgba(255,153,51,0.3), rgba(18,136,7,0.3)); 
            border-radius: 15px; padding: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);'>
        <p style='font-size: 1.1rem; line-height: 1.7; text-shadow: 0 1px 2px rgba(0,0,0,0.1);'>
            Beyond the famous tourist destinations, India is home to countless hidden treasures that offer 
            authentic cultural experiences. Explore these lesser-known places that showcase India's incredible diversity.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Display hidden gems in a masonry-style layout (3 columns)
    cols = st.columns(3)
    
    for idx, gem in enumerate(HIDDEN_GEMS):
        with cols[idx % 3]:
            # Get image
            img_data = get_image_for_hidden_gem(gem)
            
            # Display location badge
            st.markdown(f"""
            <div style='position: relative; z-index: 10;'>
                <div style='position: absolute; top: 10px; left: 10px; background: linear-gradient(135deg, #FF9933, #FF7633); 
                        color: white; padding: 6px 12px; border-radius: 5px; font-size: 0.8rem; font-weight: bold;
                        box-shadow: 0 2px 5px rgba(0,0,0,0.2); text-transform: uppercase; letter-spacing: 0.5px;'>
                    {gem["location"]}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Display the image - using Streamlit's component directly reduces HTML complexity
            try:
                if verify_image_accessibility(img_data['url']):
                    st.image(img_data['url'], use_container_width=True)
                else:
                    # Use placeholder image
                    st.image("https://media.istockphoto.com/id/1147544807/vector/thumbnail-image-vector-graphic.jpg?s=612x612&w=0&k=20&c=rnCKVbdxqkjlcs3xH87-9gocETqpspHFXu5dIGB4wuM=", use_container_width=True)
            except:
                # Use placeholder image on error
                st.image("https://media.istockphoto.com/id/1147544807/vector/thumbnail-image-vector-graphic.jpg?s=612x612&w=0&k=20&c=rnCKVbdxqkjlcs3xH87-9gocETqpspHFXu5dIGB4wuM=", use_container_width=True)
            
            # Card background wrapper
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, rgba(0,0,0,0.2), rgba(50,50,50,0.4)); 
                    border-radius: 15px; overflow: hidden; box-shadow: 0 6px 15px rgba(0,0,0,0.4); 
                    padding: 20px; margin-top: -40px; position: relative;'>
            """, unsafe_allow_html=True)
            
            # Title section - separate simple HTML
            st.markdown(f"""
            <h3 style='margin: 0 0 15px 0; background: linear-gradient(90deg, #FF9933, #e67300); 
                      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                      font-size: 1.5rem; font-weight: 700; letter-spacing: 0.5px;'>{gem["name"]}</h3>
            """, unsafe_allow_html=True)
            
            # Description section - separate HTML            
            # Replace newlines with <br> before the f-string to avoid backslash issues            
            formatted_description = gem["description"].replace("\n", "<br>")            
            st.markdown(f"""            
            <div style='background: linear-gradient(135deg, rgba(0,0,0,0.2), rgba(50,50,50,0.1));                      
                     border-radius: 10px; padding: 15px; margin-bottom: 18px;'>                
                <p style='color: rgba(255,255,255,0.95); margin-bottom: 0; font-size: 0.95rem;                         
                        line-height: 1.6; text-shadow: 0 1px 2px rgba(0,0,0,0.2);'>{formatted_description}</p>            
            </div>            
            """, unsafe_allow_html=True)
            
            # Significance section - separate HTML
            st.markdown(f"""
            <div style='margin-bottom: 15px;'>
                <div style='display: flex; align-items: flex-start;'>
                    <div style='background: linear-gradient(135deg, #FF9933, #e67300); border-radius: 50%; width: 24px; 
                            height: 24px; display: flex; align-items: center; justify-content: center; margin-right: 10px; 
                            flex-shrink: 0; margin-top: 2px;'>
                        <span style='color: white; font-weight: bold; font-size: 0.8rem;'>S</span>
                    </div>
                    <p style='font-size: 0.95rem; margin: 0; color: rgba(255,255,255,0.95);
                            line-height: 1.5; text-shadow: 0 1px 1px rgba(0,0,0,0.1);'>{gem["significance"]}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Travel Tips section - separate HTML
            st.markdown(f"""
            <div style='margin-bottom: 5px;'>
                <div style='display: flex; align-items: flex-start;'>
                    <div style='background: linear-gradient(135deg, #128807, #0d6b05); border-radius: 50%; width: 24px; 
                            height: 24px; display: flex; align-items: center; justify-content: center; margin-right: 10px;
                            flex-shrink: 0; margin-top: 2px;'>
                        <span style='color: white; font-weight: bold; font-size: 0.8rem;'>T</span>
                    </div>
                    <p style='font-size: 0.95rem; margin: 0; color: rgba(255,255,255,0.95);
                            line-height: 1.5; text-shadow: 0 1px 1px rgba(0,0,0,0.1);'>{gem["travel_tips"]}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Close the card wrapper
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Add spacing between cards
            st.markdown("<div style='margin-bottom: 25px;'></div>", unsafe_allow_html=True)

def show_cultural_gallery():
    """Show a gallery of cultural images organized by categories."""
    st.markdown("<h1 class='main-header'>Desi Gallery</h1>", unsafe_allow_html=True)
    
    # Create tabs for different sections
    tabs = st.tabs(["Hidden Gems", "Endangered Heritage", "State Specials", "Explore by Category"])
    
    with tabs[0]:
        # Display hidden gems
        display_hidden_gems()
    
    with tabs[1]:
        # Endangered Heritage Section
        st.markdown("<h2 class='sub-header'>⚠️ Endangered Heritage</h2>", unsafe_allow_html=True)
        
        # Add intro text
        st.markdown("""
        <div style='margin-bottom: 20px; background: linear-gradient(135deg, rgba(255,82,82,0.3), rgba(255,153,51,0.3)); 
                border-radius: 15px; padding: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);'>
            <p style='font-size: 1.1rem; line-height: 1.7; text-shadow: 0 1px 2px rgba(0,0,0,0.1);'>
                These art forms and cultural practices are at risk of disappearing. Learn about them and support their preservation.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Create two columns for endangered art forms and spots
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h3>🎨 Endangered Art Forms</h3>", unsafe_allow_html=True)
            
            endangered_art_forms = [
                {
                    "name": "Chitrakathi",
                    "region": "Maharashtra",
                    "status": "Critically Endangered",
                    "description": "A 400-year-old storytelling art form using painted scrolls. Only 3-4 practitioners remain.",
                    "image_search": "chitrakathi painting maharashtra"
                },
                {
                    "name": "Manjusha Art",
                    "region": "Bihar",
                    "status": "Endangered",
                    "description": "Ancient scroll painting art form depicting stories of Bihula-Bishari. Less than 20 artists practice it.",
                    "image_search": "manjusha art bihar"
                },
                {
                    "name": "Kalamkari",
                    "region": "Andhra Pradesh",
                    "status": "Vulnerable",
                    "description": "Traditional hand-painted textile art. Natural dye techniques are being lost.",
                    "image_search": "kalamkari painting andhra"
                },
                {
                    "name": "Pattachitra",
                    "region": "Odisha",
                    "status": "Endangered",
                    "description": "Cloth-based scroll painting tradition. Original techniques are being replaced by modern methods.",
                    "image_search": "pattachitra odisha"
                }
            ]
            
            for art_form in endangered_art_forms:
                st.markdown(f"""
                <div style='background: linear-gradient(135deg, rgba(0,0,0,0.2), rgba(50,50,50,0.4)); 
                        border-radius: 15px; padding: 20px; margin-bottom: 20px;'>
                    <h4 style='color: #FF5252; margin-bottom: 10px;'>{art_form['name']}</h4>
                    <p style='color: #FF9933; font-size: 0.9rem; margin-bottom: 10px;'>{art_form['region']} • {art_form['status']}</p>
                    <p style='color: rgba(255,255,255,0.9);'>{art_form['description']}</p>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("<h3>🏛️ Endangered Heritage Sites</h3>", unsafe_allow_html=True)
            
            endangered_sites = [
                {
                    "name": "Hampi's Ancient Water Systems",
                    "region": "Karnataka",
                    "status": "Critical",
                    "description": "Ancient water management systems dating back to the Vijayanagara Empire. Many structures are deteriorating.",
                    "image_search": "hampi water systems karnataka"
                },
                {
                    "name": "Champaner-Pavagadh",
                    "region": "Gujarat",
                    "status": "Endangered",
                    "description": "UNESCO World Heritage site with unique blend of Hindu and Islamic architecture. Needs urgent conservation.",
                    "image_search": "champaner pavagadh gujarat"
                },
                {
                    "name": "Ancient Caves of Ajanta",
                    "region": "Maharashtra",
                    "status": "Vulnerable",
                    "description": "2nd-century BCE Buddhist cave paintings. Environmental factors threaten preservation.",
                    "image_search": "ajanta caves maharashtra"
                },
                {
                    "name": "Traditional Stepwells",
                    "region": "Multiple States",
                    "status": "Endangered",
                    "description": "Ancient water conservation structures. Many are abandoned and deteriorating.",
                    "image_search": "stepwells india architecture"
                }
            ]
            
            for site in endangered_sites:
                st.markdown(f"""
                <div style='background: linear-gradient(135deg, rgba(0,0,0,0.2), rgba(50,50,50,0.4)); 
                        border-radius: 15px; padding: 20px; margin-bottom: 20px;'>
                    <h4 style='color: #FF5252; margin-bottom: 10px;'>{site['name']}</h4>
                    <p style='color: #FF9933; font-size: 0.9rem; margin-bottom: 10px;'>{site['region']} • {site['status']}</p>
                    <p style='color: rgba(255,255,255,0.9);'>{site['description']}</p>
                </div>
                """, unsafe_allow_html=True)
        
        # Add call to action
        st.markdown("""
        <div style='margin-top: 30px; background: linear-gradient(135deg, rgba(18,136,7,0.3), rgba(255,153,51,0.3)); 
                border-radius: 15px; padding: 20px; text-align: center;'>
            <h3 style='color: #128807; margin-bottom: 15px;'>How You Can Help</h3>
            <p style='color: rgba(255,255,255,0.9); margin-bottom: 10px;'>
                Support these endangered art forms and heritage sites by:
            </p>
            <ul style='color: rgba(255,255,255,0.9); text-align: left; display: inline-block;'>
                <li>Visiting and learning about these art forms and sites</li>
                <li>Supporting local artisans and conservation efforts</li>
                <li>Sharing knowledge about these cultural treasures</li>
                <li>Contributing to preservation initiatives</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tabs[2]:
        # State Specials Section
        st.markdown("<h2 class='sub-header'>🎭 State Specials</h2>", unsafe_allow_html=True)
        
        # Add intro text
        st.markdown("""
        <div style='margin-bottom: 20px; background: linear-gradient(135deg, rgba(78,205,196,0.3), rgba(255,107,107,0.3)); 
                border-radius: 15px; padding: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);'>
            <p style='font-size: 1.1rem; line-height: 1.7; text-shadow: 0 1px 2px rgba(0,0,0,0.1);'>
                Discover unique art forms, crafts, and cultural elements from each state of India. Each state has its own 
                distinct cultural identity and artistic traditions that make it special.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # State-wise specials data
        state_specials = {
            "Andhra Pradesh": {
                "art_forms": ["Kalamkari", "Tirupati Laddu Making", "Kondapalli Toys"],
                "crafts": ["Uppada Silk", "Mangalagiri Cotton", "Etikoppaka Wooden Toys"],
                "cultural_elements": ["Kuchipudi Dance", "Harikatha", "Burrakatha"]
            },
            "Arunachal Pradesh": {
                "art_forms": ["Apatani Tattooing", "Monpa Paper Making", "Wancho Wood Carving"],
                "crafts": ["Bamboo Craft", "Cane Work", "Traditional Textiles"],
                "cultural_elements": ["Losar Festival", "Aji Lamu Dance", "Ponung Dance"]
            },
            "Assam": {
                "art_forms": ["Mask Making", "Terracotta", "Cane and Bamboo"],
                "crafts": ["Muga Silk", "Japi Making", "Brass Metal Work"],
                "cultural_elements": ["Bihu Dance", "Sattriya", "Ankia Naat"]
            },
            "Bihar": {
                "art_forms": ["Madhubani Painting", "Manjusha Art", "Sujni Embroidery"],
                "crafts": ["Tikuli Art", "Bamboo Craft", "Stone Carving"],
                "cultural_elements": ["Chhau Dance", "Jat-Jatin Dance", "Bidesia"]
            },
            "Chhattisgarh": {
                "art_forms": ["Tattooing", "Wood Carving", "Clay Work"],
                "crafts": ["Bastar Dhokra", "Tattooing", "Bamboo Craft"],
                "cultural_elements": ["Pandwani", "Raut Nacha", "Karma Dance"]
            },
            "Goa": {
                "art_forms": ["Azulejos", "Wood Inlay", "Shell Craft"],
                "crafts": ["Crochet", "Bamboo Craft", "Pottery"],
                "cultural_elements": ["Dekhni", "Fugdi", "Goff"]
            },
            "Gujarat": {
                "art_forms": ["Pithora Painting", "Rogan Art", "Ahmedabad Wood Carving"],
                "crafts": ["Patola Silk", "Bandhani", "Kutch Embroidery"],
                "cultural_elements": ["Garba", "Dandiya Raas", "Bhavai"]
            },
            "Haryana": {
                "art_forms": ["Phulkari", "Mud Work", "Wood Carving"],
                "crafts": ["Durries", "Pottery", "Basket Weaving"],
                "cultural_elements": ["Saang", "Ras Leela", "Dhamal Dance"]
            },
            "Himachal Pradesh": {
                "art_forms": ["Kangra Painting", "Chamba Rumal", "Wood Carving"],
                "crafts": ["Kullu Shawls", "Metal Work", "Stone Carving"],
                "cultural_elements": ["Nati Dance", "Chham Dance", "Losar Festival"]
            },
            "Jharkhand": {
                "art_forms": ["Sohrai Painting", "Paitkar Painting", "Tattoo Art"],
                "crafts": ["Bamboo Craft", "Stone Carving", "Wood Work"],
                "cultural_elements": ["Chhau Dance", "Jhumair", "Domkach"]
            },
            "Karnataka": {
                "art_forms": ["Mysore Painting", "Chitrakala", "Wood Inlay"],
                "crafts": ["Ilkal Sarees", "Bidriware", "Sandalwood Carving"],
                "cultural_elements": ["Yakshagana", "Dollu Kunitha", "Veeragase"]
            },
            "Kerala": {
                "art_forms": ["Mural Painting", "Theyyam", "Kathakali Makeup"],
                "crafts": ["Coir Products", "Wood Carving", "Metal Work"],
                "cultural_elements": ["Kathakali", "Mohiniyattam", "Thiruvathira"]
            },
            "Madhya Pradesh": {
                "art_forms": ["Gond Art", "Pithora", "Mandana"],
                "crafts": ["Chanderi Sarees", "Maheshwari Sarees", "Bagh Print"],
                "cultural_elements": ["Bhagoria", "Tertali", "Lehangi"]
            },
            "Maharashtra": {
                "art_forms": ["Warli Painting", "Chitrakathi", "Paithani Weaving"],
                "crafts": ["Bidriware", "Kolhapuri Chappals", "Narayan Peth Sarees"],
                "cultural_elements": ["Lavani", "Tamasha", "Dindi"]
            },
            "Manipur": {
                "art_forms": ["Lai Haraoba", "Pottery", "Bamboo Craft"],
                "crafts": ["Manipuri Shawls", "Cane Work", "Wood Carving"],
                "cultural_elements": ["Manipuri Dance", "Thang Ta", "Pung Cholom"]
            },
            "Meghalaya": {
                "art_forms": ["Bamboo Craft", "Cane Work", "Wood Carving"],
                "crafts": ["Eri Silk", "Bamboo Products", "Cane Furniture"],
                "cultural_elements": ["Nongkrem Dance", "Shad Suk Mynsiem", "Wangala"]
            },
            "Mizoram": {
                "art_forms": ["Bamboo Craft", "Cane Work", "Weaving"],
                "crafts": ["Puan", "Bamboo Products", "Cane Furniture"],
                "cultural_elements": ["Cheraw Dance", "Khuallam", "Chheihlam"]
            },
            "Nagaland": {
                "art_forms": ["Wood Carving", "Bamboo Craft", "Weaving"],
                "crafts": ["Naga Shawls", "Bamboo Products", "Cane Work"],
                "cultural_elements": ["Hornbill Festival", "War Dance", "Zeliang"]
            },
            "Odisha": {
                "art_forms": ["Pattachitra", "Saura Painting", "Tala Chitra"],
                "crafts": ["Ikat", "Silver Filigree", "Stone Carving"],
                "cultural_elements": ["Odissi", "Chhau", "Gotipua"]
            },
            "Punjab": {
                "art_forms": ["Phulkari", "Mud Work", "Wood Carving"],
                "crafts": ["Durries", "Pottery", "Basket Weaving"],
                "cultural_elements": ["Bhangra", "Giddha", "Jhumar"]
            },
            "Rajasthan": {
                "art_forms": ["Miniature Painting", "Blue Pottery", "Phad Painting"],
                "crafts": ["Bandhani", "Block Printing", "Metal Work"],
                "cultural_elements": ["Ghoomar", "Kalbelia", "Bhavai"]
            },
            "Sikkim": {
                "art_forms": ["Thangka Painting", "Wood Carving", "Carpet Weaving"],
                "crafts": ["Bamboo Craft", "Cane Work", "Traditional Textiles"],
                "cultural_elements": ["Cham Dance", "Maruni", "Tamang Selo"]
            },
            "Tamil Nadu": {
                "art_forms": ["Tanjore Painting", "Kolam", "Temple Art"],
                "crafts": ["Kanjivaram Sarees", "Temple Jewelry", "Wood Carving"],
                "cultural_elements": ["Bharatanatyam", "Therukoothu", "Karagattam"]
            },
            "Telangana": {
                "art_forms": ["Nirmal Painting", "Cheriyal Scrolls", "Bidriware"],
                "crafts": ["Pochampally Ikat", "Silver Filigree", "Lacquer Work"],
                "cultural_elements": ["Perini", "Dappu", "Gusadi"]
            },
            "Tripura": {
                "art_forms": ["Bamboo Craft", "Cane Work", "Weaving"],
                "crafts": ["Riha", "Bamboo Products", "Cane Furniture"],
                "cultural_elements": ["Hojagiri", "Garia", "Lebang Boomani"]
            },
            "Uttar Pradesh": {
                "art_forms": ["Chikankari", "Zardozi", "Wood Inlay"],
                "crafts": ["Brass Work", "Glass Work", "Carpet Weaving"],
                "cultural_elements": ["Kathak", "Ramlila", "Nautanki"]
            },
            "Uttarakhand": {
                "art_forms": ["Aipan", "Wood Carving", "Stone Carving"],
                "crafts": ["Ringal Craft", "Woolen Textiles", "Copper Work"],
                "cultural_elements": ["Jagar", "Chholiya", "Barada Nati"]
            },
            "West Bengal": {
                "art_forms": ["Kalighat Painting", "Patachitra", "Terracotta"],
                "crafts": ["Baluchari Sarees", "Dokra", "Conch Shell Craft"],
                "cultural_elements": ["Chhau", "Gambhira", "Baul"]
            }
        }
        
        # Create a search box for states
        search_state = st.text_input("🔍 Search for a state", "")
        
        # Filter states based on search
        filtered_states = [state for state in state_specials.keys() 
                         if search_state.lower() in state.lower()]
        
        # Display state information in a grid
        cols = st.columns(3)
        for idx, state in enumerate(filtered_states):
            with cols[idx % 3]:
                # Create a container for the state card with enhanced gradient
                st.markdown(f"""
                <style>
                .card {{
                    background: linear-gradient(135deg, rgba(78,205,196,0.3), rgba(255,107,107,0.3));
                    border-radius: 10px;
                    padding: 15px;
                    margin: 15px 0;
                }}
                .title {{
                    color: #FFFFFF;
                    font-size: 26px;
                    font-weight: 900;
                    text-align: center;
                    margin-bottom: 15px;
                    text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
                }}
                .section {{
                    background: rgba(255,255,255,0.15);
                    border-radius: 8px;
                    padding: 12px;
                    margin: 8px 0;
                }}
                .section-title {{
                    color: #F8F9FA;
                    font-size: 18px;
                    font-weight: 800;
                    margin-bottom: 8px;
                    text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
                }}
                .item {{
                    color: #E9ECEF;
                    font-size: 15px;
                    font-weight: 600;
                    margin: 4px 0;
                    padding: 8px 12px;
                    border-left: 3px solid rgba(255,255,255,0.3);
                    transition: all 0.3s ease;
                }}
                .item:hover {{
                    background: rgba(255,255,255,0.1);
                    border-left: 3px solid #FFFFFF;
                    transform: translateX(5px);
                }}
                </style>
                """, unsafe_allow_html=True)

                # Create the state card content
                html = f"""
                <div class="card">
                    <div class="title">{state}</div>
                    <div class="section">
                        <div class="section-title">🎨 Art Forms</div>
                        {"".join(f'<div class="item">{art}</div>' for art in state_specials[state]["art_forms"])}
                    </div>
                    <div class="section">
                        <div class="section-title">🛠️ Crafts</div>
                        {"".join(f'<div class="item">{craft}</div>' for craft in state_specials[state]["crafts"])}
                    </div>
                    <div class="section">
                        <div class="section-title">🎭 Cultural Elements</div>
                        {"".join(f'<div class="item">{element}</div>' for element in state_specials[state]["cultural_elements"])}
                    </div>
                </div>
                """
                
                # Display the card
                st.markdown(html, unsafe_allow_html=True)
    
    with tabs[3]:
        # Category selection
        selected_category = st.selectbox(
            "Select Category",
            list(CULTURAL_CATEGORIES.keys())
        )
        
        # Subcategory selection if available
        if selected_category in CULTURAL_CATEGORIES:
            selected_subcategory = st.selectbox(
                "Select Specific Item",
                ["All"] + CULTURAL_CATEGORIES[selected_category]
            )
        else:
            selected_subcategory = "All"
        
        # Display gallery
        if selected_subcategory == "All":
            display_cultural_gallery(selected_category)
        else:
            display_cultural_gallery(selected_category, selected_subcategory) 