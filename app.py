import requests
import pandas as pd
import streamlit as st

# Set page config to wide with a dark theme footprint
st.set_page_config(page_title="CF Nexus Analytics", page_icon="⚡", layout="wide")

# --- CYBERPUNK ULTRA-PREMIUM UI CSS ---
st.markdown("""
    <style>
    .main { background-color: #0b0f19; }
    h1 { color: #00f2fe; font-family: 'Space Grotesk', sans-serif; font-weight: 800; }
    h3 { color: #4facfe; }
    
    /* Premium Glassmorphic Cards */
    .glass-card {
        background: rgba(17, 24, 39, 0.7);
        border: 1px solid rgba(79, 70, 229, 0.3);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        padding: 25px;
        border-radius: 16px;
        color: #e2e8f0;
        margin-bottom: 25px;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: bold;
        color: #00f2fe;
    }
    .rec-box {
        background: linear-gradient(135deg, #1e1b4b 0%, #061024 100%);
        border-left: 5px solid #00f2fe;
        padding: 20px;
        border-radius: 8px;
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ NEXUS: Codeforces Intelligence Engine")
st.write("Advanced algorithmic telemetry, difficulty spectrum mapping, and predictive practice charting.")
st.markdown("---")

# --- SIDEBAR CONTROL UNIT ---
st.sidebar.markdown("### 🎛️ Control Terminal")
handle = st.sidebar.text_input("Enter Target Handle:", "Suryansh210207").strip()

rating_range = st.sidebar.slider(
    "Set Analytics Rating Bounds:",
    min_value=800, max_value=2500, value=(800, 1500), step=100
)

@st.cache_data(ttl=1800, show_spinner=False)
def fetch_cf_profile(cf_handle):
    # Fetch User Submissions
    status_url = f"https://codeforces.com/api/user.status?handle={cf_handle}"
    try:
        res = requests.get(status_url, timeout=12)
        if res.status_code != 200: return None
        return res.json()
    except:
        return None

if st.sidebar.button("Run Advanced Diagnostics", type="primary"):
    if not handle:
        st.sidebar.error("Error: Handle required.")
    else:
        with st.spinner("Decoding API payloads and compiling metrics..."):
            response = fetch_cf_profile(handle)

        if not response or response.get("status") != "OK":
            st.error("🚨 Terminal Error: Unable to sync with Codeforces database. Verify spelling.")
        else:
            submissions = response["result"]
            solved_problems = []
            solved_ids = set() # Track globally to isolate what is already solved
            
            for sub in submissions:
                if sub.get("verdict") == "OK":
                    prob = sub.get("problem", {})
                    prob_id = f"{prob.get('contestId', '')}{prob.get('index', '')}"
                    if not prob_id or prob_id in solved_ids: continue
                    
                    solved_ids.add(prob_id)
                    solved_problems.append({
                        "ID": prob_id,
                        "Name": prob.get("name", "Unknown"),
                        "Rating": prob.get("rating", 0),
                        "Tags": prob.get("tags", [])
                    })
            
            if not solved_problems:
                st.warning("Telemetry Notice: Empty profile signature within current constraints.")
            else:
                base_df = pd.DataFrame(solved_problems)
                
                # Filter down by active slider bounds
                df = base_df[(base_df['Rating'] >= rating_range[0]) & (base_df['Rating'] <= rating_range[1])]
                # Strip out problems with no rating recorded for clean rating analytics
                df_rated = df[df['Rating'] > 0]
                
                # --- UI ROW 1: CORE TELEMETRY METRICS ---
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown(f'<div class="glass-card">📊 <span style="color:#9ca3af;">Total Profile Solves</span><br><span class="metric-value">{len(base_df)}</span></div>', unsafe_allow_html=True)
                with col2:
                    st.markdown(f'<div class="glass-card">🎯 <span style="color:#9ca3af;">Solves In Active Range</span><br><span class="metric-value">{len(df)}</span></div>', unsafe_allow_html=True)
                with col3:
                    median_r = int(df_rated['Rating'].median()) if not df_rated.empty else 0
                    st.markdown(f'<div class="glass-card">📈 <span style="color:#9ca3af;">Median Difficulty Target</span><br><span class="metric-value">{median_r}</span></div>', unsafe_allow_html=True)
                
                # --- UI ROW 2: DUAL VISUALIZATION ENGINE ---
                all_tags = df.explode('Tags')
                all_tags = all_tags[all_tags['Tags'].notna() & (all_tags['Tags'] != '')]
                
                chart_col1, chart_col2 = st.columns(2)
                
                with chart_col1:
                    st.write("### 📊 Algorithm Tag Densities")
                    if not all_tags.empty:
                        tag_counts = all_tags['Tags'].value_counts().head(8)
                        st.bar_chart(tag_counts, color="#4facfe")
                    else:
                        st.info("No algorithm labels captured.")
                        
                with chart_col2:
                    st.write("### 📈 Solved Problem Rating Distribution")
                    if not df_rated.empty:
                        rating_counts = df_rated['Rating'].value_counts().sort_index()
                        st.bar_chart(rating_counts, color="#00f2fe")
                    else:
                        st.info("No rated problems available in this range.")
                
                # --- UI ROW 3: PROGRESSIVE LADDER RECOMMENDATION SYSTEM ---
                st.markdown("---")
                st.write("### 🧠 Predictive Growth Ladder")
                
                # Filter out metadata tags and complex advanced topics
                ignored_tags = {'*special', 'fft', 'chinese remainder theorem', 'flows', 'heavy-light decomposition', 'matrices'}
                clean_tags = all_tags[~all_tags['Tags'].isin(ignored_tags) & ~all_tags['Tags'].str.startswith('*')]
                
                if not clean_tags.empty and not df_rated.empty:
                    # Target weakest algorithm among common competitive topics
                    weakest_tag = clean_tags['Tags'].value_counts().index[-1]
                    
                    # Calculate baseline rating tier from current average solved difficulty
                    avg_solved = int(df_rated['Rating'].mean())
                    base_tier = ((avg_solved // 100) + 1) * 100 # Rounds up (e.g. ~861 -> 900)
                    base_tier = max(900, base_tier)
                    
                    # Create 3 distinct target tiers (+0, +100, +200 relative to base tier)
                    ladder_tiers = [
                        {"label": "🟢 STEP 1: Warmup (+100)", "rating": base_tier},
                        {"label": "🟡 STEP 2: Target (+200)", "rating": base_tier + 100},
                        {"label": "🔴 STEP 3: Stretch (+300)", "rating": base_tier + 200}
                    ]
                    
                    st.markdown(f"""
                        <div class="rec-box">
                            <h4 style="margin:0; color:#00f2fe;">📈 Progressive Level-Up Track: {weakest_tag.upper()}</h4>
                            <p style="margin:5px 0 0 0; color:#9ca3af;">Based on your current baseline (~{avg_solved}), here is a 3-tier difficulty ladder targeting your gap in <b>{weakest_tag}</b>. Solve them sequentially from left to right!</p>
                        </div>
                    """, unsafe_allow_html=True)
                    st.write("##")
                    
                    # LIVE API CALL TO GLOBAL PROBLEMSET
                    try:
                        global_problems_url = "https://codeforces.com/api/problemset.problems"
                        prob_res = requests.get(global_problems_url, timeout=10).json()
                        
                        if prob_res.get("status") == "OK":
                            all_global_probs = prob_res["result"]["problems"]
                            recommendations = []
                            
                            # Loop over each ladder tier and fetch 1 problem matching that exact rating
                            for tier in ladder_tiers:
                                target_r = tier["rating"]
                                found_prob = None
                                
                                # First attempt: Find problem with weakest tag at target rating
                                for p in all_global_probs:
                                    g_id = f"{p.get('contestId', '')}{p.get('index', '')}"
                                    if g_id not in solved_ids and p.get('rating') == target_r and weakest_tag in p.get('tags', []):
                                        found_prob = p
                                        break
                                
                                # Fallback: Find any unsolved problem at target rating if tag combo is rare
                                if not found_prob:
                                    for p in all_global_probs:
                                        g_id = f"{p.get('contestId', '')}{p.get('index', '')}"
                                        if g_id not in solved_ids and p.get('rating') == target_r:
                                            found_prob = p
                                            break
                                            
                                if found_prob:
                                    recommendations.append({"tier_info": tier, "prob": found_prob})

                            # Render the Progressive Ladder Cards
                            if recommendations:
                                r_cols = st.columns(len(recommendations))
                                for i, item in enumerate(recommendations):
                                    tier_info = item["tier_info"]
                                    rec_prob = item["prob"]
                                    link = f"https://codeforces.com/problemset/problem/{rec_prob['contestId']}/{rec_prob['index']}"
                                    
                                    with r_cols[i]:
                                        st.markdown(f"""
                                            <div style="background:#111827; border: 1px solid #00f2fe; padding:15px; border-radius:8px; text-align:center;">
                                                <span style="color:#00f2fe; font-size:0.85rem; font-weight:bold;">{tier_info['label']}</span>
                                                <h5 style="margin:10px 0;">{rec_prob['contestId']}{rec_prob['index']} - {rec_prob['name']}</h5>
                                                <p style="margin:0 0 10px 0; font-size:0.9rem; color:#9ca3af;">Difficulty: <b>{rec_prob.get('rating')}</b></p>
                                                <a href="{link}" target="_blank" style="background:#4facfe; color:black; padding:6px 12px; border-radius:4px; text-decoration:none; font-weight:bold; font-size:0.85rem;">Launch Task 🚀</a>
                                            </div>
                                        """, unsafe_allow_html=True)
                            else:
                                st.write("*No ladder combinations found in global index. Shift your rating slider bounds.*")
                    except Exception as e:
                        st.write("⚠️ *Could not map global index for fresh recommendations.*")