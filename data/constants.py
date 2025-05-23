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
    # Classical Dance Forms
    'Bharatanatyam': "Did you know? Bharatanatyam was originally performed by temple dancers called 'Devadasis' and was revived in the 20th century by Rukmini Devi Arundale.",
    'Kathakali': "Did you know? Kathakali performers undergo 4-5 hours of elaborate makeup using natural colors, and the green face paint represents noble characters.",
    'Kathak': "Did you know? Kathak evolved from storytelling traditions in temples, where dancers would narrate stories through dance and hand gestures.",
    'Odissi': "Did you know? Odissi dance movements are inspired by the sculptures of ancient temples in Odisha, particularly the Konark Sun Temple.",
    'Kuchipudi': "Did you know? Kuchipudi was traditionally performed only by men, even for female roles, until the 20th century.",
    'Manipuri': "Did you know? Manipuri dance is deeply connected to the worship of Lord Krishna, and its graceful movements imitate the gentle swaying of the Manipur hills.",
    'Mohiniyattam': "Did you know? Mohiniyattam is known as the 'Dance of the Enchantress' and is characterized by its emphasis on feminine grace and beauty.",
    'Sattriya': "Did you know? Sattriya was performed exclusively in monasteries for 500 years before being recognized as a classical dance form in 2000.",
    
    # Andhra Pradesh
    'Kalamkari': "Did you know? Kalamkari artists use natural dyes and a special pen made from bamboo to create intricate designs on fabric.",
    'Budithi Brass Craft': "Did you know? Budithi brass craft uses a unique technique of lost-wax casting that has been passed down through generations.",
    
    # Arunachal Pradesh
    'Monpa Mask': "Did you know? Monpa masks are handcrafted using paper mache and natural colors, representing various Buddhist deities.",
    'Thangka Paintings': "Did you know? Thangka paintings are created on cotton or silk and can take up to a year to complete due to their intricate details.",
    'Wancho Wood Carving': "Did you know? Wancho wood carvings often depict tribal myths and legends, with each carving telling a unique story.",
    
    # Assam
    'Bihu Dance': "Did you know? Bihu dance is performed during the harvest festival and involves rapid hand and hip movements symbolizing joy and celebration.",
    'Assam Silk Weaving': "Did you know? Assam silk, particularly Muga silk, is known for its natural golden color and durability, often lasting for generations.",
    
    # Bihar
    'Madhubani Painting': "Did you know? Madhubani paintings were traditionally created by women on the walls of their homes during festivals and special occasions.",
    'Manjusha Art': "Did you know? Manjusha art is the only art form in India that is displayed in a series, telling a complete story through multiple panels.",
    'Sujni Embroidery': "Did you know? Sujni embroidery was traditionally made from old saris and cloth, creating beautiful quilts with stories of daily life.",
    
    # Chhattisgarh
    'Panthi Dance': "Did you know? Panthi dance is performed during the harvest festival and involves synchronized movements with bamboo sticks.",
    'Godna Art': "Did you know? Godna art is a traditional form of tattooing that was used to mark important life events and social status.",
    'Bell Metal Craft': "Did you know? Bell metal craft in Chhattisgarh uses a special alloy of copper and tin, creating unique musical instruments.",
    
    # Goa
    'Dekni Dance': "Did you know? Dekni dance combines Portuguese and Indian cultural elements, performed by women in traditional costumes.",
    'Fugdi Dance': "Did you know? Fugdi dance is performed in a circle formation, with dancers moving in rhythmic patterns while singing folk songs.",
    'Goan Lacework': "Did you know? Goan lacework was introduced by Portuguese nuns and is known for its intricate patterns and delicate designs.",
    
    # Gujarat
    'Garba': "Did you know? Garba dance is performed in concentric circles around a lamp or idol, symbolizing the cycle of life and death.",
    'Patola Weaving': "Did you know? Patola silk sarees can take up to 6 months to weave, with each thread being individually dyed before weaving.",
    'Rogan Art': "Did you know? Rogan art uses castor oil to create intricate designs, with only one family keeping this art form alive.",
    
    # Haryana
    'Phag Dance': "Did you know? Phag dance is performed during the spring festival, with dancers using colorful sticks to create rhythmic patterns.",
    'Embroidery Craft': "Did you know? Haryana's embroidery uses mirror work and colorful threads to create vibrant patterns on fabric.",
    'Charpai Weaving': "Did you know? Charpai weaving is a traditional craft that creates comfortable beds using natural materials like jute and cotton.",
    
    # Himachal Pradesh
    'Kullu Shawl Weaving': "Did you know? Kullu shawls are handwoven using traditional patterns that have been passed down through generations.",
    'Chamba Rumal': "Did you know? Chamba Rumal is a unique form of embroidery that creates intricate designs on both sides of the fabric.",
    'Kangra Painting': "Did you know? Kangra paintings are known for their delicate brushwork and use of natural colors made from minerals and plants.",
    
    # Jharkhand
    'Sohrai Painting': "Did you know? Sohrai paintings are created during the harvest festival using natural colors and depict scenes from daily life.",
    'Chhau Dance': "Did you know? Chhau dance combines martial arts, acrobatics, and storytelling, often performed with elaborate masks.",
    'Dokra Metal Craft': "Did you know? Dokra metal casting uses the lost-wax technique, a method that has remained unchanged for over 4000 years.",
    
    # Karnataka
    'Yakshagana': "Did you know? Yakshagana combines dance, music, and drama, with performers wearing elaborate costumes and makeup.",
    'Bidri Ware': "Did you know? Bidri work uses a special blackened alloy of zinc and copper, inlaid with silver to create striking contrast.",
    'Mysore Painting': "Did you know? Mysore paintings are known for their gesso work, where gold leaf is applied over a special paste to create raised patterns.",
    
    # Kerala
    'Kathakali': "Did you know? Kathakali performers undergo 4-5 hours of elaborate makeup using natural colors, and the green face paint represents noble characters.",
    'Mohiniyattam': "Did you know? Mohiniyattam is known as the 'Dance of the Enchantress' and is characterized by its emphasis on feminine grace and beauty.",
    'Aranmula Kannadi': "Did you know? Aranmula Kannadi is a unique mirror made of metal alloy, with the secret formula known only to a few families.",
    
    # Madhya Pradesh
    'Gond Art': "Did you know? Gond art uses dots and lines to create intricate patterns that tell stories of nature and tribal life.",
    'Bagh Print': "Did you know? Bagh printing uses natural dyes and a special process that makes the colors become more vibrant with each wash.",
    'Chanderi Weaving': "Did you know? Chanderi sarees are known for their sheer texture and gold borders, created using a special weaving technique.",
    
    # Maharashtra
    'Lavani Dance': "Did you know? Lavani dance combines traditional folk music with energetic movements, often performed by women in colorful costumes.",
    'Warli Painting': "Did you know? Warli paintings use only three colors - white (rice paste), red (geru), and black (charcoal) - to create their distinctive tribal art.",
    'Paithani Sarees': "Did you know? Paithani sarees can take up to a year to weave, with each thread being individually dyed before weaving.",
    
    # Manipur
    'Manipuri Dance': "Did you know? Manipuri dance is deeply connected to the worship of Lord Krishna, and its graceful movements imitate the gentle swaying of the Manipur hills.",
    'Longpi Pottery': "Did you know? Longpi pottery is made without using a potter's wheel, using a unique technique of hand molding and stone polishing.",
    'Phanek Weaving': "Did you know? Phanek weaving uses traditional looms and natural dyes to create intricate patterns on fabric.",
    
    # Meghalaya
    'Nongkrem Dance': "Did you know? Nongkrem dance is performed during the harvest festival, with dancers wearing elaborate costumes and headgear.",
    'Bamboo Craft': "Did you know? Meghalaya's bamboo craft creates everything from furniture to musical instruments using sustainable techniques.",
    'Garo Wangala Dance': "Did you know? Garo Wangala dance is performed to thank the sun god for a good harvest, with dancers wearing traditional costumes.",
    
    # Mizoram
    'Cheraw Dance': "Did you know? Cheraw dance involves dancers moving between bamboo sticks that are clapped together in rhythmic patterns.",
    'Mizo Bamboo Dance': "Did you know? Mizo bamboo dance is performed during festivals, with dancers creating complex patterns using bamboo poles.",
    'Puanchei Textiles': "Did you know? Puanchei textiles are handwoven using traditional patterns that have been passed down through generations.",
    
    # Nagaland
    'Hornbill Festival Dances': "Did you know? Hornbill Festival dances showcase the unique cultural heritage of Naga tribes through traditional costumes and movements.",
    'Naga Shawl Weaving': "Did you know? Naga shawls are handwoven using traditional patterns that represent different tribes and social status.",
    'Wood Carving': "Did you know? Naga wood carving often depicts tribal myths and legends, with each carving telling a unique story.",
    
    # Odisha
    'Odissi': "Did you know? Odissi dance movements are inspired by the sculptures of ancient temples in Odisha, particularly the Konark Sun Temple.",
    'Pattachitra': "Did you know? Pattachitra paintings are created on cloth treated with a special mixture of chalk and gum, making them durable for centuries.",
    'Applique Work': "Did you know? Odisha's applique work creates intricate designs by sewing pieces of colored fabric onto a base material.",
    
    # Punjab
    'Bhangra': "Did you know? Bhangra dance originated as a celebration of the harvest season, with energetic movements and traditional music.",
    'Phulkari': "Did you know? Phulkari embroidery uses a special darning stitch that creates a reversible pattern, with the design visible on both sides.",
    'Jutti Making': "Did you know? Punjabi juttis are handcrafted using traditional techniques, with each pair taking several days to complete.",
    
    # Rajasthan
    'Ghoomar Dance': "Did you know? Ghoomar dance is performed by women in colorful ghagras, creating beautiful patterns as they twirl in circles.",
    'Blue Pottery': "Did you know? Blue Pottery is unique because it doesn't use clay, but instead uses a special mixture of ground quartz stone and glass.",
    'Miniature Painting': "Did you know? Miniature paintings were created using brushes made from squirrel hair, with some as fine as a single strand.",
    
    # Sikkim
    'Mask Dance': "Did you know? Sikkim's mask dances are performed during religious festivals, with each mask representing different deities and demons.",
    'Thangka Painting': "Did you know? Thangka paintings are created on cotton or silk and can take up to a year to complete due to their intricate details.",
    'Carpet Weaving': "Did you know? Sikkim's carpet weaving uses traditional Tibetan techniques to create intricate patterns and designs.",
    
    # Tamil Nadu
    'Bharatanatyam': "Did you know? Bharatanatyam was originally performed by temple dancers called 'Devadasis' and was revived in the 20th century by Rukmini Devi Arundale.",
    'Tanjore Painting': "Did you know? Tanjore paintings are known for their rich colors, gold foil work, and semi-precious stones, making them appear three-dimensional.",
    'Stone Carving': "Did you know? Tamil Nadu's stone carving tradition dates back to the Pallava period, creating intricate temple sculptures.",
    
    # Telangana
    'Perini Shivatandavam': "Did you know? Perini Shivatandavam is a warrior dance form that was performed before going to battle to invoke Lord Shiva's blessings.",
    'Nirmal Paintings': "Did you know? Nirmal paintings are created using natural colors and gold leaf, with each piece taking several months to complete.",
    'Bidri Craft': "Did you know? Bidri work uses a special blackened alloy of zinc and copper, inlaid with silver to create striking contrast.",
    
    # Tripura
    'Hojagiri Dance': "Did you know? Hojagiri dance is performed by women balancing earthen pitchers on their heads while dancing gracefully.",
    'Bamboo Craft': "Did you know? Tripura's bamboo craft creates everything from furniture to musical instruments using sustainable techniques.",
    'Risa Textile Weaving': "Did you know? Risa textiles are handwoven using traditional patterns that have been passed down through generations.",
    
    # Uttar Pradesh
    'Chikankari': "Did you know? Chikankari embroidery uses up to 40 different types of stitches, each with its own unique purpose and effect.",
    'Zardozi': "Did you know? Zardozi work uses real gold and silver threads, along with precious stones, to create luxurious embroidery patterns.",
    'Wood Inlay': "Did you know? Uttar Pradesh's wood inlay work creates intricate patterns by embedding different materials into wood surfaces.",
    
    # Uttarakhand
    'Aipan': "Did you know? Aipan designs are created using rice paste and are considered sacred in Kumaoni culture.",
    'Wood Carving': "Did you know? Uttarakhand's wood carving tradition creates intricate designs on doors, windows, and furniture.",
    'Stone Carving': "Did you know? Stone carving in Uttarakhand often depicts scenes from Hindu mythology and local folklore.",
    
    # Other Traditional Arts
    'Kolam': "Did you know? Kolam designs are drawn daily at dawn using rice flour, serving as both decoration and food for ants and birds.",
    'Rangoli': "Did you know? Rangoli patterns are believed to welcome prosperity and ward off evil spirits from the home.",
    'Sanjhi': "Did you know? Sanjhi paper cutting art was traditionally used to create stencils for decorating temples and homes.",
    
    # Contemporary Folk Arts
    'Lippan Kaam': "Did you know? Lippan Kaam uses a mixture of mud and camel dung to create mirror work designs on walls.",
    'Rogan Art': "Did you know? Rogan art uses castor oil to create intricate designs, with only one family keeping this art form alive.",
    'Mata Ni Pachedi': "Did you know? Mata Ni Pachedi temple cloths are painted using natural dyes and tell stories of the goddess.",
    'Pabuji Ki Phad': "Did you know? Pabuji Ki Phad scrolls can be up to 30 feet long and are used to tell the story of the folk deity Pabuji."
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