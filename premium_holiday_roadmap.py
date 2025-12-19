import streamlit as st
import pandas as pd
import base64
import os

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="FinBox Holiday Calendar 2026", 
    page_icon="🗓️", 
    layout="wide"
)

# -----------------------------
# CONFIGURATION
# -----------------------------
# CHANGE THIS TO YOUR BACKGROUND IMAGE FILENAME
bg_image_filename = "background.jpg" 

# -----------------------------
# HELPER: LOAD IMAGE SAFELY
# -----------------------------
def get_base64_image(image_path):
    """Converts a local image file to a Base64 string for HTML embedding."""
    if not os.path.exists(image_path):
        return None
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# -----------------------------
# 1. DATA ENTRY
# -----------------------------
raw_data = [
    {"Date": "01-Jan-26", "Name": "New Year", "Day": "Thursday", "ImageFile": "new_year.png", "Bangalore": True, "Mumbai": True, "Gurgaon": True},
    {"Date": "15-Jan-26", "Name": "Makara Sankranti", "Day": "Thursday", "ImageFile": "makara_sankranti.jpg", "Bangalore": True, "Mumbai": True, "Gurgaon": True},
    {"Date": "26-Jan-26", "Name": "Republic Day", "Day": "Monday", "ImageFile": "republic_day.jpg", "Bangalore": True, "Mumbai": True, "Gurgaon": True},
    {"Date": "04-Mar-26", "Name": "Holi", "Day": "Wednesday", "ImageFile": "holi.jpg", "Bangalore": True, "Mumbai": True, "Gurgaon": True},
    {"Date": "19-Mar-26", "Name": "Ugadi / Gudhi Padwa", "Day": "Thursday", "ImageFile": "ugadi.jpg", "Bangalore": True, "Mumbai": True, "Gurgaon": False},
    {"Date": "03-Apr-26", "Name": "Good Friday", "Day": "Friday", "ImageFile": "good_friday.jpg", "Bangalore": True, "Mumbai": True, "Gurgaon": True},
    {"Date": "01-May-26", "Name": "May Day", "Day": "Friday", "ImageFile": "may_day.jpg", "Bangalore": True, "Mumbai": True, "Gurgaon": True},
    {"Date": "28-May-26", "Name": "Bakrid", "Day": "Thursday", "ImageFile": "bakrid.jpg", "Bangalore": True, "Mumbai": True, "Gurgaon": True},
    {"Date": "21-Aug-26", "Name": "Varamahalakshmi Vrata", "Day": "Friday", "ImageFile": "varamahalakshmi.jpg", "Bangalore": True, "Mumbai": False, "Gurgaon": False},
    {"Date": "28-Aug-26", "Name": "Raksha Bandhan", "Day": "Friday", "ImageFile": "raksha_bandhan.jpg", "Bangalore": False, "Mumbai": True, "Gurgaon": True},
    {"Date": "14-Sep-26", "Name": "Ganesh Chaturthi", "Day": "Monday", "ImageFile": "ganesh_chaturthi.jpg", "Bangalore": True, "Mumbai": True, "Gurgaon": True},
    {"Date": "02-Oct-26", "Name": "Gandhi Jayanthi", "Day": "Friday", "ImageFile": "gandhi_jayanthi.jpg", "Bangalore": True, "Mumbai": True, "Gurgaon": True},
    {"Date": "20-Oct-26", "Name": "Dussehra", "Day": "Tuesday", "ImageFile": "dussehra.jpg", "Bangalore": True, "Mumbai": True, "Gurgaon": True},
    {"Date": "09-Nov-26", "Name": "Diwali", "Day": "Monday", "ImageFile": "diwali.jpg", "Bangalore": True, "Mumbai": True, "Gurgaon": True},
    {"Date": "10-Nov-26", "Name": "Diwali", "Day": "Tuesday", "ImageFile": "diwali.jpg", "Bangalore": True, "Mumbai": True, "Gurgaon": True},
    {"Date": "24-Nov-26", "Name": "Guru Nanak’s Birthday", "Day": "Tuesday", "ImageFile": "guru_nanak.jpg", "Bangalore": False, "Mumbai": False, "Gurgaon": True},
    {"Date": "25-Dec-26", "Name": "Christmas", "Day": "Friday", "ImageFile": "christmas.jpg", "Bangalore": True, "Mumbai": True, "Gurgaon": True},
]

df = pd.DataFrame(raw_data)

# -----------------------------
# 2. BACKGROUND IMAGE LOGIC
# -----------------------------
bg_img_b64 = get_base64_image(bg_image_filename)

