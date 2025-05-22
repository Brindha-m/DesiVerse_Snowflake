"""
Constants and data definitions for the DesiVerse application.
Contains dictionaries for art forms, facts, tourism tips, and more.
"""

# API Keys
PEXELS_API_KEY = 'LmuL4VEbCt9aw1Jdt992OVcUhn83HGZeJVZEshCgbxu7NUIVMt9v92nH'  # Replace with your Pexels API key
PIXABAY_API_KEY = '50387507-573cae0b9f62d4ec40daf0b1d'  # This is a free API key for testing

# Art form details dictionary with descriptions
art_form_details = {
    'Bharatanatyam': {
        'description': 'Bharatanatyam is one of the oldest classical dance forms of India, originating from Tamil Nadu. It is characterized by fixed upper torso, bent legs, and flexed knees, combined with symbolic hand gestures and facial expressions.',
        'history': 'Dating back to 2000 years, it was originally performed in temples by devadasis. The dance form was revived in the 20th century by Rukmini Devi Arundale.',
        'techniques': 'Includes adavus (basic steps), mudras (hand gestures), and abhinaya (expressions). The dance follows the Carnatic music system.',
        'costume': 'Traditional costume includes a sari with pleats, jewelry, and ghungroos (ankle bells).',
        'famous_practitioners': 'Rukmini Devi Arundale, Balasaraswati, Padma Subrahmanyam'
    },
    'Kathakali': {
        'description': 'Kathakali is a classical dance-drama form from Kerala, known for its elaborate costumes, makeup, and facial expressions. It combines dance, music, and acting to tell stories from Indian epics.',
        'history': 'Originated in the 17th century, it evolved from various art forms including Koodiyattam and Krishnanattam.',
        'techniques': 'Features complex facial expressions, hand gestures, and body movements. The makeup is elaborate and symbolic.',
        'costume': 'Heavy costumes, colorful makeup, and elaborate headgear. The makeup is called chutti.',
        'famous_practitioners': 'Kalamandalam Gopi, Kalamandalam Ramankutty Nair'
    },
    'Kathak': {
        'description': 'Kathak is a classical dance form from North India, characterized by intricate footwork, spins, and storytelling. It combines elements of both Hindu and Muslim cultures.',
        'history': 'Originated in the temples of North India, it evolved during the Mughal era into a court entertainment.',
        'techniques': 'Features complex footwork, spins (chakkars), and storytelling through gestures and expressions.',
        'costume': 'Traditional costume includes a long tunic (angarkha), churidar, and dupatta for women.',
        'famous_practitioners': 'Birju Maharaj, Sitara Devi, Shovana Narayan'
    },
    'Odissi': {
        'description': 'Odissi is a classical dance form from Odisha, characterized by its fluid movements and sculpturesque poses. It is known for its grace and elegance.',
        'history': 'Originated in the temples of Odisha, it was revived in the 20th century after a period of decline.',
        'techniques': 'Features tribhangi (three-bend) posture, chauka (square) stance, and mudras (hand gestures).',
        'costume': 'Traditional costume includes a sari with pleats, silver jewelry, and ghungroos.',
        'famous_practitioners': 'Kelucharan Mohapatra, Sanjukta Panigrahi, Sonal Mansingh'
    },
    'Kuchipudi': {
        'description': 'Kuchipudi is a classical dance form from Andhra Pradesh, known for its graceful movements and dramatic elements. It combines pure dance with storytelling.',
        'history': 'Originated in the village of Kuchipudi in Andhra Pradesh, it was traditionally performed by men.',
        'techniques': 'Features intricate footwork, graceful movements, and dramatic elements. Includes tarangam (dancing on brass plate).',
        'costume': 'Traditional costume includes a sari with pleats, jewelry, and ghungroos. Men wear dhoti and angavastram.',
        'famous_practitioners': 'Vedantam Satyanarayana Sarma, Yamini Krishnamurthy, Raja and Radha Reddy'
    },
    'Manipuri': {
        'description': 'Manipuri is a classical dance form from Manipur, known for its gentle, graceful movements and spiritual themes. It is deeply connected to Vaishnavism.',
        'history': 'Originated in Manipur, it evolved from the Lai Haraoba festival and was influenced by Vaishnavism.',
        'techniques': 'Features gentle, flowing movements, circular patterns, and subtle expressions. Includes both tandava and lasya elements.',
        'costume': 'Traditional costume includes a long skirt (phanek), veil (innaphi), and elaborate jewelry.',
        'famous_practitioners': 'Guru Bipin Singh, Darshana Jhaveri, Priti Patel'
    },
    'Mohiniyattam': {
        'description': 'Mohiniyattam is a classical dance form from Kerala, known for its graceful, feminine movements. It is characterized by its lasya (graceful) style.',
        'history': 'Originated in Kerala, it was revived in the 20th century by Vallathol Narayana Menon.',
        'techniques': 'Features gentle, swaying movements, circular patterns, and subtle expressions. Includes adavus and mudras.',
        'costume': 'Traditional costume includes a white sari with gold border, jewelry, and flowers in hair.',
        'famous_practitioners': 'Kalamandalam Kalyanikutty Amma, Kalamandalam Satyabhama, Kalamandalam Kshemavathy'
    },
    'Sattriya': {
        'description': 'Sattriya is a classical dance form from Assam, originating in the Vaishnavite monasteries. It combines dance, drama, and music.',
        'history': 'Created by Srimanta Sankardev in the 15th century as part of the Vaishnavite movement in Assam.',
        'techniques': 'Features both tandava and lasya elements, with emphasis on bhakti (devotion). Includes various dance numbers and plays.',
        'costume': 'Traditional costume includes dhoti, chadar, and paguri for men, and mekhela-chador for women.',
        'famous_practitioners': 'Guru Jatin Goswami, Indira P.P. Bora, Anwesa Mahanta'
    }
}

