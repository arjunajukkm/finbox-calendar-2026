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
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------
# CONFIGURATION
# -----------------------------
bg_image_filename = "background.jpg" 

# -----------------------------
# HELPER FUNCTIONS
# -----------------------------
def get_base64_image(image_path):
    if not os.path.exists(image_path):
        return None
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def parse_date(date_str):
    parts = date_str.split("-")
    if len(parts) == 3:
        return parts[0], parts[1], "20" + parts[2]
    return date_str, "", ""

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
# 2. BACKGROUND & STYLES
# -----------------------------
bg_img_b64 = get_base64_image(bg_image_filename)
bg_css = f"""background-image: url("data:image/png;base64,{bg_img_b64}");""" if bg_img_b64 else "background-color: #F8FAFC;"

finbox_css = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

.stApp {{
    font-family: 'Inter', sans-serif;
    {bg_css}
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* --- BRANDING HEADER --- */
.brand-header {{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-bottom: 3rem;
    padding-top: 1rem;
    text-align: center;
}}

.brand-logo {{
    width: 250px;
    max-width: 60vw; /* Scales down on mobile but caps at 250px */
    height: auto;
    margin-bottom: 1.5rem;
}}

.page-title {{
    /* FLUID TYPOGRAPHY: Scales smoothly between 24px and 40px depending on screen width */
    font-size: clamp(1.5rem, 5vw, 2.5rem); 
    font-weight: 800;
    color: #0F172A;
    text-shadow: 2px 2px 4px rgba(255,255,255,0.8);
    line-height: 1.1;
}}

.page-subtitle {{
    font-size: clamp(0.9rem, 3vw, 1.2rem);
    color: #334155;
    font-weight: 600;
    margin-top: 0.5rem;
    text-shadow: 1px 1px 2px rgba(255,255,255,0.8);
}}

/* --- TIMELINE CONTAINER --- */
.timeline {{
    position: relative;
    width: 95%;
    max-width: 1100px;
    margin: 0 auto;
    padding: 20px 0;
}}

/* The Vertical Line */
.timeline::after {{
    content: '';
    position: absolute;
    width: 3px;
    background: #94A3B8;
    top: 0;
    bottom: 0;
    left: 50%;
    margin-left: -1px;
    transition: left 0.3s ease; /* Smooth transition if resized */
}}

/* --- CARD WRAPPERS --- */
.container-box {{
    padding: 10px 40px;
    position: relative;
    background-color: transparent;
    width: 50%;
    box-sizing: border-box;
}}

.left {{ left: 0; }}
.right {{ left: 50%; }}

/* The Dots on the Timeline */
.container-box::after {{
    content: '';
    position: absolute;
    width: 16px;
    height: 16px;
    right: -9px;
    background-color: #fff;
    border: 4px solid #2E5CFF;
    top: 50%;
    transform: translateY(-50%);
    border-radius: 50%;
    z-index: 10;
    box-shadow: 0 0 0 4px #DBEAFE;
}}
.right::after {{ left: -9px; }}

/* --- CARD CONTENT (FLUID FLEXBOX) --- */
.content {{
    background: rgba(255, 255, 255, 0.95);
    border-radius: 12px;
    border: 1px solid #E2E8F0;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    
    /* Auto-Layout: Flex row puts text and image side by side */
    display: flex; 
    flex-direction: row; 
    align-items: center;
    justify-content: space-between;
    padding: 1.2rem;
    gap: 15px; /* Space between text and image */
    
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}}

.content:hover {{
    transform: translateY(-3px);
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.15);
    border-color: #BFDBFE;
}}

/* --- TEXT AREA --- */
.text-area {{
    flex: 1; /* Takes up all available space not used by image */
    min-width: 0; /* Important for flex text wrapping */
    display: flex;
    flex-direction: column;
    justify-content: center;
}}

/* FLUID TEXT SIZING */
.date-badge {{
    display: inline-block;
    width: fit-content;
    padding: 6px 10px;
    background: #EFF6FF;
    color: #2E5CFF;
    border-radius: 6px;
    font-size: clamp(0.75rem, 1.5vw, 1rem); /* Fluid Font */
    font-weight: 700;
    text-transform: uppercase;
    margin-bottom: 6px;
}}

.holiday-name {{
    font-size: clamp(1.1rem, 2.5vw, 1.8rem); /* Fluid Font: Scales with card width */
    font-weight: 700;
    color: #1E293B;
    line-height: 1.2;
    margin-bottom: 4px;
}}

.holiday-day {{
    font-size: clamp(0.9rem, 2vw, 1.2rem); /* Fluid Font */
    color: #64748B;
    font-weight: 500;
}}

/* --- FLUID IMAGES --- */
.card-img {{
    /* The image tries to be 30% of the card, but never wider than 140px, never smaller than 90px */
    width: 30%; 
    max-width: 140px; 
    min-width: 90px; 
    aspect-ratio: 1 / 1; /* Keeps it square */
    border-radius: 8px;
    object-fit: cover;
    background-color: #f1f5f9;
    flex-shrink: 0; /* Prevents image from squishing if text is long */
}}

/* --- FOOTER --- */
.footer-note {{
    width: 90%;
    max-width: 1000px;
    margin: 3rem auto;
    padding: 1.5rem;
    background: rgba(255,255,255,0.9);
    border-radius: 12px;
    border: 1px solid #E2E8F0;
}}

/* ----------------------------------------------------------- */
/* RESPONSIVE LOGIC (LAYOUT SHIFT ONLY)                        */
/* ----------------------------------------------------------- */
/* We keep the sizing fluid above, but when the screen is physically 
   too narrow (tablets/phones), we must shift from 2 columns to 1 column.
*/
@media screen and (max-width: 768px) {{
    /* Move vertical line to left */
    .timeline::after {{ left: 25px; }}
    
    /* Stack cards on the right */
    .container-box {{ 
        width: 100%; 
        padding-left: 60px; /* Make room for the line/dots */
        padding-right: 10px; 
    }}
    
    /* Align dots to left line */
    .container-box::after {{ left: 16px; }}
    
    /* Reset left/right positioning to default */
    .left, .right {{ left: 0; }}
    
    /* On very small phones, stack content vertically inside the card */
    @media (max-width: 400px) {{
        .content {{
            flex-direction: column-reverse; /* Image on top */
            text-align: center;
        }}
        .text-area {{ align-items: center; }}
        .card-img {{ width: 100%; max-width: 100%; height: 150px; }}
    }}
}}
</style>
"""

# Inject CSS
st.markdown(finbox_css, unsafe_allow_html=True)

# -----------------------------
# 3. HEADER
# -----------------------------
logo_filename = "FinBox Logo with wordmark.png"
logo_b64 = get_base64_image(logo_filename)

if logo_b64:
    logo_html = f'<img src="data:image/png;base64,{logo_b64}" class="brand-logo">'
else:
    logo_html = f'<div style="color:red;font-weight:bold;margin-bottom:10px;">⚠️ Logo Not Found</div>'

st.markdown(f"""
<div class="brand-header">
    {logo_html}
    <div class="page-title">Holiday Calendar 2026</div>
    <div class="page-subtitle">People & Culture • FinBox</div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# 4. CONTROLS (FILTER)
# -----------------------------
# Using Streamlit columns to center the selector nicely
c1, c2, c3 = st.columns([1, 4, 1])
with c2:
    locations = ["Bangalore", "Mumbai", "Gurgaon"]
    selected_loc = st.selectbox("Select Location", locations, index=0)

filtered_df = df[df[selected_loc] == True].reset_index(drop=True)

# -----------------------------
# 5. GENERATE TIMELINE HTML
# -----------------------------
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
        # Placeholder if image missing
        img_tag = '<div class="card-img" style="display:flex;align-items:center;justify-content:center;color:#94a3b8;font-size:0.8rem;">NO IMG</div>'
    
    # Alternate left/right classes
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
# 6. FOOTER
# -----------------------------
st.markdown("""
<div class="footer-note">
    <div style="font-weight: 800; font-size: 1.2rem; margin-bottom: 0.5rem; color: #0F172A;">Note</div>
    <ul style="color: #DC2626; font-weight: 600; font-size: 0.95rem; line-height: 1.6; padding-left: 1.2rem;">
        <li>Holidays that fall on Saturdays or Sundays are not included in this list.</li>
        <li>Ramzan and Bakrid dates may vary based on moon sighting confirmation by the religious authorities.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; margin: 3rem 0; color:#475569; font-size:0.8rem; font-weight:600; text-shadow: 1px 1px 2px rgba(255,255,255,0.8);">
    Confidential • FinBox Internal Use Only
</div>
""", unsafe_allow_html=True)
