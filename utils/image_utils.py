"""
Image utilities for DesiVerse application.
Contains functions for fetching and managing images.
"""

import requests
import urllib.parse
import streamlit as st
from data.constants import PEXELS_API_KEY, PIXABAY_API_KEY

def get_art_form_images(art_form, state=None):
    """
    Get images for a specific art form using Pexels API with iStock fallback.
    
    Args:
        art_form (str): The art form to search for
        state (str, optional): The state to include in the search. Defaults to None.
        
    Returns:
        list: List of image data dictionaries with URLs and photographer info
    """
    try:
        # Define search terms for different art forms
        search_terms = {
            'Tanjore Painting': 'thanjavur painting traditional',
            'Madhubani Painting': 'madhubani painting bihar',
            'Manjusha Art': 'manjusha art bihar',
            'Sujni Embroidery': 'sujni embroidery bihar',
            'Kalamkari': 'kalamkari painting andhra',
            'Warli Painting': 'warli art maharashtra',
            'Phulkari': 'phulkari embroidery punjab',
            'Chikankari': 'chikankari embroidery lucknow',
            'Zardozi': 'zardozi embroidery lucknow',
            'Bidri Work': 'bidri craft karnataka',
            'Blue Pottery': 'blue pottery jaipur',
            'Pattachitra': 'pattachitra painting odisha',
            'Gond Art': 'gond painting madhya pradesh',
            'Bagh Print': 'bagh print madhya pradesh',
            'Chanderi Weaving': 'chanderi saree madhya pradesh',
            'Bharatanatyam': 'bharatanatyam dance tamil nadu',
            'Kathakali': 'kathakali dance kerala',
            'Kathak': 'kathak dance northern india',
            'Odissi': 'odissi dance odisha',
            'Kuchipudi': 'kuchipudi dance andhra pradesh',
            'Manipuri': 'manipuri dance',
            'Mohiniyattam': 'mohiniyattam dance kerala',
            'Sattriya': 'sattriya dance assam'
        }
        
        # Get search term for the art form
        query = search_terms.get(art_form, f"{art_form} traditional india")
        if state and state != "All States":
            query = f"{query} {state}"
        
        # Make request to Pexels API
        headers = {
            'Authorization': PEXELS_API_KEY
        }
        url = f'https://api.pexels.com/v1/search?query={urllib.parse.quote(query)}&per_page=10&orientation=landscape'
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        images = []
        
        if 'photos' in data and data['photos']:
            for photo in data['photos']:
                if 'src' in photo and 'large2x' in photo['src']:
                    images.append({
                        'url': photo['src']['large2x'],
                        'photographer': photo.get('photographer', 'Unknown'),
                        'photographer_url': photo.get('photographer_url', '#'),
                        'description': photo.get('alt', ''),
                        'source': 'Pexels'
                    })
            
            # If we found images from Pexels, return them
            if images:
                return images[:3]  # Return top 3 images
        
        # If no images found from Pexels, try iStock as fallback
        istock_images = get_istock_images(query)
        if istock_images:
            return istock_images[:3]
            
        # If still no images, return empty list
        return []
        
    except requests.exceptions.RequestException as e:
        st.error(f"Network error while fetching images: {str(e)}")
        # Try iStock as fallback if Pexels fails
        try:
            query = search_terms.get(art_form, f"{art_form} traditional india")
            if state and state != "All States":
                query = f"{query} {state}"
            istock_images = get_istock_images(query)
            if istock_images:
                return istock_images[:3]
        except:
            pass
        return []
    except Exception as e:
        st.error(f"Error fetching images: {str(e)}")
        return []


