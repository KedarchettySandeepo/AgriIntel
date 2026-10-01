import streamlit as st
import streamlit.components.v1 as components
from ultralytics import YOLO
from serpapi_search import search_agriculture
from PIL import Image
from pathlib import Path
from urllib.parse import urlparse

@st.cache_data(ttl=1800, show_spinner=False)
def cached_agriculture_search(crop_name, disease_name):
    """Fetch current agricultural references through the existing SerpApi helper."""
    return search_agriculture(
        disease_name=disease_name,
        crop_name=crop_name
    )

def source_domain(url):
    try:
        return urlparse(url).netloc.replace("www.", "")
    except Exception:
        return ""

import html
# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="AgriIntel — AI Crop Disease Intelligence",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)
# ============================================================
# PROJECT PATH
# ============================================================
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = (
    BASE_DIR
    / "runs"
    / "classify"
    / "runs"
    / "classify"
    / "crop_disease_classifier_v4-2"
    / "weights"
    / "best.pt"
)
# ============================================================
# PADDY CLASSES
# ============================================================
PADDY_CLASSES = {
    "bacterial_leaf_blight",
    "bacterial_leaf_streak",
    "bacterial_panicle_blight",
    "blast",
    "brown_spot",
    "dead_heart",
    "downy_mildew",
    "hispa",
    "normal",
    "tungro"
}
# ============================================================
# MULTILINGUAL UI
# ============================================================
LANGUAGES = {
    "English": "en",
    "हिन्दी": "hi",
    "ଓଡ଼ିଆ": "or",
}
UI_TEXT = {
    "en": {
        "app": "🌱 AI Crop Disease Detector",
        "sidebar": "Upload a crop image to identify the crop and its disease or condition.",
        "intro": "Upload a crop or leaf image and let the AI analyze its disease or condition.",
        "upload": "📷 Upload Crop Image",
        "upload_help": "Upload a clear crop or leaf image.",
        "waiting": "👆 Upload a crop or leaf image above to start the analysis.",
        "uploaded": "Uploaded Crop Image",
        "result": "🔬 Detection Result",
        "crop": "🌱 Crop",
        "condition": "🦠 Disease / Condition",
        "confidence": "🤖 AI Confidence",
        "confidence_title": "📊 Prediction Confidence",
        "other": "🔎 Other Possible Predictions",
        "info": "📚 Disease / Condition Information",
        "description": "Description",
        "symptoms": "Symptoms",
        "management": "Management",
        "farmer_action": "🌾 What to do next",
        "listen": "🔊 Listen to result",
        "running": "🔬 Running AI prediction...",
        "disclaimer": "⚠️ AI-assisted result only. For actual agricultural treatment or management decisions, confirm the diagnosis with a qualified agricultural expert.",
        "high": "🟢 High confidence prediction",
        "moderate": "🟡 Moderate confidence prediction",
        "low": "🔴 Low confidence prediction",
    },
    "hi": {
        "app": "🌱 एआई फसल रोग पहचानक",
        "sidebar": "फसल और उसके रोग या स्थिति की पहचान करने के लिए तस्वीर अपलोड करें।",
        "intro": "फसल या पत्ती की तस्वीर अपलोड करें और एआई से रोग या स्थिति का विश्लेषण करवाएं।",
        "upload": "📷 फसल की तस्वीर अपलोड करें",
        "upload_help": "पत्ती की तस्वीर अपलोड करें",
        "waiting": "👆 विश्लेषण शुरू करने के लिए ऊपर फसल या पत्ती की तस्वीर अपलोड करें।",
        "uploaded": "अपलोड की गई फसल की तस्वीर",
        "result": "🔬 पहचान का परिणाम",
        "crop": "🌱 फसल",
        "condition": "🦠 रोग / स्थिति",
        "confidence": "🎯 एआई विश्वसनीयता",
        "confidence_title": "📊 भविष्यवाणी की विश्वसनीयता",
        "other": "🔎 अन्य संभावित परिणाम",
        "info": "📚 रोग / स्थिति की जानकारी",
        "description": "विवरण",
        "symptoms": "लक्षण",
        "management": "प्रबंधन",
        "farmer_action": "🌾 आगे क्या करें",
        "listen": "🔊 परिणाम सुनें",
        "running": "🔬 एआई भविष्यवाणी चल रही है...",
        "disclaimer": "⚠️ यह केवल एआई-सहायित परिणाम है। वास्तविक कृषि उपचार या प्रबंधन निर्णय लेने से पहले योग्य कृषि विशेषज्ञ से पुष्टि करें।",
        "high": "🟢 उच्च विश्वसनीयता",
        "moderate": "🟡 मध्यम विश्वसनीयता",
        "low": "🔴 कम विश्वसनीयता",
    },
    "or": {
        "app": "🌱 AI ଫସଲ ରୋଗ ଚିହ୍ନଟକାରୀ",
        "sidebar": "ଫସଲ ଏବଂ ଏହାର ରୋଗ କିମ୍ବା ଅବସ୍ଥା ଚିହ୍ନଟ ପାଇଁ ଛବି ଅପଲୋଡ୍ କରନ୍ତୁ।",
        "intro": "ଫସଲ କିମ୍ବା ପତ୍ରର ଛବି ଅପଲୋଡ୍ କରନ୍ତୁ ଏବଂ AI ଦ୍ୱାରା ରୋଗ କିମ୍ବା ଅବସ୍ଥା ବିଶ୍ଳେଷଣ କରନ୍ତୁ।",
        "upload": "📷 ଫସଲର ଛବି ଅପଲୋଡ୍ କରନ୍ତୁ",
        "upload_help": "ପତ୍ରର ଛବି ଅପଲୋଡ୍ କରନ୍ତୁ",
        "waiting": "👆 ବିଶ୍ଳେଷଣ ଆରମ୍ଭ ପାଇଁ ଉପରେ ଫସଲ କିମ୍ବା ପତ୍ରର ଛବି ଅପଲୋଡ୍ କରନ୍ତୁ।",
        "uploaded": "ଅପଲୋଡ୍ ହୋଇଥିବା ଫସଲ ଛବି",
        "result": "🔬 ଚିହ୍ନଟ ଫଳାଫଳ",
        "crop": "🌱 ଫସଲ",
        "condition": "🦠 ରୋଗ / ଅବସ୍ଥା",
        "confidence": "🎯 AI ବିଶ୍ୱସନୀୟତା",
        "confidence_title": "📊 ପୂର୍ବାନୁମାନ ବିଶ୍ୱସନୀୟତା",
        "other": "🔎 ଅନ୍ୟ ସମ୍ଭାବ୍ୟ ଫଳାଫଳ",
        "info": "📚 ରୋଗ / ଅବସ୍ଥା ସୂଚନା",
        "description": "ବିବରଣୀ",
        "symptoms": "ଲକ୍ଷଣ",
        "management": "ପରିଚାଳନା",
        "farmer_action": "🌾 ପରବର୍ତ୍ତୀ ପଦକ୍ଷେପ",
        "listen": "🔊 ଫଳାଫଳ ଶୁଣନ୍ତୁ",
        "running": "🔬 AI ପୂର୍ବାନୁମାନ ଚାଲୁଛି...",
        "disclaimer": "⚠️ ଏହା କେବଳ AI ସହାୟିତ ଫଳାଫଳ। ପ୍ରକୃତ କୃଷି ଚିକିତ୍ସା କିମ୍ବା ପରିଚାଳନା ନିଷ୍ପତ୍ତି ପୂର୍ବରୁ ଯୋଗ୍ୟ କୃଷି ବିଶେଷଜ୍ଞଙ୍କଠାରୁ ନିଶ୍ଚିତ କରନ୍ତୁ।",
        "high": "🟢 ଉଚ୍ଚ ବିଶ୍ୱସନୀୟତା",
        "moderate": "🟡 ମଧ୍ୟମ ବିଶ୍ୱସନୀୟତା",
        "low": "🔴 କମ ବିଶ୍ୱସନୀୟତା",
    },
}
CROP_NAMES = {
    "en": {},
    "hi": {
        "Apple": "सेब", "Blueberry": "ब्लूबेरी", "Cherry_(including_sour)": "चेरी",
        "Corn_(maize)": "मक्का", "Grape": "अंगूर", "Orange": "संतरा",
        "Paddy": "धान / चावल", "Peach": "आड़ू", "Pepper,_bell": "शिमला मिर्च",
        "Potato": "आलू", "Raspberry": "रास्पबेरी", "Soybean": "सोयाबीन",
        "Squash": "स्क्वैश", "Strawberry": "स्ट्रॉबेरी", "Tomato": "टमाटर", "Wheat": "गेहूं",
    },
    "or": {
        "Apple": "ସେଓ", "Blueberry": "ବ୍ଲୁବେରି", "Cherry_(including_sour)": "ଚେରି",
        "Corn_(maize)": "ମକା", "Grape": "ଅଙ୍ଗୁର", "Orange": "କମଳା",
        "Paddy": "ଧାନ / ଚାଉଳ", "Peach": "ପିଚ୍", "Pepper,_bell": "କ୍ୟାପ୍ସିକମ୍",
        "Potato": "ଆଳୁ", "Raspberry": "ରାସ୍ପବେରି", "Soybean": "ସୋୟାବିନ୍",
        "Squash": "ସ୍କ୍ୱାଶ୍", "Strawberry": "ଷ୍ଟ୍ରବେରି", "Tomato": "ଟମାଟୋ", "Wheat": "ଗହମ",
    },
}
CONDITION_NAMES = {
    "hi": {
        "healthy": "स्वस्थ", "normal": "सामान्य", "bacterial leaf blight": "बैक्टीरियल लीफ ब्लाइट",
        "bacterial leaf streak": "बैक्टीरियल लीफ स्ट्रीक", "bacterial panicle blight": "बैक्टीरियल पैनिकल ब्लाइट",
        "blast": "ब्लास्ट", "brown spot": "ब्राउन स्पॉट", "dead heart": "डेड हार्ट",
        "downy mildew": "डाउनी मिल्ड्यू", "hispa": "हिस्पा", "tungro": "टुंग्रो",
        "powdery mildew": "पाउडरी मिल्ड्यू", "leaf rust": "लीफ रस्ट", "stem rust": "स्टेम रस्ट",
        "yellow rust": "येलो रस्ट", "septoria": "सेप्टोरिया", "black rot": "ब्लैक रॉट",
        "apple scab": "एप्पल स्कैब", "cedar apple rust": "सीडर एप्पल रस्ट",
    },
    "or": {
        "healthy": "ସୁସ୍ଥ", "normal": "ସାଧାରଣ", "bacterial leaf blight": "ବ୍ୟାକ୍ଟେରିଆଲ୍ ଲିଫ୍ ବ୍ଲାଇଟ୍",
        "bacterial leaf streak": "ବ୍ୟାକ୍ଟେରିଆଲ୍ ଲିଫ୍ ଷ୍ଟ୍ରିକ୍", "bacterial panicle blight": "ବ୍ୟାକ୍ଟେରିଆଲ୍ ପାନିକଲ୍ ବ୍ଲାଇଟ୍",
        "blast": "ବ୍ଲାଷ୍ଟ", "brown spot": "ବ୍ରାଉନ୍ ସ୍ପଟ୍", "dead heart": "ଡେଡ୍ ହାର୍ଟ",
        "downy mildew": "ଡାଉନି ମିଲଡିଉ", "hispa": "ହିସ୍ପା", "tungro": "ଟୁଙ୍ଗ୍ରୋ",
        "powdery mildew": "ପାଉଡରି ମିଲଡିଉ", "leaf rust": "ଲିଫ୍ ରଷ୍ଟ", "stem rust": "ଷ୍ଟେମ୍ ରଷ୍ଟ",
        "yellow rust": "ୟେଲୋ ରଷ୍ଟ", "septoria": "ସେପ୍ଟୋରିଆ", "black rot": "ବ୍ଲାକ୍ ରଟ୍",
        "apple scab": "ଆପଲ୍ ସ୍କାବ୍", "cedar apple rust": "ସିଡାର୍ ଆପଲ୍ ରଷ୍ଟ",
    },
}
WHEAT_INFO = {
    "Wheat___healthy": ("The model classified the wheat plant as healthy.", "No major disease pattern from the trained Wheat classes was detected.", "Continue regular field monitoring and good crop-management practices."),
    "Wheat___leaf_rust": ("A fungal disease affecting wheat leaves.", "Small rust-colored pustules may appear on leaf surfaces.", "Follow locally recommended resistant varieties and disease-management practices."),
    "Wheat___stem_rust": ("A fungal disease affecting wheat stems and leaves.", "Reddish-brown rust pustules may develop on stems and leaves.", "Monitor fields and follow locally recommended disease-management practices."),
    "Wheat___yellow_rust": ("A fungal disease affecting wheat foliage.", "Yellow or orange-yellow rust pustules may form in stripes on leaves.", "Monitor fields and follow locally recommended disease-management guidance."),
    "Wheat___powdery_mildew": ("A fungal disease affecting wheat foliage.", "White powder-like fungal growth may appear on leaf surfaces.", "Follow locally recommended disease-management practices."),
    "Wheat___septoria": ("A fungal disease affecting wheat leaves.", "Dark or brown leaf lesions may develop on affected leaves.", "Follow locally recommended disease-management practices."),
}
# ============================================================
# DISEASE INFORMATION
# ============================================================
DISEASE_INFO = {
    # --------------------------------------------------------
    # APPLE
    # --------------------------------------------------------
    "Apple___Apple_scab": {
        "description": "A fungal disease affecting apple leaves and fruit.",
        "symptoms": "Olive or brown circular lesions may appear on leaves and fruit.",
        "management": "Use resistant varieties where available and follow locally recommended orchard-management practices."
    },
    "Apple___Black_rot": {
        "description": "A fungal disease affecting apple leaves and fruit.",
        "symptoms": "Dark lesions may develop on leaves and fruit, with fruit eventually developing dark rot.",
        "management": "Remove infected plant material and maintain good orchard sanitation."
    },
    "Apple___Cedar_apple_rust": {
        "description": "A fungal disease affecting apple foliage.",
        "symptoms": "Yellow-orange spots may appear on leaves.",
        "management": "Use resistant varieties where available and follow recommended disease-management practices."
    },
    "Apple___healthy": {
        "description": "The model classified the apple plant as healthy.",
        "symptoms": "No major disease pattern from the trained classes was detected.",
        "management": "Continue regular monitoring and good orchard-management practices."
    },
    # --------------------------------------------------------
    # BLUEBERRY
    # --------------------------------------------------------
    "Blueberry___healthy": {
        "description": "The model classified the blueberry plant as healthy.",
        "symptoms": "No major disease pattern from the trained classes was detected.",
        "management": "Continue routine monitoring and good crop-management practices."
    },
    # --------------------------------------------------------
    # CHERRY
    # --------------------------------------------------------
    "Cherry_(including_sour)___Powdery_mildew": {
        "description": "A fungal disease affecting cherry foliage.",
        "symptoms": "White or gray powder-like fungal growth may appear on leaf surfaces.",
        "management": "Improve air circulation and follow locally recommended disease-management practices."
    },
    "Cherry_(including_sour)___healthy": {
        "description": "The model classified the cherry plant as healthy.",
        "symptoms": "No major disease pattern from the trained classes was detected.",
        "management": "Continue regular monitoring and orchard-management practices."
    },
    # --------------------------------------------------------
    # CORN
    # --------------------------------------------------------
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "description": "A fungal disease affecting maize leaves.",
        "symptoms": "Gray or tan rectangular lesions may develop on leaves.",
        "management": "Use resistant hybrids where available and follow recommended crop-management practices."
    },
    "Corn_(maize)___Common_rust_": {
        "description": "A fungal disease affecting maize.",
        "symptoms": "Reddish-brown rust-colored pustules may appear on leaves.",
        "management": "Use resistant hybrids where available and follow local crop-management recommendations."
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "description": "A fungal disease affecting maize leaves.",
        "symptoms": "Long gray-green or brown lesions may develop on leaves.",
        "management": "Use resistant hybrids and recommended crop-management practices."
    },
    "Corn_(maize)___healthy": {
        "description": "The model classified the maize plant as healthy.",
        "symptoms": "No major disease pattern from the trained classes was detected.",
        "management": "Continue monitoring and good maize-management practices."
    },
    # --------------------------------------------------------
    # GRAPE
    # --------------------------------------------------------
    "Grape___Black_rot": {
        "description": "A fungal disease affecting grape leaves and fruit.",
        "symptoms": "Brown or reddish leaf lesions and darkened fruit may occur.",
        "management": "Remove infected material and maintain vineyard sanitation."
    },
    "Grape___Esca_(Black_Measles)": {
        "description": "A disease complex affecting grapevines.",
        "symptoms": "Leaf discoloration and characteristic spotting may occur.",
        "management": "Maintain vineyard sanitation and follow locally recommended management practices."
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "description": "A fungal disease affecting grape foliage.",
        "symptoms": "Leaf spots and blighted areas may develop.",
        "management": "Remove heavily infected material and maintain good vineyard management."
    },
    "Grape___healthy": {
        "description": "The model classified the grape plant as healthy.",
        "symptoms": "No major disease pattern from the trained classes was detected.",
        "management": "Continue regular vineyard monitoring."
    },
    # --------------------------------------------------------
    # ORANGE
    # --------------------------------------------------------
    "Orange___Haunglongbing_(Citrus_greening)": {
        "description": "A serious citrus disease associated with bacterial pathogens and insect vectors.",
        "symptoms": "Leaves may show uneven yellowing or blotchy discoloration.",
        "management": "Follow local citrus-health guidance and monitor insect vectors."
    },
    # --------------------------------------------------------
    # PADDY
    # --------------------------------------------------------
    "Paddy___bacterial_leaf_blight": {
        "description": "A bacterial disease affecting rice leaves.",
        "symptoms": "Water-soaked or yellowing lesions may develop along leaf margins.",
        "management": "Use resistant varieties where available and follow locally recommended crop-management practices."
    },
    "Paddy___bacterial_leaf_streak": {
        "description": "A bacterial disease affecting rice foliage.",
        "symptoms": "Narrow water-soaked streaks can appear on leaves.",
        "management": "Use appropriate resistant varieties and recommended crop-management practices."
    },
    "Paddy___bacterial_panicle_blight": {
        "description": "A bacterial condition affecting rice panicles.",
        "symptoms": "Panicle and grain development may be affected.",
        "management": "Maintain good field sanitation and follow locally recommended crop-management practices."
    },
    "Paddy___blast": {
        "description": "A major fungal disease of rice associated with Magnaporthe oryzae.",
        "symptoms": "Spindle-shaped lesions with gray centers and darker margins may develop on leaves.",
        "management": "Use resistant varieties where available and follow locally recommended disease-management practices."
    },
    "Paddy___brown_spot": {
        "description": "A fungal disease affecting rice leaves.",
        "symptoms": "Brown circular or oval spots may develop on leaves.",
        "management": "Maintain balanced crop nutrition and follow recommended disease-management practices."
    },
    "Paddy___dead_heart": {
        "description": "A rice condition in which the central shoot dries and dies, commonly associated with insect damage.",
        "symptoms": "The central shoot may dry while surrounding leaves remain green.",
        "management": "Monitor fields for insect pests and follow integrated pest-management practices."
    },
    "Paddy___downy_mildew": {
        "description": "A disease condition affecting rice foliage.",
        "symptoms": "Yellowish or pale leaf areas may develop.",
        "management": "Maintain appropriate field conditions and follow locally recommended disease-management practices."
    },
    "Paddy___hispa": {
        "description": "An insect pest condition affecting rice leaves.",
        "symptoms": "Leaf surfaces may show scraping and feeding damage.",
        "management": "Monitor pest populations and follow integrated pest-management practices."
    },
    "Paddy___normal": {
        "description": "The model classified the rice plant as normal or healthy.",
        "symptoms": "No major disease or pest pattern from the trained Paddy classes was detected.",
        "management": "Continue regular field monitoring and good crop-management practices."
    },
    "Paddy___tungro": {
        "description": "A viral disease complex affecting rice and associated with insect vectors.",
        "symptoms": "Yellowing, orange-yellow discoloration, stunting and reduced growth may occur.",
        "management": "Use healthy planting material and follow locally recommended vector-management practices."
    },
    # --------------------------------------------------------
    # PEACH
    # --------------------------------------------------------
    "Peach___Bacterial_spot": {
        "description": "A bacterial disease affecting peach leaves and fruit.",
        "symptoms": "Small dark spots may develop on leaves and fruit.",
        "management": "Maintain orchard sanitation and follow recommended disease-management practices."
    },
    "Peach___healthy": {
        "description": "The model classified the peach plant as healthy.",
        "symptoms": "No major disease pattern from the trained classes was detected.",
        "management": "Continue routine orchard monitoring."
    },
    # --------------------------------------------------------
    # PEPPER
    # --------------------------------------------------------
    "Pepper,_bell___Bacterial_spot": {
        "description": "A bacterial disease affecting pepper foliage and fruit.",
        "symptoms": "Small dark or water-soaked spots may develop.",
        "management": "Use healthy planting material and maintain sanitation."
    },
    "Pepper,_bell___healthy": {
        "description": "The model classified the bell pepper plant as healthy.",
        "symptoms": "No major disease pattern from the trained classes was detected.",
        "management": "Continue regular crop monitoring."
    },
    # --------------------------------------------------------
    # POTATO
    # --------------------------------------------------------
    "Potato___Early_blight": {
        "description": "A fungal disease affecting potato foliage.",
        "symptoms": "Dark lesions with concentric rings may develop on leaves.",
        "management": "Use appropriate sanitation, crop rotation and locally recommended disease-management practices."
    },
    "Potato___Late_blight": {
        "description": "A serious disease affecting potato leaves and tubers.",
        "symptoms": "Dark water-soaked lesions may develop rapidly.",
        "management": "Monitor fields closely and follow locally recommended late-blight management practices."
    },
    "Potato___healthy": {
        "description": "The model classified the potato plant as healthy.",
        "symptoms": "No major disease pattern from the trained classes was detected.",
        "management": "Continue field monitoring and good potato-management practices."
    },
    # --------------------------------------------------------
    # RASPBERRY
    # --------------------------------------------------------
    "Raspberry___healthy": {
        "description": "The model classified the raspberry plant as healthy.",
        "symptoms": "No major disease pattern from the trained classes was detected.",
        "management": "Continue routine crop monitoring."
    },
    # --------------------------------------------------------
    # SOYBEAN
    # --------------------------------------------------------
    "Soybean___healthy": {
        "description": "The model classified the soybean plant as healthy.",
        "symptoms": "No major disease pattern from the trained classes was detected.",
        "management": "Continue regular crop monitoring."
    },
    # --------------------------------------------------------
    # SQUASH
    # --------------------------------------------------------
    "Squash___Powdery_mildew": {
        "description": "A fungal disease affecting squash foliage.",
        "symptoms": "White powder-like growth may appear on leaf surfaces.",
        "management": "Improve air circulation and follow locally recommended disease-management practices."
    },
    # --------------------------------------------------------
    # STRAWBERRY
    # --------------------------------------------------------
    "Strawberry___Leaf_scorch": {
        "description": "A disease condition affecting strawberry foliage.",
        "symptoms": "Dark or scorched-looking areas may develop on leaves.",
        "management": "Maintain field sanitation and follow recommended crop-management practices."
    },
    "Strawberry___healthy": {
        "description": "The model classified the strawberry plant as healthy.",
        "symptoms": "No major disease pattern from the trained classes was detected.",
        "management": "Continue regular monitoring."
    },
    # --------------------------------------------------------
    # TOMATO
    # --------------------------------------------------------
    "Tomato___Bacterial_spot": {
        "description": "A bacterial disease affecting tomato leaves and fruit.",
        "symptoms": "Small dark spots may appear on leaves, stems or fruit.",
        "management": "Use healthy planting material and maintain good sanitation."
    },
    "Tomato___Early_blight": {
        "description": "A fungal disease affecting tomato foliage.",
        "symptoms": "Dark lesions with concentric rings may appear on older leaves.",
        "management": "Remove heavily infected material and maintain good sanitation."
    },
    "Tomato___Late_blight": {
        "description": "A serious disease that can rapidly affect tomato foliage and fruit.",
        "symptoms": "Dark water-soaked lesions may develop and expand quickly.",
        "management": "Monitor plants closely and follow locally recommended management practices."
    },
    "Tomato___Leaf_Mold": {
        "description": "A fungal disease affecting tomato foliage, particularly under humid conditions.",
        "symptoms": "Yellowish areas may develop on the upper leaf surface with fungal growth underneath.",
        "management": "Improve ventilation and reduce prolonged leaf wetness."
    },
    "Tomato___Septoria_leaf_spot": {
        "description": "A fungal disease affecting tomato leaves.",
        "symptoms": "Small circular spots with darker margins may develop.",
        "management": "Remove infected plant material and maintain good sanitation."
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "description": "An insect pest condition affecting tomato foliage.",
        "symptoms": "Fine stippling, yellowing and webbing may appear.",
        "management": "Monitor plants regularly and follow integrated pest-management practices."
    },
    "Tomato___Target_Spot": {
        "description": "A fungal disease affecting tomato foliage and fruit.",
        "symptoms": "Circular brown lesions with target-like patterns may develop.",
        "management": "Maintain good sanitation and follow recommended disease-management practices."
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "description": "A viral disease associated with whitefly transmission.",
        "symptoms": "Leaf curling, yellowing, reduced leaf size and stunted growth may occur.",
        "management": "Use healthy planting material and follow locally recommended vector-management practices."
    },
    "Tomato___Tomato_mosaic_virus": {
        "description": "A viral disease affecting tomato plants.",
        "symptoms": "Mottled or mosaic patterns may appear on leaves.",
        "management": "Maintain sanitation and avoid spreading infected plant material."
    },
    "Tomato___healthy": {
        "description": "The model classified the tomato plant as healthy.",
        "symptoms": "No major disease pattern from the trained classes was detected.",
        "management": "Continue routine monitoring and good crop-management practices."
    }
}
# ============================================================
# HELPER FUNCTIONS
# ============================================================
def get_crop_name(class_name):
    if "___" in class_name:
        return class_name.split("___")[0]
    return class_name