if bg_img_b64:
    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bg_img_b64}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """
else:
    # Fallback if image not found
    page_bg_img = """
    <style>
    .stApp {
        background-color: #F7F9FC;
    }
    </style>
    """

# -----------------------------
# 3. FINBOX BRANDING CSS
# -----------------------------
finbox_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

.stApp {
    font-family: 'Inter', sans-serif;
}

/* Header */
.brand-header {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    margin-bottom: 50px;
    padding-top: 20px;
}
.brand-logo {
    width: 250px; 
    margin-bottom: 20px;
}
.page-title {
    font-size: 36px;
    font-weight: 800;
    color: #0F172A;
    text-shadow: 2px 2px 4px rgba(255,255,255,0.8); /* Added shadow for readability */
    letter-spacing: -0.5px;
}
.page-subtitle {
    color: #334155; /* Darker for better contrast against bg */
    font-size: 18px;
    font-weight: 600;
    margin-top: 5px;
    text-shadow: 1px 1px 2px rgba(255,255,255,0.8);
}

/* Timeline Container */
.timeline {
    position: relative;
    max-width: 1000px; 
    margin: 0 auto;
    padding: 20px 0;
}
.timeline::after {
    content: '';
    position: absolute;
    width: 2px;
    background: #94A3B8; /* Darker line for visibility */
    top: 0;
    bottom: 0;
    left: 50%;
    margin-left: -1px;
}

/* Card Container */
.container-box {
    padding: 15px 50px;
    position: relative;
    background-color: transparent;
    width: 50%;
    box-sizing: border-box;
}
.left { left: 0; }
.right { left: 50%; }

/* Dots */
.container-box::after {
    content: '';
    position: absolute;
    width: 14px;
    height: 14px;
    right: -7px;
    background-color: #fff;
    border: 3px solid #2E5CFF;
    top: 50%;
    transform: translateY(-50%);
    border-radius: 50%;
    z-index: 10;
    box-shadow: 0 0 0 4px #DBEAFE;
}
.right::after { left: -7px; }

/* --- CARD LAYOUT --- */
.content {
    background: rgba(255, 255, 255, 0.95); /* High opacity white background */
    border-radius: 12px;
    border: 1px solid #E2E8F0;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    padding: 16px;
}

.content:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.15);
    border-color: #BFDBFE;
}

/* Text Area */
.text-area {
    flex: 1;
    text-align: left;
    padding-right: 15px;
}

/* Image Styling */
.card-img {
    width: 150px;
    height: 150px;
    border-radius: 10px;
    object-fit: cover;
    flex-shrink: 0;
    background-color: #f8fafc;
}

/* Typography */
.date-badge {
    display: inline-block;
    padding: 5px 10px;
    background: #EFF6FF;
    color: #2E5CFF;
    border-radius: 6px;
    font-size: 20px;
    font-weight: 700;
    text-transform: uppercase;
    margin-bottom: 8px;
    letter-spacing: 0.5px;
}
.holiday-name {
    font-size: 30px;
    font-weight: 700;
    color: #1E293B;
    margin-bottom: 4px;
    line-height: 1.2;
}
.holiday-day {
    font-size: 20px;
    color: #64748B;
    font-weight: 500;
}

/* Mobile Responsiveness */
@media screen and (max-width: 700px) {
    .timeline::after { left: 31px; }
    .container-box { width: 100%; padding-left: 70px; padding-right: 25px; }
    .container-box::after { left: 24px; }
    .right { left: 0%; }
}
</style>
"""

# Inject Background + CSS
st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown(finbox_css, unsafe_allow_html=True)

# -----------------------------
# 4. HEADER WITH LOGO
# -----------------------------
logo_filename = "FinBox Logo with wordmark.png"
logo_b64 = get_base64_image(logo_filename)

if logo_b64:
    logo_html = f'<img src="data:image/png;base64,{logo_b64}" class="brand-logo">'
else:
    logo_html = f'<div style="color:red;font-weight:bold;">⚠️ {logo_filename} Not Found</div>'

st.markdown(f"""
<div class="brand-header">
    {logo_html}
    <div class="page-title">Holiday Calendar 2026</div>
    <div class="page-subtitle">People & Culture • FinBox</div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# 5. FILTER
# -----------------------------
col1, col2, col3 = st.columns([3, 2, 3])
with col2:
    locations = ["Bangalore", "Mumbai", "Gurgaon"]
    selected_loc = st.selectbox("", locations, index=0)

filtered_df = df[df[selected_loc] == True].reset_index(drop=True)

# -----------------------------
# 6. TIMELINE RENDER
# -----------------------------
def parse_date(date_str):
    parts = date_str.split("-")
    if len(parts) == 3:
        return parts[0], parts[1], "20" + parts[2]
    return date_str, "", ""

timeline_html = '<div class="timeline">'

for i, row in filtered_df.iterrows():
    day_num, month, year = parse_date(row["Date"])
    name = row["Name"]
    day = row["Day"]
    
    # Image Handling
    fname = row["ImageFile"]
    img_b64 = get_base64_image(fname)
    
    if img_b64:
        img_tag = f'<img src="data:image/png;base64,{img_b64}" class="card-img">'
    else:
        img_tag = '<div class="card-img" style="display:flex;align-items:center;justify-content:center;color:#cbd5e1;">IMG</div>'
    
    pos = "left" if i % 2 == 0 else "right"
    
    timeline_html += f"""
<div class="container-box {pos}">
    <div class="content">
        <div class="text-area">
            <div class="date-badge">{day_num} {month} {year}</div>
            <div class="holiday-name">{name}</div>
            <div class="holiday-day">{day}</div>
        </div>
        {img_tag}
    </div>
</div>
"""

timeline_html += '</div>'

st.markdown(timeline_html, unsafe_allow_html=True)

# -----------------------------
# 7. NOTES & FOOTER
# -----------------------------
# Note: Added a white background wrapper around the notes so they are readable over the image.
st.markdown("""
<div style="max-width: 1000px; margin: 20px auto; padding: 20px 50px; background: rgba(255,255,255,0.9); border-radius: 12px; border: 1px solid #E2E8F0;">
    <div style="font-weight: 800; font-size: 20px; margin-bottom: 10px; color: #0F172A;">Note</div>
    <ul style="color: #DC2626; font-weight: 600; font-size: 16px; line-height: 1.8;">
        <li>Holidays that fall on Saturdays or Sundays are not included in this list.</li>
        <li>Ramzan and Bakrid dates may vary based on moon sighting confirmation by the religious authorities.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; margin-top:40px; margin-bottom: 40px; color:#475569; font-size:13px; font-weight:600; text-shadow: 1px 1px 2px rgba(255,255,255,0.8);">
    Confidential • FinBox Internal Use Only
</div>
""", unsafe_allow_html=True)