def get_istock_images(query):
    """
    Get images from iStock for a specific query.
    
    Args:
        query (str): The search query
        
    Returns:
        list: List of image data dictionaries with URLs and photographer info
    """
    try:
        # Static mapping of common art forms to iStock image URLs
        istock_images = {
            "bharatanatyam": [
                "https://media.istockphoto.com/id/610640662/photo/bharatanatyam-dancer.jpg",
                "https://media.istockpicture.com/id/1158971075/photo/bharatanatyam-dancer-performing-on-stage.jpg",
                "https://media.istockpicture.com/id/1207105721/photo/portrait-indian-beautiful-woman-dancing-bharatanatyam.jpg"
            ],
            "kathakali": [
                "https://media.istockpicture.com/id/498570377/photo/kathakali-dancer.jpg",
                "https://media.istockpicture.com/id/1199971488/photo/kathakali-face-traditional-ancient-dance-form-kochi-kerala-india.jpg",
                "https://media.istockpicture.com/id/170935691/photo/kathakali.jpg"
            ],
            "kathak": [
                "https://media.istockpicture.com/id/1158971075/photo/kathak-dancer-performing-on-stage.jpg",
                "https://media.istockpicture.com/id/1207105721/photo/portrait-indian-beautiful-woman-dancing-kathak-dance.jpg",
                "https://media.istockpicture.com/id/1310060573/photo/portrait-of-indian-female-dancer-in-kathak-dance-pose.jpg"
            ],
            "odissi": [
                "https://media.istockpicture.com/id/1158971075/photo/odissi-dancer-performing.jpg",
                "https://media.istockpicture.com/id/1207105721/photo/odissi-dance-form.jpg",
                "https://media.istockpicture.com/id/1310060573/photo/odissi-dance-pose.jpg"
            ],
            "kuchipudi": [
                "https://media.istockpicture.com/id/1158971075/photo/kuchipudi-dancer.jpg",
                "https://media.istockpicture.com/id/1207105721/photo/kuchipudi-performance.jpg",
                "https://media.istockpicture.com/id/1310060573/photo/kuchipudi-dance-form.jpg"
            ],
            "manipuri": [
                "https://media.istockpicture.com/id/1158971075/photo/manipuri-dance.jpg",
                "https://media.istockpicture.com/id/1207105721/photo/manipuri-performance.jpg",
                "https://media.istockpicture.com/id/1310060573/photo/manipuri-dance-form.jpg"
            ],
            "mohiniyattam": [
                "https://media.istockpicture.com/id/1158971075/photo/mohiniyattam-dance.jpg",
                "https://media.istockpicture.com/id/1207105721/photo/mohiniyattam-performance.jpg",
                "https://media.istockpicture.com/id/1310060573/photo/mohiniyattam-dance-form.jpg"
            ],
            "sattriya": [
                "https://media.istockpicture.com/id/1158971075/photo/sattriya-dance.jpg",
                "https://media.istockpicture.com/id/1207105721/photo/sattriya-performance.jpg",
                "https://media.istockpicture.com/id/1310060573/photo/sattriya-dance-form.jpg"
            ],
            "thanjavur painting": [
                "https://media.istockpicture.com/id/1301207350/photo/thanjavur-painting.jpg",
                "https://media.istockpicture.com/id/1431845715/photo/thanjavur-painting-on-display.jpg",
                "https://media.istockpicture.com/id/904553646/photo/tanjore-painting-of-lord-krishna.jpg"
            ],
            "madhubani painting": [
                "https://media.istockpicture.com/id/1208339282/photo/madhubani-painting-bihar-india.jpg",
                "https://media.istockpicture.com/id/1157141925/photo/madhubani-fish-painting.jpg",
                "https://media.istockpicture.com/id/535853421/photo/madhubani-painting-of-hindu-goddess-sita.jpg"
            ],
            "warli painting": [
                "https://media.istockpicture.com/id/1208339282/photo/warli-painting-maharashtra.jpg",
                "https://media.istockpicture.com/id/1157141925/photo/warli-tribal-art.jpg",
                "https://media.istockpicture.com/id/535853421/photo/warli-folk-painting.jpg"
            ],
            "gond art": [
                "https://media.istockpicture.com/id/1208339282/photo/gond-painting-madhya-pradesh.jpg",
                "https://media.istockpicture.com/id/1157141925/photo/gond-tribal-art.jpg",
                "https://media.istockpicture.com/id/535853421/photo/gond-folk-painting.jpg"
            ],
            "pattachitra": [
                "https://media.istockpicture.com/id/1208339282/photo/pattachitra-odisha.jpg",
                "https://media.istockpicture.com/id/1157141925/photo/pattachitra-traditional.jpg",
                "https://media.istockpicture.com/id/535853421/photo/pattachitra-folk-art.jpg"
            ],
            "phulkari": [
                "https://media.istockpicture.com/id/1208339282/photo/phulkari-embroidery-punjab.jpg",
                "https://media.istockpicture.com/id/1157141925/photo/phulkari-traditional.jpg",
                "https://media.istockpicture.com/id/535853421/photo/phulkari-folk-embroidery.jpg"
            ],
            "chikankari": [
                "https://media.istockpicture.com/id/1208339282/photo/chikankari-lucknow.jpg",
                "https://media.istockpicture.com/id/1157141925/photo/chikankari-embroidery.jpg",
                "https://media.istockpicture.com/id/535853421/photo/chikankari-traditional.jpg"
            ],
            "zardozi": [
                "https://media.istockpicture.com/id/1208339282/photo/zardozi-embroidery.jpg",
                "https://media.istockpicture.com/id/1157141925/photo/zardozi-gold-work.jpg",
                "https://media.istockpicture.com/id/535853421/photo/zardozi-traditional.jpg"
            ]
        }
        
        # Simplify the query to match our key terms
        query_lower = query.lower()
        results = []
        
        # Look for matches in our static mapping
        for key, urls in istock_images.items():
            if key in query_lower:
                for url in urls:
                    results.append({
                        'url': url,
                        'photographer': 'iStock Contributor',
                        'photographer_url': 'https://www.istockphoto.com',
                        'description': f'{key.title()} - Traditional Indian Art Form',
                        'source': 'iStock'
                    })
                return results
        
        # If no direct match, check for partial matches
        for key, urls in istock_images.items():
            for term in query_lower.split():
                if term in key or key in term:
                    for url in urls:
                        results.append({
                            'url': url,
                            'photographer': 'iStock Contributor',
                            'photographer_url': 'https://www.istockphoto.com',
                            'description': f'{key.title()} - Traditional Indian Art Form',
                            'source': 'iStock'
                        })
                    return results
                    
        return []
        
    except Exception as e:
        print(f"Error fetching iStock images: {str(e)}")
        return []


