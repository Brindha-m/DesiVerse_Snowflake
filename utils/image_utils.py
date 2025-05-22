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
        # Since direct API access to iStock requires a paid account and API key,
        # we'll use a curated list of common art form images from iStock
        # In a production app, you would integrate properly with their API
        
        # Static mapping of common art forms to iStock image URLs
        istock_images = {
            "bharatanatyam": [
                "https://media.istockphoto.com/id/610640662/photo/bharatanatyam-dancer.jpg",
                "https://media.istockphoto.com/id/1301207350/photo/bharatanatyam-painting-in-thanjavur-style.jpg",
                "https://media.istockphoto.com/id/1324019877/photo/bharatanatyam-dancer.jpg"
            ],
            "kathakali": [
                "https://media.istockphoto.com/id/498570377/photo/kathakali-dancer.jpg",
                "https://media.istockphoto.com/id/1199971488/photo/kathakali-face-traditional-ancient-dance-form-kochi-kerala-india.jpg",
                "https://media.istockphoto.com/id/170935691/photo/kathakali.jpg"
            ],
            "kathak": [
                "https://media.istockphoto.com/id/1158971075/photo/kathak-dancer-performing-on-stage.jpg",
                "https://media.istockphoto.com/id/1207105721/photo/portrait-indian-beautiful-woman-dancing-kathak-dance.jpg",
                "https://media.istockphoto.com/id/1310060573/photo/portrait-of-indian-female-dancer-in-kathak-dance-pose.jpg"
            ],
            "thanjavur painting": [
                "https://media.istockphoto.com/id/1301207350/photo/bharatanatyam-painting-in-thanjavur-style.jpg",
                "https://media.istockphoto.com/id/1431845715/photo/thanjavur-painting-on-display-at-a-gallery.jpg",
                "https://media.istockphoto.com/id/904553646/photo/tanjore-painting-of-lord-krishna.jpg"
            ],
            "madhubani painting": [
                "https://media.istockphoto.com/id/1208339282/photo/madhubani-painting-bihar-india.jpg",
                "https://media.istockphoto.com/id/1157141925/photo/madhubani-fish-painting.jpg",
                "https://media.istockphoto.com/id/535853421/photo/madhubani-painting-of-hindu-goddess-sita.jpg"
            ]
        }
        
        # Simplify the query to match our key terms
        query_lower = query.lower()
        results = []
        
        # Look for matches in our static mapping
        for key, urls in istock_images.items():
            if key in query_lower:
                for i, url in enumerate(urls):
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
                    for i, url in enumerate(urls):
                        results.append({
                            'url': url,
                            'photographer': 'iStock Contributor',
                            'photographer_url': 'https://www.istockphoto.com',
                            'description': f'{key.title()} - Traditional Indian Art Form',
                            'source': 'iStock'
                        })
                    return results
                    
        # Return empty list if no matches
        return []
        
    except Exception as e:
        print(f"Error fetching iStock images: {str(e)}")
        return []


@st.cache_data(ttl=3600)  # Cache for 1 hour
def get_cached_art_form_images(art_form, state=None):
    """
    Cached version of get_art_form_images for better performance.
    
    Args:
        art_form (str): The art form to search for
        state (str, optional): The state to include in the search. Defaults to None.
        
    Returns:
        list: List of image data dictionaries with URLs and photographer info
    """
    return get_art_form_images(art_form, state)


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