def get_condition_name(class_name):
    if "___" in class_name:
        return class_name.split("___", 1)[1]
    return class_name
def readable_crop(name):
    name = name.replace("_", " ")
    if name == "Corn (maize)":
        return "Corn (Maize)"
    if name == "Pepper, bell":
        return "Bell Pepper"
    return name
def readable_condition(name):
    readable = (
        name
        .replace("_", " ")
        .replace("  ", " ")
    )
    key = readable.strip().lower()
    return CONDITION_NAMES.get(language, {}).get(key, readable)
def translated_crop(name):
    return CROP_NAMES.get(language, {}).get(name, readable_crop(name))
# ============================================================
# VOICE OUTPUT
# ============================================================
def speak_result(text_to_speak):
    """Use the browser's built-in speech synthesis; no external API needed."""
    safe_text = html.escape(text_to_speak, quote=True)
    language_code = {
        "en": "en-IN",
        "hi": "hi-IN",
        "or": "or-IN",
    }.get(language, "en-IN")
    components.html(
        f"""
        \<script>
        function speakText() {{
            const text = {safe_text!r};
            if (!('speechSynthesis' in window)) {{
                alert('Speech output is not supported by this browser.');
                return;
            }}
            window.speechSynthesis.cancel();
            const utterance = new SpeechSynthesisUtterance(text);
            utterance.lang = "{language_code}";
            utterance.rate = 0.9;
            utterance.pitch = 1.0;
            window.speechSynthesis.speak(utterance);
        }}
        speakText();
        \</script>
        """,
        height=0,
    )