# Interesting facts about art forms
art_form_facts = {
    'Tanjore Painting': "Did you know? Tanjore paintings are known for their rich colors, surface richness, and compact composition. They are characterized by the use of gold foil and precious stones, making them one of the most expensive traditional art forms in India.",
    'Madhubani Painting': "Did you know? Madhubani paintings were traditionally created by women on the walls of their homes during festivals and special occasions. The art form was discovered by the world after a major earthquake in 1934 when the walls cracked and revealed these beautiful paintings.",
    'Manjusha Art': "Did you know? Manjusha art is the only art form in India that is displayed in series, telling a complete story through multiple panels. It's deeply connected to the Bishahari festival of Bihar.",
    'Sujni Embroidery': "Did you know? Sujni embroidery originated as a way to make quilts from old saris. The art form uses a unique running stitch that creates beautiful patterns while also making the fabric stronger.",
    'Kalamkari': "Did you know? The word 'Kalamkari' literally means 'pen work' in Persian. Artists use a special pen made from bamboo and date palm to create intricate designs, and the process involves 23 steps!",
    'Warli Painting': "Did you know? Warli paintings use only three colors: white (from rice paste), red (from geru), and black (from soot). The art form is over 2,500 years old and was discovered in the 1970s.",
    'Phulkari': "Did you know? Phulkari embroidery was traditionally made by grandmothers for their granddaughters' wedding trousseau. Each piece could take up to a year to complete!",
    'Chikankari': "Did you know? Chikankari was introduced to India by Empress Noor Jahan, wife of Mughal Emperor Jahangir. The art form uses up to 40 different types of stitches!",
    'Zardozi': "Did you know? Zardozi was once used to adorn the clothes of kings and queens. The art form uses real gold and silver threads, along with precious stones and pearls.",
    'Bidri Work': "Did you know? Bidri work gets its name from the city of Bidar in Karnataka. The art form uses a unique technique of inlaying silver into blackened zinc and copper alloy.",
    'Blue Pottery': "Did you know? Blue Pottery is the only pottery in the world that doesn't use clay! It's made from a special dough of ground quartz stone, powdered glass, and raw materials.",
    'Pattachitra': "Did you know? Pattachitra artists still use natural colors made from stones, minerals, and plants. The art form is known for its intricate details and mythological themes.",
    'Gond Art': "Did you know? Gond art is created by the Gond tribe of Madhya Pradesh. Each painting tells a story and is believed to bring good luck and ward off evil spirits.",
    'Bagh Print': "Did you know? Bagh print uses natural dyes and a unique printing technique that has remained unchanged for over 1,000 years. The process involves 16 stages of printing and washing!",
    'Chanderi Weaving': "Did you know? Chanderi sarees are so fine that they can pass through a ring! The art form dates back to the 11th century and was patronized by the Scindia royal family."
}

# Lesser known heritage sites
lesser_known_sites = {
    'Champaner-Pavagadh': {
        'location': 'Gujarat',
        'description': 'A UNESCO World Heritage site featuring a unique blend of Hindu and Islamic architecture.',
        'significance': 'Ancient capital of Gujarat with well-preserved 16th-century architecture.',
        'tips': 'Best visited during monsoon for lush greenery. Support local guides for authentic experiences.'
    },
    'Majuli Island': {
        'location': 'Assam',
        'description': 'World\'s largest river island and a hub of Assamese culture and Vaishnavite monasteries.',
        'significance': 'Home to unique mask-making traditions and traditional dance forms.',
        'tips': 'Stay in local homestays and participate in traditional craft workshops.'
    },
    'Chettinad': {
        'location': 'Tamil Nadu',
        'description': 'Known for its grand mansions and unique architecture of the Chettiar community.',
        'significance': 'Preserves the rich cultural heritage of the Chettiar merchants.',
        'tips': 'Experience local cuisine and traditional architecture through heritage stays.'
    },
    'Ziro Valley': {
        'location': 'Arunachal Pradesh',
        'description': 'Home to the Apatani tribe and their unique agricultural practices.',
        'significance': 'UNESCO World Heritage site for its cultural landscape.',
        'tips': 'Visit during the Ziro Music Festival for a unique cultural experience.'
    },
    'Shekhawati': {
        'location': 'Rajasthan',
        'description': 'Known for its painted havelis and frescoes.',
        'significance': 'Open-air art gallery showcasing traditional Rajasthani art.',
        'tips': 'Explore on foot or bicycle to minimize environmental impact.'
    }
}