@st.cache_data(ttl=3600)  # Cache for 1 hour
def get_cached_art_form_images(art_form, state=None):
    """
    Get cached images for an art form with enhanced search terms.
    
    Args:
        art_form (str): Name of the art form
        state (str, optional): State name for additional context
        
    Returns:
        list: List of image URLs
    """
    # Create a more specific search query with regional context
    search_terms = {
        'Bharatanatyam': [
            'bharatanatyam dancer tamil nadu',
            'bharatanatyam performance',
            'bharatanatyam dance pose',
            'bharatanatyam mudras',
            'bharatanatyam costume',
            'bharatanatyam temple dance',
            'bharatanatyam classical dance',
            'bharatanatyam dancer stage',
            'bharatanatyam dance form',
            'bharatanatyam performance tamil'
        ],
        'Kathakali': [
            'kathakali dance kerala',
            'kathakali makeup',
            'kathakali performance',
            'kathakali costume',
            'kathakali face paint',
            'kathakali traditional',
            'kathakali artist',
            'kathakali drama',
            'kathakali dance form',
            'kathakali kerala'
        ],
        'Kathak': [
            'kathak dance performance',
            'kathak dancer',
            'kathak costume',
            'kathak traditional',
            'kathak classical dance',
            'kathak mudras',
            'kathak pose',
            'kathak stage',
            'kathak dance form',
            'kathak north india'
        ],
        'Odissi': [
            'odissi dance odisha',
            'odissi performance',
            'odissi dancer',
            'odissi costume',
            'odissi traditional',
            'odissi classical dance',
            'odissi mudras',
            'odissi pose',
            'odissi dance form',
            'odissi temple dance'
        ],
        'Kuchipudi': [
            'kuchipudi dance andhra',
            'kuchipudi performance',
            'kuchipudi dancer',
            'kuchipudi costume',
            'kuchipudi traditional',
            'kuchipudi classical dance',
            'kuchipudi mudras',
            'kuchipudi pose',
            'kuchipudi dance form',
            'kuchipudi telugu dance'
        ],
        'Manipuri': [
            'manipuri dance manipur',
            'manipuri performance',
            'manipuri dancer',
            'manipuri costume',
            'manipuri traditional',
            'manipuri classical dance',
            'manipuri pose',
            'manipuri dance form',
            'manipuri northeast',
            'manipuri jagoi'
        ],
        'Mohiniyattam': [
            'mohiniyattam dance kerala',
            'mohiniyattam performance',
            'mohiniyattam dancer',
            'mohiniyattam costume',
            'mohiniyattam traditional',
            'mohiniyattam classical dance',
            'mohiniyattam mudras',
            'mohiniyattam pose',
            'mohiniyattam dance form',
            'mohiniyattam lasya'
        ],
        'Sattriya': [
            'sattriya dance assam',
            'sattriya performance',
            'sattriya dancer',
            'sattriya costume',
            'sattriya traditional',
            'sattriya classical dance',
            'sattriya pose',
            'sattriya dance form',
            'sattriya monastery',
            'sattriya vaishnav'
        ],
        'Tanjore Painting': [
            'thanjavur painting',
            'tanjore painting gold',
            'tanjore painting hindu',
            'thanjavur painting detail',
            'tanjore painting traditional',
            'tanjore painting gods',
            'thanjavur painting temple',
            'tanjore painting heritage',
            'tanjore painting art',
            'thanjavur painting style'
        ],
        'Madhubani Painting': [
            'madhubani painting bihar',
            'madhubani art',
            'madhubani traditional',
            'madhubani folk art',
            'madhubani detail',
            'madhubani village',
            'madhubani heritage',
            'madhubani style',
            'madhubani colors',
            'madhubani bihar'
        ],
        'Warli Painting': [
            'warli painting maharashtra',
            'warli art',
            'warli traditional',
            'warli tribal art',
            'warli detail',
            'warli village',
            'warli heritage',
            'warli style',
            'warli colors',
            'warli maharashtra'
        ],
        'Gond Art': [
            'gond painting madhya pradesh',
            'gond art',
            'gond traditional',
            'gond tribal art',
            'gond detail',
            'gond village',
            'gond heritage',
            'gond style',
            'gond colors',
            'gond mp'
        ],
        'Pattachitra': [
            'pattachitra odisha',
            'pattachitra art',
            'pattachitra traditional',
            'pattachitra folk art',
            'pattachitra detail',
            'pattachitra scroll',
            'pattachitra heritage',
            'pattachitra style',
            'pattachitra colors',
            'pattachitra odisha'
        ],
        'Phulkari': [
            'phulkari embroidery punjab',
            'phulkari work',
            'phulkari traditional',
            'phulkari folk art',
            'phulkari detail',
            'phulkari design',
            'phulkari heritage',
            'phulkari style',
            'phulkari colors',
            'phulkari punjab'
        ],
        'Chikankari': [
            'chikankari lucknow',
            'chikankari embroidery',
            'chikankari traditional',
            'chikankari work',
            'chikankari detail',
            'chikankari design',
            'chikankari heritage',
            'chikankari style',
            'chikankari white',
            'chikankari uttar pradesh'
        ],
        'Zardozi': [
            'zardozi embroidery lucknow',
            'zardozi work',
            'zardozi traditional',
            'zardozi gold',
            'zardozi detail',
            'zardozi design',
            'zardozi heritage',
            'zardozi style',
            'zardozi metallic',
            'zardozi uttar pradesh'
        ]
    }
    
    # Get specific search terms for the art form
    specific_terms = search_terms.get(art_form, [art_form])
    
    # Add state context if available
    if state and state != "All States":
        specific_terms = [f"{term} {state}" for term in specific_terms]
    
    # Try each search term until we find images
    for term in specific_terms:
        try:
            # Try Pexels first
            images = search_pexels_images(term)
            if images:
                return images
            
            # If Pexels fails, try Pixabay
            images = search_pixabay_images(term)
            if images:
                return images
                
            # If both fail, try iStock
            images = get_istock_images(term)
            if images:
                return images
        except Exception as e:
            continue
    
    return None