def farmer_action(class_name):
    """Short, non-prescriptive next-step guidance for farmers."""
    condition_key = get_condition_name(class_name).lower()
    if condition_key in {"healthy", "normal"}:
        return {
            "en": "The image appears healthy. Continue regular field monitoring and good crop-management practices.",
            "hi": "फसल स्वस्थ दिखाई दे रही है। नियमित निगरानी और अच्छी फसल प्रबंधन पद्धतियाँ जारी रखें।",
            "or": "ଫସଲ ସୁସ୍ଥ ଦେଖାଯାଉଛି। ନିୟମିତ ନିରୀକ୍ଷଣ ଏବଂ ଭଲ ଫସଲ ପରିଚାଳନା ଜାରି ରଖନ୍ତୁ।",
        }.get(language)
    if any(word in condition_key for word in [
        "rust", "mildew", "blight", "scab", "rot", "spot",
        "septoria", "esca", "cercospora", "target"
    ]):
        return {
            "en": "Separate or remove badly affected plant material where appropriate, avoid prolonged leaf wetness, and follow locally recommended disease-management guidance.",
            "hi": "जहाँ उचित हो वहाँ बहुत प्रभावित पौधों के हिस्सों को अलग या हटाएँ, पत्तियों पर लंबे समय तक नमी से बचें और स्थानीय रोग-प्रबंधन सलाह का पालन करें।",
            "or": "ଯେଉଁଠାରେ ଉଚିତ ସେଠାରେ ଅଧିକ ପ୍ରଭାବିତ ଉଦ୍ଭିଦ ଅଂଶକୁ ଅଲଗା କିମ୍ବା ହଟାନ୍ତୁ, ପତ୍ରରେ ଦୀର୍ଘ ସମୟ ଆର୍ଦ୍ରତା ରହିବାରୁ ବଞ୍ଚନ୍ତୁ ଏବଂ ସ୍ଥାନୀୟ ରୋଗ ପରିଚାଳନା ପରାମର୍ଶ ଅନୁସରଣ କରନ୍ତୁ।",
        }.get(language)
    if any(word in condition_key for word in [
        "bacterial", "virus", "viral", "tungro", "yellow_leaf_curl"
    ]):
        return {
            "en": "Use clean planting material, remove clearly infected material where appropriate, and follow locally recommended disease and vector-management guidance.",
            "hi": "स्वच्छ रोपण सामग्री का उपयोग करें, जहाँ उचित हो स्पष्ट रूप से संक्रमित हिस्सों को हटाएँ और स्थानीय रोग तथा वाहक-कीट प्रबंधन सलाह का पालन करें।",
            "or": "ସ୍ୱଚ୍ଛ ରୋପଣ ସାମଗ୍ରୀ ବ୍ୟବହାର କରନ୍ତୁ, ଯେଉଁଠାରେ ଉଚିତ ସେଠାରେ ସ୍ପଷ୍ଟ ଭାବେ ସଂକ୍ରମିତ ଅଂଶକୁ ହଟାନ୍ତୁ ଏବଂ ସ୍ଥାନୀୟ ରୋଗ ଓ ବାହକ-କୀଟ ପରିଚାଳନା ପରାମର୍ଶ ଅନୁସରଣ କରନ୍ତୁ।",
        }.get(language)
    if any(word in condition_key for word in ["hispa", "spider", "mite", "dead_heart"]):
        return {
            "en": "Inspect the crop regularly for pest activity and follow integrated pest-management guidance appropriate for your area.",
            "hi": "कीटों की गतिविधि के लिए फसल की नियमित जाँच करें और अपने क्षेत्र के अनुसार समेकित कीट प्रबंधन सलाह का पालन करें।",
            "or": "କୀଟପତଙ୍ଗର ଉପସ୍ଥିତି ପାଇଁ ଫସଲକୁ ନିୟମିତ ଯାଞ୍ଚ କରନ୍ତୁ ଏବଂ ନିଜ ଅଞ୍ଚଳ ପାଇଁ ଉପଯୁକ୍ତ ସମନ୍ୱିତ କୀଟ ପରିଚାଳନା ପରାମର୍ଶ ଅନୁସରଣ କରନ୍ତୁ।",
        }.get(language)
    return {
        "en": "Recheck the image in good lighting and confirm the result with a qualified agricultural expert before treatment decisions.",
        "hi": "अच्छी रोशनी में तस्वीर दोबारा जाँचें और उपचार का निर्णय लेने से पहले योग्य कृषि विशेषज्ञ से परिणाम की पुष्टि करें।",
        "or": "ଭଲ ଆଲୋକରେ ଛବିକୁ ପୁନଃ ଯାଞ୍ଚ କରନ୍ତୁ ଏବଂ ଚିକିତ୍ସା ନିଷ୍ପତ୍ତି ପୂର୍ବରୁ ଯୋଗ୍ୟ କୃଷି ବିଶେଷଜ୍ଞଙ୍କଠାରୁ ଫଳାଫଳ ନିଶ୍ଚିତ କରନ୍ତୁ।",
    }.get(language)