# Responsible tourism tips
responsible_tourism_tips = [
    {
        'category': 'Cultural Preservation',
        'tips': [
            'Support local artisans by purchasing authentic handicrafts',
            'Learn about local customs and traditions before visiting',
            'Respect cultural sites and follow local guidelines',
            'Participate in community-led tourism initiatives'
        ]
    },
    {
        'category': 'Environmental Conservation',
        'tips': [
            'Choose eco-friendly accommodations',
            'Minimize plastic usage and carry reusable items',
            'Use public transport or shared vehicles when possible',
            'Support conservation projects in the area'
        ]
    },
    {
        'category': 'Community Support',
        'tips': [
            'Stay in locally-owned accommodations',
            'Eat at local restaurants and try traditional cuisine',
            'Hire local guides for authentic experiences',
            'Purchase souvenirs from local artisans'
        ]
    },
    {
        'category': 'Wildlife Protection',
        'tips': [
            'Avoid animal-based tourism activities',
            'Choose wildlife sanctuaries that prioritize animal welfare',
            'Maintain safe distance from wildlife',
            'Follow park guidelines and respect animal habitats'
        ]
    }
]

# Quiz questions about Indian art and culture
quiz_questions = [
    {
        "question": "Which classical dance form originated in Kerala?",
        "options": ["Kathak", "Bharatanatyam", "Kathakali", "Odissi"],
        "correct": "Kathakali",
        "explanation": "Kathakali is a classical dance-drama form that originated in Kerala in the 17th century. It is known for its elaborate costumes, makeup, and facial expressions."
    },
    {
        "question": "Which art form is known for its intricate patterns created using wax and dye?",
        "options": ["Madhubani", "Batik", "Warli", "Gond"],
        "correct": "Batik",
        "explanation": "Batik is a traditional art form that uses wax-resist dyeing to create intricate patterns on fabric. It is practiced in various parts of India."
    },
    {
        "question": "Which state is famous for its Phulkari embroidery?",
        "options": ["Rajasthan", "Punjab", "Gujarat", "Karnataka"],
        "correct": "Punjab",
        "explanation": "Phulkari is a traditional embroidery style from Punjab, characterized by its vibrant colors and geometric patterns."
    },
    {
        "question": "Which musical instrument is associated with the Baul tradition of Bengal?",
        "options": ["Sitar", "Ektara", "Tabla", "Sarod"],
        "correct": "Ektara",
        "explanation": "The Ektara is a one-stringed instrument commonly used by Baul musicians in Bengal. It is known for its simple yet distinctive sound."
    },
    {
        "question": "Which art form is known for its intricate paper cutting designs?",
        "options": ["Sanjhi", "Rangoli", "Alpana", "Kolam"],
        "correct": "Sanjhi",
        "explanation": "Sanjhi is a traditional art form from Mathura, Uttar Pradesh, where intricate designs are cut into paper and used to create beautiful patterns."
    }
]

# Cultural categories for gallery
CULTURAL_CATEGORIES = {
    'festivals': [
        'Diwali', 'Holi', 'Durga Puja', 'Ganesh Chaturthi', 'Onam',
        'Pongal', 'Baisakhi', 'Raksha Bandhan', 'Navratri', 'Eid'
    ],
    'dance_forms': [
        'Bharatanatyam', 'Kathak', 'Kathakali', 'Odissi', 'Kuchipudi',
        'Manipuri', 'Mohiniyattam', 'Sattriya', 'Garba', 'Bhangra'
    ],
    'heritage_sites': [
        'Taj Mahal', 'Khajuraho', 'Hampi', 'Konark Sun Temple',
        'Ajanta Caves', 'Ellora Caves', 'Sanchi Stupa', 'Mahabalipuram'
    ],
    'crafts': [
        'Madhubani Painting', 'Warli Art', 'Kalamkari', 'Phulkari',
        'Chikankari', 'Zardozi', 'Bidri Work', 'Blue Pottery'
    ]
}

# Color palettes
INDIAN_COLORS = {
    'primary': ['#FF9933', '#138808', '#000080'],  # Saffron, Green, Navy
    'secondary': ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEEAD'],
    'gradient': ['#FF9933', '#FFB74D', '#FFCC80', '#FFE0B2', '#FFF3E0'],
    'earth': ['#8B4513', '#A0522D', '#CD853F', '#DEB887', '#F5DEB3']
} 