def search_pexels_images(query):
    """
    Search for images on Pexels with enhanced query handling.
    """
    try:
        headers = {
            'Authorization': PEXELS_API_KEY
        }
        # Remove orientation filter to get more results
        url = f'https://api.pexels.com/v1/search?query={query}&per_page=5'
        response = requests.get(url, headers=headers)
        data = response.json()
        
        if 'photos' in data and data['photos']:
            return [{'url': photo['src']['large'], 'source': 'Pexels'} for photo in data['photos']]
    except Exception as e:
        pass
    return None

def search_pixabay_images(query):
    """
    Search for images on Pixabay with enhanced query handling.
    """
    try:
        # Remove orientation filter to get more results
        url = f'https://pixabay.com/api/?key={PIXABAY_API_KEY}&q={query}&per_page=5'
        response = requests.get(url)
        data = response.json()
        
        if 'hits' in data and data['hits']:
            return [{'url': hit['largeImageURL'], 'source': 'Pixabay'} for hit in data['hits']]
    except Exception as e:
        pass
    return None

def get_cultural_images(category, subcategory=None, count=5):
    """
    Get high-quality images for cultural categories using Pexels API with iStock fallback.
    
    Args:
        category (str): The category to search for (e.g., 'festivals', 'dance_forms')
        subcategory (str, optional): Specific subcategory. Defaults to None.
        count (int, optional): Number of images to fetch. Defaults to 5.
        
    Returns:
        list: List of image data dictionaries
    """
    try:
        # Construct search query
        if subcategory:
            query = f"{subcategory} {category} india"
        else:
            query = f"{category} india"
        
        # Make request to Pexels API
        headers = {
            'Authorization': PEXELS_API_KEY
        }
        url = f'https://api.pexels.com/v1/search?query={urllib.parse.quote(query)}&per_page={count}&orientation=landscape'
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Parse the response
        data = response.json()
        
        # Extract image URLs with metadata
        images = []
        if 'photos' in data and data['photos']:
            for photo in data['photos']:
                if 'src' in photo and 'large2x' in photo['src']:
                    images.append({
                        'url': photo['src']['large2x'],
                        'photographer': photo.get('photographer', 'Unknown'),
                        'photographer_url': photo.get('photographer_url', '#'),
                        'description': photo.get('alt', ''),
                        'source': 'Pexels'
                    })
            
            # If we found images from Pexels, return them
            if images:
                return images
        
        # If no images from Pexels or not enough, try iStock as fallback
        if len(images) < count:
            # Try to get iStock images
            istock_images = get_istock_images(query)
            
            # Combine images from both sources if needed, up to the requested count
            combined_images = images + istock_images
            return combined_images[:count]
            
        # If we have enough Pexels images, return them
        return images
        
    except Exception as e:
        print(f"Error fetching images for {category}: {str(e)}")
        st.error(f"Error fetching images: {str(e)}")
        
        # Try iStock as fallback
        try:
            if subcategory:
                query = f"{subcategory} {category} india"
            else:
                query = f"{category} india"
            
            istock_images = get_istock_images(query)
            if istock_images:
                return istock_images[:count]
        except:
            pass
            
        return []


def verify_image_accessibility(url):
    """
    Verify that an image URL is accessible.
    
    Args:
        url (str): The URL to verify
        
    Returns:
        bool: True if accessible, False otherwise
    """
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200
    except:
        return False 