# ============================================================
# LOAD MODEL
# ============================================================
@st.cache_resource
def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model not found:\n{MODEL_PATH}"
        )
    return YOLO(
        str(MODEL_PATH)
    )
try:
    model = load_model()
except Exception as error:
    st.error("❌ Model could not be loaded.")
    st.code(str(error))
    st.stop()
# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    language_name = st.selectbox("🌐 Language", list(LANGUAGES.keys()))
    language = LANGUAGES[language_name]
    T = UI_TEXT[language]
    st.title(T["app"])
    st.divider()
    st.write(T["sidebar"])
# ============================================================
# MAIN TITLE
# ============================================================
st.title(T["app"])
st.write(T["intro"])
# ============================================================
# IMAGE UPLOAD
# ============================================================
st.header(T["upload"])
uploaded_file = st.file_uploader(
    T["upload_help"],
    type=[
        "jpg",
        "jpeg",
        "png",
        "webp"
    ]
)
# Image source: uploaded file only. Camera input is intentionally disabled.
image_source = uploaded_file
# ============================================================
# WAIT FOR IMAGE
# ============================================================
if image_source is None:
    st.info(T["waiting"])
    st.stop()
# ============================================================
# OPEN IMAGE
# ============================================================
image = Image.open(
    image_source
).convert("RGB")
# ============================================================
# IMAGE + RESULT COLUMNS
# ============================================================
image_col, result_col = st.columns(
    [1.15, 0.85],
    gap="large"
)
with image_col:
    st.image(
        image,
        caption=T["uploaded"],
        use_container_width=True
    )
