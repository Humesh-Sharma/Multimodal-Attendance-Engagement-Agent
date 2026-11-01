
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="EduSense AI | Classroom Intelligence",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# CUSTOM UI / CSS
# ==========================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --bg: #0b1120;
    --panel: #111b2e;
    --panel-light: #16233a;
    --border: #263650;
    --text: #edf3ff;
    --muted: #94a6c5;
    --blue: #60a5fa;
    --cyan: #22d3ee;
    --green: #34d399;
}

.stApp {
    background: var(--bg);
    color: var(--text);
    font-family: 'Inter', sans-serif;
}

[data-testid="stHeader"] {
    background: rgba(11, 17, 32, 0.9);
}

[data-testid="stSidebar"] {
    background: #0e1728;
    border-right: 1px solid var(--border);
}

[data-testid="stSidebar"] > div:first-child {
    padding-top: 1.5rem;
}

[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label {
    color: #c4d2e9;
}

h1, h2, h3 {
    color: var(--text) !important;
    letter-spacing: -0.5px;
}

p, li {
    color: #c1cde0;
}

.block-container {
    padding-top: 1.8rem;
    padding-bottom: 3rem;
    max-width: 1600px;
}

div[data-testid="stMetric"] {
    background: linear-gradient(145deg, #15233a, #101a2c);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 19px 20px;
    min-height: 125px;
    box-shadow: 0 5px 18px rgba(0,0,0,0.12);
}

div[data-testid="stMetricLabel"] p {
    color: var(--muted) !important;
    font-size: 0.85rem;
    font-weight: 500;
}

div[data-testid="stMetricValue"] {
    color: #f1f6ff !important;
    font-size: 1.8rem;
    font-weight: 750;
}

div[data-testid="stMetricDelta"] {
    font-size: 0.8rem;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: var(--panel);
    border-color: var(--border);
    border-radius: 16px;
}

.stButton > button,
.stDownloadButton > button {
    background: linear-gradient(100deg, #2563eb, #0891b2);
    color: white;
    border: none;
    border-radius: 9px;
    font-weight: 600;
    padding: 0.55rem 1rem;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    border: 1px solid #60a5fa;
    color: white;
    filter: brightness(1.12);
}

[data-testid="stDataFrame"] {
    border: 1px solid var(--border);
    border-radius: 12px;
    overflow: hidden;
}

[data-testid="stCameraInput"] {
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 10px;
    background: #111b2e;
}

hr {
    border-color: var(--border);
}

div[data-testid="stAlert"] {
    border-radius: 12px;
}

.eyebrow {
    color: var(--cyan);
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 7px;
}

.hero {
    background: linear-gradient(115deg, #142748 0%, #11243b 55%, #123343 100%);
    border: 1px solid #294464;
    border-radius: 18px;
    padding: 25px 28px;
    margin-bottom: 23px;
}

.hero-title {
    color: #f1f6ff;
    font-size: 1.8rem;
    font-weight: 800;
    margin: 0 0 8px 0;
}

.hero-subtitle {
    color: #b3c5df;
    font-size: 0.92rem;
    margin: 0;
}

.section-label {
    color: #f1f6ff;
    font-size: 1.08rem;
    font-weight: 700;
    margin-bottom: 12px;
}

.mini-label {
    color: var(--muted);
    font-size: 0.78rem;
    margin-bottom: 5px;
}

.insight-card {
    background: #171f35;
    border: 1px solid #624b3a;
    border-left: 4px solid #f59e0b;
    padding: 17px;
    border-radius: 12px;
    margin-bottom: 15px;
}

.insight-title {
    color: #fbbf24;
    font-size: 0.82rem;
    font-weight: 700;
    margin-bottom: 9px;
}

.insight-body {
    color: #edf3ff;
    font-size: 0.95rem;
    font-weight: 600;
    line-height: 1.6;
}

.insight-footer {
    color: #a9bad3;
    font-size: 0.8rem;
    margin-top: 9px;
}

.status-pill {
    display: inline-block;
    color: #6ee7b7;
    background: #103b35;
    border: 1px solid #1b6353;
    border-radius: 30px;
    padding: 6px 12px;
    font-size: 0.76rem;
    font-weight: 700;
}

.brand {
    font-size: 1.45rem;
    font-weight: 800;
    color: #f1f6ff;
}

.brand span {
    color: #60a5fa;
}

.brand-caption {
    color: #8297b8;
    font-size: 0.78rem;
    margin-top: 4px;
}

[data-testid="stRadio"] label {
    padding-top: 3px;
    padding-bottom: 3px;
}

footer {
    visibility: hidden;
}

@media (max-width: 768px) {
    .hero {
        padding: 20px;
    }
    .hero-title {
        font-size: 1.4rem;
    }
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# SIDEBAR
# ==========================================
with st.sidebar:
    st.markdown("""
    <div style="padding: 5px 0 20px 0;">
        <div class="brand">🎓 EduSense<span> AI</span></div>
        <div class="brand-caption">CLASSROOM INTELLIGENCE SYSTEM</div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("##### WORKSPACE")

    nav_option = st.radio(
        "Navigation",
        [
            "Live Classroom Monitor",
            "Teacher Central & Profile",
            "Session Analytics & Export"
        ],
        label_visibility="collapsed"
    )

    st.divider()

    st.markdown("##### ⚙️ DETECTION SETTINGS")

    conf_threshold = st.slider(
        "Face Detection Confidence",
        0.0, 1.0, 0.80, 0.05
    )

    enable_audio = st.checkbox(
        "Enable Acoustic Telemetry",
        value=True
    )

    st.divider()

    st.markdown("##### SYSTEM STATUS")

    st.markdown(
        '<span class="status-pill">● SYSTEM ONLINE</span>',
        unsafe_allow_html=True
    )

    st.caption("EduSense AI · Prototype v1.0")


# ==========================================
# SAMPLE SESSION TELEMETRY
# ==========================================
@st.cache_data
def load_session_telemetry():
    timestamps = pd.date_range(
        start="2026-10-31 08:47:56",
        periods=20,
        freq="5s"
    )

    attention = [
        85, 84, 85, 78, 82, 50, 80, 78, 25, 80,
        85, 90, 30, 80, 88, 86, 85, 85, 92, 90
    ]

    emotions = [
        "Engaged", "Engaged", "Neutral", "Engaged", "Distracted",
        "Engaged", "Engaged", "Engaged", "Distracted", "Neutral",
        "Engaged", "Engaged", "Neutral", "Distracted", "Engaged",
        "Engaged", "Engaged", "Engaged", "Engaged", "Engaged"
    ]

    audio = np.random.uniform(-46.0, -42.0, size=20).round(1)

    return pd.DataFrame({
        "Timestamp": timestamps.strftime("%H:%M:%S"),
        "avg_attention": attention,
        "Emotion": emotions,
        "Audio_dB": audio
    })


telemetry_data = load_session_telemetry()

# Respect the acoustic telemetry setting in analytics.
if not enable_audio:
    telemetry_data = telemetry_data.drop(columns=["Audio_dB"])


# ==========================================
# REUSABLE PAGE HEADER
# ==========================================
def page_header(eyebrow, title, subtitle):
    st.markdown(f"""
    <div class="hero">
        <div class="eyebrow">{eyebrow}</div>
        <div class="hero-title">{title}</div>
        <p class="hero-subtitle">{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# VIEW 1: LIVE CLASSROOM MONITOR
# ==========================================
if nav_option == "Live Classroom Monitor":

    page_header(
        "LIVE MONITORING / OVERVIEW",
        "Classroom Intelligence",
        "Monitor attendance, attention signals, and classroom activity from one workspace."
    )

    status_col1, status_col2 = st.columns([3, 1])

    with status_col1:
        st.success(
            "Session status: Active · Sample engagement indicators are available."
        )

    with status_col2:
        st.markdown(
            '<div style="text-align:right;padding-top:5px;">'
            '<span class="status-pill">● LIVE SESSION</span></div>',
            unsafe_allow_html=True
        )

    # KPI cards
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Students Present",
            "2",
            delta="Session Active"
        )

    with col2:
        st.metric(
            "Average Attention",
            "87.5%",
            delta="+12% 30-day trend"
        )

    with col3:
        st.metric(
            "Noise Level",
            "-44.0 dB" if enable_audio else "Disabled",
            delta="Normal discussion" if enable_audio else None
        )

    with col4:
        st.metric(
            "Active IDs",
            "ID: 1, ID: 3",
            delta="All Engaged"
        )

    st.markdown("---")

    left_feed, right_side = st.columns([1.7, 1])

    with left_feed:
        st.markdown(
            '<div class="section-label">📹 Classroom Camera</div>',
            unsafe_allow_html=True
        )

        with st.container(border=True):
            st.caption(
                "Capture a frame for the classroom vision pipeline."
            )

            camera_frame = st.camera_input(
                "Camera Input",
                label_visibility="collapsed"
            )

            if camera_frame is not None:
                st.success("Image captured successfully.")
                st.image(
                    camera_frame,
                    caption="Captured classroom frame",
                    use_container_width=True
                )
                st.info(
                    "The captured image is ready for integration with a "
                    "face-detection model. Detection is not implemented here."
                )

        if enable_audio:
            with st.container(border=True):
                st.markdown("**🔊 Acoustic Telemetry**")
                st.caption("Sample acoustic measurements")

                if "Audio_dB" in telemetry_data.columns:
                    avg_audio = telemetry_data["Audio_dB"].mean()
                    st.metric("Average Sample Level", f"{avg_audio:.1f} dB")
                else:
                    st.info("No acoustic measurements available.")

        st.caption(
            f"Configured face detection confidence: {conf_threshold:.0%}"
        )

    with right_side:
        st.markdown(
            '<div class="section-label">💡 AI Recommendation</div>',
            unsafe_allow_html=True
        )

        with st.container(border=True):
            st.markdown("""
            <div class="insight-card">
                <div class="insight-title">⚡ HIGH PRIORITY · 02 MIN AGO</div>
                <div class="insight-body">
                    Challenge students with a harder problem.
                </div>
                <div class="insight-footer">
                    Potential impact: Deeper learning and participation
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.caption(
                "Illustrative recommendation based on the prototype."
            )

        st.markdown(
            '<div class="section-label">🏆 Engagement Leaderboard</div>',
            unsafe_allow_html=True
        )

        leaderboard_df = pd.DataFrame({
            "Student": ["Student 1", "Student 3"],
            "Score": ["36 pts", "2 pts"]
        })

        with st.container(border=True):
            st.dataframe(
                leaderboard_df,
                use_container_width=True,
                hide_index=True
            )


# ==========================================
# VIEW 2: TEACHER CENTRAL & PROFILE
# ==========================================
elif nav_option == "Teacher Central & Profile":

    page_header(
        "TEACHER WORKSPACE / PERFORMANCE",
        "Teacher Central",
        "Review teaching indicators, strengths, and opportunities to improve classroom engagement."
    )

    st.markdown("### Teaching Overview")

    col_t1, col_t2, col_t3 = st.columns(3)

    with col_t1:
        st.metric(
            "Teaching Effectiveness",
            "87.5 / 100",
            delta="+12% 30-day trend"
        )

        with st.container(border=True):
            st.markdown("**📊 Performance Snapshot**")
            st.progress(0.875)
            st.caption("Illustrative effectiveness score: 87.5%")

    with col_t2:
        with st.container(border=True):
            st.markdown("### 🌟 Strengths")

            st.markdown("""
            **01 · Strong engagement**

            High engagement sessions (85%+).

            ---

            **02 · Emotion diversity**

            Manage and respond to varied classroom engagement signals.
            """)

    with col_t3:
        with st.container(border=True):
            st.markdown("### 📚 Recommendations")

            st.markdown("""
            **01 · Interactive polls**

            Introduce quick polls to encourage participation.

            ---

            **02 · Short video breaks**

            Use short video segments to refresh attention.
            """)

            st.caption(
                "Previously supplied impact estimates: +18% and +25%. "
                "These are illustrative, not validated predictions."
            )

    st.markdown("---")

    st.markdown("### 📈 Class History Comparison")

    hist_c1, hist_c2 = st.columns(2)

    with hist_c1:
        with st.container(border=True):
            st.caption("YESTERDAY")
            st.metric("CS101", "78% Avg")
            st.progress(0.78)

    with hist_c2:
        with st.container(border=True):
            st.caption("WORKSHOP SESSION")
            st.metric("Math Workshop", "92% Avg")
            st.progress(0.92)

    st.info(
        "Teaching indicators and class history are sample values. "
        "Connect real session records to calculate actual performance."
    )


# ==========================================
# VIEW 3: SESSION ANALYTICS & EXPORT
# ==========================================
elif nav_option == "Session Analytics & Export":

    page_header(
        "REPORTING / DATA INSIGHTS",
        "Session Analytics",
        "Explore attention patterns, engagement signals, and downloadable session data."
    )

    # Session summary
    avg_attention = telemetry_data["avg_attention"].mean()
    attention_peak = telemetry_data["avg_attention"].max()

    engaged_pct = (
        (telemetry_data["Emotion"] == "Engaged").mean() * 100
    )

    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric(
            "Average Attention",
            f"{avg_attention:.1f}%"
        )

    with m2:
        st.metric(
            "Peak Attention",
            f"{attention_peak:.0f}%"
        )

    with m3:
        st.metric(
            "Engaged Samples",
            f"{engaged_pct:.0f}%"
        )

    st.markdown("---")

    # Export controls
    st.markdown("### 📥 Export Session Data")

    export_col1, export_col2 = st.columns([1, 4])

    with export_col1:
        csv_file = telemetry_data.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            label="Download CSV",
            data=csv_file,
            file_name="session_analytics_report.csv",
            mime="text/csv",
            use_container_width=True
        )

    with export_col2:
        st.caption(
            f"Export contains {len(telemetry_data)} telemetry records. "
            "Acoustic measurements are included only when enabled."
        )

    st.markdown("---")

    chart_left, chart_right = st.columns(2)

    with chart_left:
        with st.container(border=True):
            st.markdown("### 📈 Attention Trend")
            st.caption("Attention score across the session")

            fig_line = px.line(
                telemetry_data,
                x="Timestamp",
                y="avg_attention",
                markers=True,
                title="Class Attention Trend Over Time",
                labels={
                    "Timestamp": "Time",
                    "avg_attention": "Attention (%)"
                }
            )

            fig_line.update_traces(
                line=dict(width=3),
                marker=dict(size=7)
            )

            fig_line.update_layout(
                yaxis_range=[0, 100],
                template="plotly_dark",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font=dict(color="#c1cde0"),
                title_font_size=15,
                margin=dict(l=10, r=10, t=55, b=10),
                xaxis=dict(showgrid=False),
                yaxis=dict(gridcolor="#263650")
            )

            st.plotly_chart(
                fig_line,
                use_container_width=True
            )

    with chart_right:
        with st.container(border=True):
            st.markdown("### 🧠 Emotion Distribution")
            st.caption("Count of recorded engagement states")

            fig_bar = px.histogram(
                telemetry_data,
                x="Timestamp",
                color="Emotion",
                barmode="stack",
                title="Affective States Over Time",
                category_orders={
                    "Emotion": ["Engaged", "Neutral", "Distracted"]
                },
                labels={
                    "Timestamp": "Time",
                    "count": "Observations"
                }
            )

            fig_bar.update_layout(
                template="plotly_dark",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font=dict(color="#c1cde0"),
                title_font_size=15,
                margin=dict(l=10, r=10, t=55, b=10),
                xaxis=dict(showgrid=False),
                yaxis=dict(gridcolor="#263650"),
                legend_title_text="Engagement State"
            )

            st.plotly_chart(
                fig_bar,
                use_container_width=True
            )

    # Raw data
    st.markdown("---")

    with st.expander("🔎 View Raw Telemetry Data"):
        st.dataframe(
            telemetry_data,
            use_container_width=True,
            hide_index=True
        )

    st.caption(
        "EduSense AI · Session analytics prototype · "
        "Charts use sample telemetry data."
    )
