import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Holiday Roadmap 2026", page_icon="✨", layout="wide")

# -----------------------------
# COMPLETE HOLIDAY DATA
# -----------------------------
data = [
    {"Date": "01-Jan-26", "Day": "Thursday", "Name": "New Year", "Bangalore": True, "Mumbai": True, "Gurgaon": True},
    {"Date": "15-Jan-26", "Day": "Thursday", "Name": "Makara Sankranti", "Bangalore": True, "Mumbai": True, "Gurgaon": True},
    {"Date": "26-Jan-26", "Day": "Monday", "Name": "Republic Day", "Bangalore": True, "Mumbai": True, "Gurgaon": True},
    {"Date": "04-Mar-26", "Day": "Wednesday", "Name": "Holi", "Bangalore": True, "Mumbai": True, "Gurgaon": True},
    {"Date": "19-Mar-26", "Day": "Thursday", "Name": "Ugadi / Gudhi Padwa", "Bangalore": True, "Mumbai": True, "Gurgaon": False},
    {"Date": "03-Apr-26", "Day": "Friday", "Name": "Good Friday", "Bangalore": True, "Mumbai": True, "Gurgaon": True},
    {"Date": "01-May-26", "Day": "Friday", "Name": "May Day", "Bangalore": True, "Mumbai": True, "Gurgaon": True},
    {"Date": "28-May-26", "Day": "Thursday", "Name": "Bakrid", "Bangalore": True, "Mumbai": True, "Gurgaon": True},
    {"Date": "21-Aug-26", "Day": "Friday", "Name": "Varamahalakshmi Vrata", "Bangalore": True, "Mumbai": False, "Gurgaon": False},
    {"Date": "28-Aug-26", "Day": "Friday", "Name": "Raksha Bandhan", "Bangalore": False, "Mumbai": True, "Gurgaon": True},
    {"Date": "14-Sep-26", "Day": "Monday", "Name": "Ganesh Chaturthi", "Bangalore": True, "Mumbai": True, "Gurgaon": True},
    {"Date": "02-Oct-26", "Day": "Friday", "Name": "Gandhi Jayanthi", "Bangalore": True, "Mumbai": True, "Gurgaon": True},
    {"Date": "20-Oct-26", "Day": "Tuesday", "Name": "Dussehra", "Bangalore": True, "Mumbai": True, "Gurgaon": True},
    {"Date": "09-Nov-26", "Day": "Monday", "Name": "Diwali", "Bangalore": True, "Mumbai": True, "Gurgaon": True},
    {"Date": "10-Nov-26", "Day": "Tuesday", "Name": "Diwali", "Bangalore": True, "Mumbai": True, "Gurgaon": True},
    {"Date": "24-Nov-26", "Day": "Tuesday", "Name": "Guru Nanak's Birthday", "Bangalore": False, "Mumbai": False, "Gurgaon": True},
    {"Date": "25-Dec-26", "Day": "Friday", "Name": "Christmas", "Bangalore": True, "Mumbai": True, "Gurgaon": True},
]

df = pd.DataFrame(data)

# -----------------------------
# PREMIUM STYLING
# -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

* {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
}

/* Hide Streamlit branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.main .block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1400px;
}

/* Premium Header */
.premium-header {
    text-align: center;
    margin-bottom: 3rem;
    padding: 3rem 2rem;
    background: linear-gradient(135deg, rgba(139, 92, 246, 0.1), rgba(59, 130, 246, 0.1));
    border-radius: 24px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
}

.premium-title {
    font-size: 3.5rem;
    font-weight: 900;
    background: linear-gradient(135deg, #a78bfa 0%, #60a5fa 50%, #34d399 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.5rem;
    letter-spacing: -2px;
}

.premium-subtitle {
    font-size: 1.1rem;
    color: rgba(255, 255, 255, 0.6);
    font-weight: 500;
}

/* Stats Cards */
.stats-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
    margin-bottom: 3rem;
}