# ============================================================
# BASIC IMAGE QUALITY CHECK
# ============================================================
image_width, image_height = image.size
if image_width < 224 or image_height < 224:
    st.warning(
        f"⚠️ Image resolution is {image_width}×{image_height}. "
        "For better results, use a clearer and larger crop/leaf image."
    )
# ============================================================
# AI PREDICTION
# ============================================================
with st.spinner(T["running"]):
    results = model.predict(
        source=image,
        verbose=False
    )
result = results[0]
probabilities = result.probs
# ============================================================
# TOP PREDICTION
# ============================================================
top1_index = int(
    probabilities.top1
)
confidence = float(
    probabilities.top1conf
)
class_name = model.names[
    top1_index
]
crop = get_crop_name(
    class_name
)
condition = get_condition_name(
    class_name
)
crop_display = translated_crop(
    crop
)
condition_display = readable_condition(
    condition
)

# ============================================================
# SERPAPI AGRICULTURAL SEARCH
# ============================================================

try:
    agri_sources = cached_agriculture_search(
        crop.replace("_", " "),
        condition.replace("_", " ")
    )
except Exception as e:
    agri_sources = []
    agri_search_error = str(e)
else:
    agri_search_error = ""

# ============================================================
# RESULT
# ============================================================
with result_col:
    st.subheader(T["result"])
    st.metric(
        T["crop"],
        crop_display
    )
    st.metric(
        T["condition"],
        condition_display
    )
    st.metric(
        T["confidence"],
        f"{confidence * 100:.2f}%"
    )
# ============================================================
# CONFIDENCE
# ============================================================
st.divider()
st.header(T["confidence_title"])
st.progress(
    confidence
)
if confidence >= 0.80:
    st.success(
        f"{T['high']} — {confidence * 100:.2f}%"
    )
elif confidence >= 0.50:
    st.warning(
        f"{T['moderate']} — {confidence * 100:.2f}%"
    )
else:
    st.error(
        f"{T['low']} — {confidence * 100:.2f}%"
    )
# ============================================================
# SAME CROP PREDICTIONS
# ============================================================
st.divider()
st.header(T["other"])
probability_array = (
    probabilities.data.cpu().numpy()
)
same_crop_predictions = []
for index, probability in enumerate(
    probability_array
):
    current_class = model.names[index]
    current_crop = get_crop_name(
        current_class
    )
    if current_crop == crop:
        same_crop_predictions.append(
            (
                current_class,
                float(probability)
            )
        )
same_crop_predictions.sort(
    key=lambda item: item[1],
    reverse=True
)
top_predictions = (
    same_crop_predictions[:5]
)
prediction_columns = st.columns(
    len(top_predictions)
)
for column, (
    prediction_class,
    probability
) in zip(
    prediction_columns,
    top_predictions
):
    prediction_condition = readable_condition(
        get_condition_name(
            prediction_class
        )
    )
    with column:
        st.metric(
            prediction_condition,
            f"{probability * 100:.2f}%"
        )