.stat-card {
    background: linear-gradient(135deg, rgba(139, 92, 246, 0.15), rgba(59, 130, 246, 0.15));
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    padding: 1.8rem;
    text-align: center;
    transition: all 0.3s ease;
}

.stat-card:hover {
    transform: translateY(-5px);
    border-color: rgba(139, 92, 246, 0.5);
    box-shadow: 0 20px 40px rgba(139, 92, 246, 0.2);
}

.stat-number {
    font-size: 2.5rem;
    font-weight: 900;
    background: linear-gradient(135deg, #a78bfa, #60a5fa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
}

.stat-label {
    font-size: 0.9rem;
    color: rgba(255, 255, 255, 0.5);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Timeline */
.timeline-container {
    position: relative;
    margin: 3rem auto;
    padding: 2rem 0;
}

.timeline-line {
    position: absolute;
    left: 50%;
    top: 0;
    bottom: 0;
    width: 3px;
    background: linear-gradient(180deg, 
        transparent 0%, 
        rgba(139, 92, 246, 0.5) 10%, 
        rgba(139, 92, 246, 0.8) 50%, 
        rgba(139, 92, 246, 0.5) 90%, 
        transparent 100%
    );
    transform: translateX(-50%);
}

.holiday-item {
    position: relative;
    display: flex;
    margin-bottom: 4rem;
    align-items: center;
}

.holiday-item:last-child {
    margin-bottom: 0;
}

/* Alternating layout */
.holiday-item:nth-child(odd) {
    flex-direction: row;
}

.holiday-item:nth-child(even) {
    flex-direction: row-reverse;
}

.holiday-spacer {
    width: 50%;
}

.holiday-card {
    width: 45%;
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.9), rgba(15, 23, 42, 0.9));
    border: 1px solid rgba(139, 92, 246, 0.3);
    border-radius: 24px;
    padding: 2rem;
    position: relative;
    backdrop-filter: blur(20px);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.holiday-card:hover {
    transform: scale(1.05);
    border-color: rgba(139, 92, 246, 0.8);
    box-shadow: 0 25px 50px rgba(139, 92, 246, 0.3);
}

.holiday-date-badge {
    position: absolute;
    top: -15px;
    left: 2rem;
    background: linear-gradient(135deg, #8b5cf6, #3b82f6);
    color: white;
    padding: 0.5rem 1.5rem;
    border-radius: 100px;
    font-weight: 800;
    font-size: 0.85rem;
    letter-spacing: 1px;
    box-shadow: 0 10px 20px rgba(139, 92, 246, 0.4);
}

.holiday-name {
    font-size: 1.8rem;
    font-weight: 800;
    color: white;
    margin-bottom: 0.5rem;
    margin-top: 0.5rem;
}

.holiday-day {
    font-size: 1rem;
    color: rgba(255, 255, 255, 0.5);
    font-weight: 600;
    margin-bottom: 1rem;
}

.holiday-month {
    display: inline-block;
    background: rgba(139, 92, 246, 0.2);
    color: #a78bfa;
    padding: 0.4rem 1rem;
    border-radius: 100px;
    font-size: 0.85rem;
    font-weight: 700;
    letter-spacing: 1px;
}

/* Timeline Node */
.timeline-node {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    width: 20px;
    height: 20px;
    background: linear-gradient(135deg, #8b5cf6, #3b82f6);
    border: 4px solid #1e293b;
    border-radius: 50%;
    box-shadow: 0 0 0 8px rgba(139, 92, 246, 0.2);
    z-index: 10;
    transition: all 0.3s ease;
}

.holiday-item:hover .timeline-node {
    width: 24px;
    height: 24px;
    box-shadow: 0 0 0 12px rgba(139, 92, 246, 0.3), 0 0 20px rgba(139, 92, 246, 0.6);
}

/* Location Selector */
.stSelectbox > div > div {
    background: rgba(30, 41, 59, 0.8) !important;
    border: 1px solid rgba(139, 92, 246, 0.3) !important;
    border-radius: 16px !important;
    color: white !important;
    font-weight: 600 !important;
}

/* Mobile Responsive */
@media (max-width: 768px) {
    .premium-title {
        font-size: 2rem;
    }
    
    .timeline-line {
        left: 30px;
    }
    
    .holiday-item,
    .holiday-item:nth-child(even) {
        flex-direction: row !important;
        padding-left: 60px;
    }
    
    .holiday-spacer {
        display: none;
    }
    
    .holiday-card {
        width: 100%;
    }
    
    .timeline-node {
        left: 30px;
    }
    
    .stats-container {
        grid-template-columns: 1fr;
    }
}

/* Month separators */
.month-separator {
    text-align: center;
    margin: 3rem 0 2rem;
    position: relative;
}

.month-separator::before,
.month-separator::after {
    content: '';
    position: absolute;
    top: 50%;
    width: 40%;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(139, 92, 246, 0.5), transparent);
}

.month-separator::before {
    left: 0;
}

.month-separator::after {
    right: 0;
}

.month-label {
    display: inline-block;
    background: linear-gradient(135deg, #8b5cf6, #3b82f6);
    color: white;
    padding: 0.8rem 2rem;
    border-radius: 100px;
    font-weight: 800;
    font-size: 1.2rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    box-shadow: 0 10px 30px rgba(139, 92, 246, 0.4);
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown("""
<div class="premium-header">
    <div class="premium-title">✨ Holiday Roadmap 2026</div>
    <div class="premium-subtitle">Your comprehensive guide to celebrations and time off</div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# LOCATION SELECTOR
# -----------------------------
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    locations = ["Bangalore", "Mumbai", "Gurgaon"]
    selected_location = st.selectbox("📍 Select Your Location", locations, index=0)

filtered_df = df[df[selected_location] == True].reset_index(drop=True)

# -----------------------------
# STATISTICS CARDS
# -----------------------------
total_holidays = len(filtered_df)
long_weekends = sum(1 for _, row in filtered_df.iterrows() if row['Day'] in ['Friday', 'Monday'])
months_with_holidays = filtered_df['Date'].apply(lambda x: x.split('-')[1]).nunique()

st.markdown(f"""
<div class="stats-container">
    <div class="stat-card">
        <div class="stat-number">{total_holidays}</div>
        <div class="stat-label">Total Holidays</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">{long_weekends}</div>
        <div class="stat-label">Potential Long Weekends</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">{months_with_holidays}</div>
        <div class="stat-label">Months Covered</div>
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# TIMELINE GENERATION
# -----------------------------
st.markdown('<div class="timeline-container"><div class="timeline-line"></div>', unsafe_allow_html=True)

current_month = None
month_names = {
    'Jan': 'January', 'Feb': 'February', 'Mar': 'March', 'Apr': 'April',
    'May': 'May', 'Jun': 'June', 'Jul': 'July', 'Aug': 'August',
    'Sep': 'September', 'Oct': 'October', 'Nov': 'November', 'Dec': 'December'
}

for idx, row in filtered_df.iterrows():
    date_parts = row['Date'].split('-')
    day_num = date_parts[0]
    month_abbr = date_parts[1]
    year = date_parts[2]
    
    month_full = month_names.get(month_abbr, month_abbr)
    
    # Add month separator if new month
    if current_month != month_abbr:
        current_month = month_abbr
        st.markdown(f"""
        <div class="month-separator">
            <span class="month-label">{month_full}</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="holiday-item">
        <div class="timeline-node"></div>
        <div class="holiday-spacer"></div>
        <div class="holiday-card">
            <div class="holiday-date-badge">{day_num} {month_abbr}</div>
            <div class="holiday-name">{row['Name']}</div>
            <div class="holiday-day">📅 {row['Day']}</div>
            <span class="holiday-month">{month_full} {year}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown(f"""
<div style="text-align: center; margin-top: 4rem; padding: 2rem; color: rgba(255, 255, 255, 0.4); font-size: 0.9rem;">
    Showing {total_holidays} holidays for {selected_location} • Plan your year wisely ✨
</div>
""", unsafe_allow_html=True)