CROP_NAMES = {
    "en": {},
    "hi": {
        "Apple": "सेब", "Blueberry": "ब्लूबेरी", "Cherry_(including_sour)": "चेरी",
        "Corn_(maize)": "मक्का", "Grape": "अंगूर", "Orange": "संतरा",
        "Paddy": "धान / चावल", "Peach": "आड़ू", "Pepper,_bell": "शिमला मिर्च",
        "Potato": "आलू", "Raspberry": "रास्पबेरी", "Soybean": "सोयाबीन",
        "Squash": "स्क्वैश", "Strawberry": "स्ट्रॉबेरी", "Tomato": "टमाटर", "Wheat": "गेहूं",
    },
    "or": {
        "Apple": "ସେଓ", "Blueberry": "ବ୍ଲୁବେରି", "Cherry_(including_sour)": "ଚେରି",
        "Corn_(maize)": "ମକା", "Grape": "ଅଙ୍ଗୁର", "Orange": "କମଳା",
        "Paddy": "ଧାନ / ଚାଉଳ", "Peach": "ପିଚ୍", "Pepper,_bell": "କ୍ୟାପ୍ସିକମ୍",
        "Potato": "ଆଳୁ", "Raspberry": "ରାସ୍ପବେରି", "Soybean": "ସୋୟାବିନ୍",
        "Squash": "ସ୍କ୍ୱାଶ୍", "Strawberry": "ଷ୍ଟ୍ରବେରି", "Tomato": "ଟମାଟୋ", "Wheat": "ଗହମ",
    },
}
CONDITION_NAMES = {
    "hi": {
        "healthy": "स्वस्थ", "normal": "सामान्य", "bacterial leaf blight": "बैक्टीरियल लीफ ब्लाइट",
        "bacterial leaf streak": "बैक्टीरियल लीफ स्ट्रीक", "bacterial panicle blight": "बैक्टीरियल पैनिकल ब्लाइट",
        "blast": "ब्लास्ट", "brown spot": "ब्राउन स्पॉट", "dead heart": "डेड हार्ट",
        "downy mildew": "डाउनी मिल्ड्यू", "hispa": "हिस्पा", "tungro": "टुंग्रो",
        "powdery mildew": "पाउडरी मिल्ड्यू", "leaf rust": "लीफ रस्ट", "stem rust": "स्टेम रस्ट",
        "yellow rust": "येलो रस्ट", "septoria": "सेप्टोरिया", "black rot": "ब्लैक रॉट",
        "apple scab": "एप्पल स्कैब", "cedar apple rust": "सीडर एप्पल रस्ट",
    },
    "or": {
        "healthy": "ସୁସ୍ଥ", "normal": "ସାଧାରଣ", "bacterial leaf blight": "ବ୍ୟାକ୍ଟେରିଆଲ୍ ଲିଫ୍ ବ୍ଲାଇଟ୍",
        "bacterial leaf streak": "ବ୍ୟାକ୍ଟେରିଆଲ୍ ଲିଫ୍ ଷ୍ଟ୍ରିକ୍", "bacterial panicle blight": "ବ୍ୟାକ୍ଟେରିଆଲ୍ ପାନିକଲ୍ ବ୍ଲାଇଟ୍",
        "blast": "ବ୍ଲାଷ୍ଟ", "brown spot": "ବ୍ରାଉନ୍ ସ୍ପଟ୍", "dead heart": "ଡେଡ୍ ହାର୍ଟ",
        "downy mildew": "ଡାଉନି ମିଲଡିଉ", "hispa": "ହିସ୍ପା", "tungro": "ଟୁଙ୍ଗ୍ରୋ",
        "powdery mildew": "ପାଉଡରି ମିଲଡିଉ", "leaf rust": "ଲିଫ୍ ରଷ୍ଟ", "stem rust": "ଷ୍ଟେମ୍ ରଷ୍ଟ",
        "yellow rust": "ୟେଲୋ ରଷ୍ଟ", "septoria": "ସେପ୍ଟୋରିଆ", "black rot": "ବ୍ଲାକ୍ ରଟ୍",
        "apple scab": "ଆପଲ୍ ସ୍କାବ୍", "cedar apple rust": "ସିଡାର୍ ଆପଲ୍ ରଷ୍ଟ",
    },
}
WHEAT_INFO = {
    "Wheat___healthy": ("The model classified the wheat plant as healthy.", "No major disease pattern from the trained Wheat classes was detected.", "Continue regular field monitoring and good crop-management practices."),
    "Wheat___leaf_rust": ("A fungal disease affecting wheat leaves.", "Small rust-colored pustules may appear on leaf surfaces.", "Follow locally recommended resistant varieties and disease-management practices."),
    "Wheat___stem_rust": ("A fungal disease affecting wheat stems and leaves.", "Reddish-brown rust pustules may develop on stems and leaves.", "Monitor fields and follow locally recommended disease-management practices."),
    "Wheat___yellow_rust": ("A fungal disease affecting wheat foliage.", "Yellow or orange-yellow rust pustules may form in stripes on leaves.", "Monitor fields and follow locally recommended disease-management guidance."),
    "Wheat___powdery_mildew": ("A fungal disease affecting wheat foliage.", "White powder-like fungal growth may appear on leaf surfaces.", "Follow locally recommended disease-management practices."),
    "Wheat___septoria": ("A fungal disease affecting wheat leaves.", "Dark or brown leaf lesions may develop on affected leaves.", "Follow locally recommended disease-management practices."),
}
# ============================================================
# DISEASE INFORMATION
# ============================================================
st.divider()
st.header(T["info"])
information = DISEASE_INFO.get(
    class_name
)
if information is None and class_name in WHEAT_INFO:
    description, symptoms, management = WHEAT_INFO[class_name]
    information = {
        "description": description,
        "symptoms": symptoms,
        "management": management,
    }
if information is None:
    information = {
        "description":
            "The image was classified into "
            "one of the trained crop conditions.",
        "symptoms":
            "The visual characteristics correspond "
            "to the selected trained category.",
        "management":
            "Confirm the result with an agricultural "
            "expert before taking treatment decisions."
    }
st.subheader(
    f"{crop_display} — {condition_display}"
)
st.write(f"**{T['description']}**")
st.write(
    information["description"]
)
st.write(f"**{T['symptoms']}**")
st.write(
    information["symptoms"]
)
st.write(f"**{T['management']}**")
st.write(
    information["management"]
)

# ============================================================
# SMART AGRICULTURAL SOURCE FILTERING
# ============================================================

HIGH_TRUST_DOMAINS = (
    "icar.gov.in", "icar.org.in", "gov.in", ".gov",
    ".edu", ".edu.in", ".ac.in", "fao.org",
    "who.int", "pubmed.ncbi.nlm.nih.gov", "ncbi.nlm.nih.gov",
)

MEDIUM_TRUST_DOMAINS = (
    "extension.", "university.", "cornell.edu",
    "ucanr.edu", "psu.edu", "msu.edu",
    "umn.edu", "iastate.edu",
)

LOW_TRUST_DOMAINS = (
    "facebook.com", "instagram.com", "pinterest.com",
    "youtube.com", "houzz.com", "scribd.com",
    "academia.edu",
)

EXCLUDED_RESULT_TERMS = (
    "fungicide product", "buy fungicide", "buy pesticide",
    "shop", "price", "amazon", "flipkart",
)

def _source_domain(url):
    try:
        return urlparse(url).netloc.lower().replace("www.", "")
    except Exception:
        return ""

def _source_relevance(source, crop, condition):
    title = str(source.get("title", "")).lower()
    snippet = str(source.get("snippet", "")).lower()
    link = str(source.get("link", "")).lower()
    domain = _source_domain(link)
    text = f"{title} {snippet}"

    crop_name = crop.lower().replace("_", " ")
    condition_name = condition.lower().replace("_", " ")

    score = 0

    # The detected disease must appear in the result.
    if condition_name in title:
        score += 12
    elif condition_name in snippet:
        score += 7
    else:
        return -100

    # The detected crop should also appear.
    if crop_name in title:
        score += 7
    elif crop_name in snippet:
        score += 4

    useful_terms = (
        "management", "prevention", "control", "symptoms",
        "disease", "pathology", "extension", "integrated",
        "sanitation", "resistant", "monitoring"
    )
    score += min(6, sum(1 for term in useful_terms if term in text))

    if any(domain == x or domain.endswith(x) or x in domain
           for x in HIGH_TRUST_DOMAINS):
        score += 12
    elif any(x in domain for x in MEDIUM_TRUST_DOMAINS):
        score += 7

    if any(x in domain for x in LOW_TRUST_DOMAINS):
        score -= 30

    if any(term in text for term in EXCLUDED_RESULT_TERMS):
        score -= 20

    return score



def build_management_suggestions(crop, condition, sources):
    """Create conservative, source-backed action suggestions from search snippets."""
    condition_text = condition.replace("_", " ").lower()
    crop_text = crop.replace("_", " ").lower()

    combined = " ".join(
        f"{item.get('title', '')} {item.get('snippet', '')}"
        for item in (sources or [])
    ).lower()

    suggestions = []

    if any(term in combined for term in ("remove fallen leaves", "leaf cleanup", "leaf decomposition")):
        suggestions.append(
            "Clean up infected or fallen leaves and plant debris where appropriate; "
            "reducing overwintering inoculum can lower disease pressure."
        )

    if any(term in combined for term in ("prune", "pruning", "open canopy", "air movement")):
        suggestions.append(
            "Prune appropriately to improve air movement and help foliage dry faster."
        )

    if any(term in combined for term in ("resistant varieties", "resistant cultivar", "disease-resistant")):
        suggestions.append(
            "Use disease-resistant varieties when they are available for the crop."
        )

    if any(term in combined for term in ("fungicide", "fungicides", "spray", "sprays")):
        suggestions.append(
            "Fungicide programs may be part of management for some diseases, but "
            "the product, dose, timing, crop, and local regulations must be checked "
            "on the current product label and local agricultural guidance."
        )

    if any(term in combined for term in ("monitor", "weather", "rain", "leaf wetness", "humidity")):
        suggestions.append(
            "Monitor weather and crop conditions because moisture and disease-development "
            "conditions can affect management timing."
        )

    if not suggestions:
        suggestions.append(
            f"Monitor the {crop_text} crop closely, remove clearly affected material "
            "where appropriate, and follow locally recommended integrated disease-management practices."
        )

    return suggestions[:5]

def rank_agriculture_sources(sources, crop, condition):
    ranked = []
    seen_links = set()

    for source in sources or []:
        link = str(source.get("link", "")).strip()
        if not link or link in seen_links:
            continue

        seen_links.add(link)
        score = _source_relevance(source, crop, condition)

        if score < 8:
            continue

        item = dict(source)
        item["_relevance_score"] = score
        item["_domain"] = _source_domain(link)
        ranked.append(item)

    ranked.sort(key=lambda item: item["_relevance_score"], reverse=True)
    return ranked[:3]


# ============================================================
# CURRENT AGRICULTURAL INFORMATION — SERPAPI
# ============================================================

st.divider()

# ============================================================
# ACTIONABLE MANAGEMENT SUGGESTIONS
# ============================================================

st.subheader("🌾 What you can do")

management_suggestions = build_management_suggestions(
    crop,
    condition,
    agri_sources
)

for suggestion in management_suggestions:
    st.markdown(f"- {suggestion}")

st.caption(
    "These suggestions are summarized from the retrieved agricultural sources. "
    "For pesticide or fungicide use, always follow the current product label "
    "and local agricultural recommendations."
)

st.header("🌐 Current Agricultural Information")
st.caption(
    "Current web references retrieved through SerpApi. "
    "Use these sources for further reading and verify management decisions "
    "with qualified agricultural guidance."
)

if agri_search_error:
    st.warning(
        "SerpApi search could not be completed right now. "
        "Check your SERPAPI_KEY and internet connection."
    )
elif agri_sources:
    for index, source in enumerate(agri_sources[:6], start=1):
        title = source.get("title") or "Untitled source"
        snippet = source.get("snippet") or "No description available."
        link = source.get("link") or ""
        domain = source_domain(link)

        with st.container(border=True):
            st.markdown(f"**{index}. {title}**")
            if domain:
                st.caption(f"Source: {domain}")
            st.write(snippet)
            if link:
                st.link_button("🔗 Open source", link)
else:
    st.info(
        "No current agricultural sources were returned for this prediction."
    )

# ============================================================
# FARMER GUIDANCE + VOICE
# ============================================================
st.divider()
st.header(T["farmer_action"])
action_text = farmer_action(class_name)
st.info(action_text)
voice_text = (
    f"{crop_display}. {condition_display}. "
    f"{information['description']} "
    f"{information['symptoms']} "
    f"{action_text}"
)
if st.button(T["listen"], use_container_width=False):
    speak_result(voice_text)
# ============================================================
# DISCLAIMER
# ============================================================
st.divider()
st.warning(T["disclaimer"])
# ============================================================
# FOOTER
# ============================================================
st.divider()
st.caption(
    "🌱 AI Crop Disease Detector"
)