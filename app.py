
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# --------------------------------------
# CREWPULSE - ASTRONAUT HEALTH MONITOR
# --------------------------------------

st.set_page_config(
    page_title="CrewPulse | Mission Control",
    page_icon="🚀",
    layout="wide"
)

# Load CSV data
DATA_FILE = Path(__file__).parent / "data" / "astronaut_health.csv"


@st.cache_data
def load_data(file_path, modified_time):
    return pd.read_csv(file_path)


df = load_data(str(DATA_FILE), DATA_FILE.stat().st_mtime)

# Application header
st.title("🚀 CrewPulse")
st.subheader("Astronaut Health Intelligence System")


st.caption(
    "Monitor. Detect. Protect. | "
    "Simulated astronaut health monitoring prototype"
)

st.divider()

# --------------------------------------
# NASA RESEARCH & DATA SOURCES
# --------------------------------------

st.header("🛰️ NASA Research & Data Sources")

st.markdown(
    """
    CrewPulse is informed by NASA's spaceflight health
    and life sciences research.

    **Important:** The astronaut readings in this prototype
    are simulated demonstration data, not actual NASA
    astronaut medical records.
    """
)

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("NASA OSDR")
    st.write(
        "Explore space biology, physiological, behavioural "
        "and environmental research."
    )
    st.link_button(
        "Explore OSDR",
        "https://osdr.nasa.gov/bio/repo/"
    )

with col2:
    st.subheader("Life Sciences Portal")
    st.write(
        "Explore human spaceflight and ground-analogue research."
    )
    st.link_button(
        "Explore Portal",
        "https://nlsp.nasa.gov/"
    )

with col3:
    st.subheader("Human Research Program")
    st.write(
        "Understand astronaut health and performance risks."
    )
    st.link_button(
        "Explore HRP",
        "https://www.nasa.gov/hrp/"
    )

st.subheader("How NASA Research Informs CrewPulse")


research_mapping = {
    "Sleep Duration": (
        "NASA SSM_Actigraphy: sleep time, "
        "sleep efficiency and awakenings."
    ),
    "Sleep Quality": (
        "NASA SSM_Sleep_Quality: sleep quality, "
        "sleep quantity, sleepiness and tiredness."
    ),
    "Wellness Indicators": (
        "NASA SSM_Sleep_Quality: energy level, "
        "stress and mentality."
    ),
    "Team Wellbeing": (
        "NASA SSM_Sleep_Quality: team cohesion, "
        "team performance and group living."
    ),
    "Heart Rate & Temperature": (
        "Prototype monitoring features. These are not "
        "validated by the two sleep datasets referenced here."
    ),
    "Combined Wellness Score": (
        "An illustrative CrewPulse calculation, "
        "not a NASA-provided score."
    )
}

for metric, explanation in research_mapping.items():
    st.markdown(f"**{metric}:** {explanation}")

st.info(
    "NASA research informs selected monitoring concepts. "
    "CrewPulse currently uses simulated data, does not import "
    "restricted NASA datasets, and has no NASA-approved "
    "thresholds or clinical validation."
)


st.caption(
    "Research sources: NASA OSDR, NASA Life Sciences Portal "
    "and NASA Human Research Program."
)

st.divider()

# Sidebar
st.sidebar.title("Mission Control")


astronaut_profiles = {
    "Astronaut 01": "A01",
    "Astronaut 02": "A02"
}

astronaut = st.sidebar.selectbox(
    "Select Astronaut",
    list(astronaut_profiles.keys())
)

selected_id = astronaut_profiles[astronaut]

# Filter all readings for the selected astronaut
df = df[df["astronaut_id"] == selected_id].copy()

st.sidebar.success(f"Profile loaded: {selected_id}")


mission_day = st.sidebar.slider(
    "Select Mission Day",
    min_value=1,
    max_value=int(df["mission_day"].max()),
    value=30
)

st.sidebar.info("CrewPulse Prototype v1.1")

# Select current mission reading
current = df[df["mission_day"] == mission_day].iloc[0]

# --------------------------------------
# PERSONAL HEALTH BASELINE
# --------------------------------------

# Use the first 5 mission days as baseline
baseline_data = df[df["mission_day"] <= 5]

baseline = baseline_data[
    ["heart_rate", "temperature", "sleep_hours", "wellness_score"]
].mean()

# Calculate differences from personal baseline
heart_rate_change = (
    (current["heart_rate"] - baseline["heart_rate"])
    / baseline["heart_rate"]
) * 100

temperature_change = (
    current["temperature"] - baseline["temperature"]
)

sleep_change = (
    current["sleep_hours"] - baseline["sleep_hours"]
)

wellness_change = (
    current["wellness_score"] - baseline["wellness_score"]
)

# Health overview
st.subheader("📊 Health Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Heart Rate",
    f'{current["heart_rate"]:.0f} BPM'
)

col2.metric(
    "Body Temperature",
    f'{current["temperature"]:.1f} °C'
)

col3.metric(
    "Sleep Duration",
    f'{current["sleep_hours"]:.1f} Hours'
)

col4.metric(
    "Wellness Score",
    f'{current["wellness_score"]:.0f}/100'
)

st.caption(
    f"Showing readings for {astronaut} "
    f"on Mission Day {mission_day}"
)

st.divider()

# Health trends
st.subheader("📈 Health Trends")

tab1, tab2, tab3, tab4 = st.tabs([
    "Heart Rate",
    "Temperature",
    "Sleep",
    "Wellness"
])

with tab1:
    fig = px.line(
        df,
        x="mission_day",
        y="heart_rate",
        markers=True,
        title="Heart Rate During Mission",
        labels={
            "mission_day": "Mission Day",
            "heart_rate": "Heart Rate (BPM)"
        }
    )
    fig.add_vline(
        x=mission_day,
        line_dash="dash",
        annotation_text="Selected Day"
    )
    st.plotly_chart(fig, width="stretch")

with tab2:
    fig = px.line(
        df,
        x="mission_day",
        y="temperature",
        markers=True,
        title="Body Temperature During Mission",
        labels={
            "mission_day": "Mission Day",
            "temperature": "Temperature (°C)"
        }
    )
    fig.add_vline(x=mission_day, line_dash="dash")
    st.plotly_chart(fig, width="stretch")

with tab3:
    fig = px.bar(
        df,
        x="mission_day",
        y="sleep_hours",
        title="Daily Sleep Duration",
        labels={
            "mission_day": "Mission Day",
            "sleep_hours": "Sleep (Hours)"
        }
    )
    st.plotly_chart(fig, width="stretch")

with tab4:
    fig = px.line(
        df,
        x="mission_day",
        y="wellness_score",
        markers=True,
        title="Astronaut Wellness Score",
        labels={
            "mission_day": "Mission Day",
            "wellness_score": "Wellness Score"
        }
    )
    st.plotly_chart(fig, width="stretch")


st.divider()

# --------------------------------------
# PERSONAL BASELINE COMPARISON
# --------------------------------------

st.subheader("🧬 Personal Health Baseline")

st.write(
    "Current health readings compared with "
    "the astronaut's first 5 mission days."
)

comparison = pd.DataFrame({
    "Health Indicator": [
        "Heart Rate",
        "Temperature",
        "Sleep Duration",
        "Wellness Score"
    ],
    "Personal Baseline": [
        f'{baseline["heart_rate"]:.1f} BPM',
        f'{baseline["temperature"]:.2f} °C',
        f'{baseline["sleep_hours"]:.2f} hours',
        f'{baseline["wellness_score"]:.1f}/100'
    ],
    "Current Reading": [
        f'{current["heart_rate"]:.1f} BPM',
        f'{current["temperature"]:.2f} °C',
        f'{current["sleep_hours"]:.2f} hours',
        f'{current["wellness_score"]:.1f}/100'
    ],
    "Change": [
        f'{heart_rate_change:+.1f}%',
        f'{temperature_change:+.2f} °C',
        f'{sleep_change:+.2f} hours',
        f'{wellness_change:+.1f} points'
    ]
})

st.dataframe(comparison, hide_index=True, width="stretch")

# --------------------------------------

# --------------------------------------
# CREWPULSE INTELLIGENT ALERT SYSTEM
# --------------------------------------

st.subheader("🚨 Intelligent Mission Alerts")

# Configurable prototype rules
# These are NOT medically validated thresholds.

def detect_changes(row, baseline):
    signals = []

    hr_change = (
        (row["heart_rate"] - baseline["heart_rate"])
        / baseline["heart_rate"]
    ) * 100

    temp_change = row["temperature"] - baseline["temperature"]
    sleep_change = row["sleep_hours"] - baseline["sleep_hours"]
    wellness_change = row["wellness_score"] - baseline["wellness_score"]

    if abs(hr_change) >= 10:
        signals.append("Heart rate changed significantly")

    if abs(temp_change) >= 0.5:
        signals.append("Temperature changed significantly")

    if sleep_change <= -1:
        signals.append("Sleep duration decreased")

    if wellness_change <= -10:
        signals.append("Wellness score decreased")

    return signals


# Detect changes for the selected mission day
current_alerts = detect_changes(current, baseline)

# Check the previous 3 mission days, including today
recent_data = df[
    (df["mission_day"] <= mission_day) &
    (df["mission_day"] >= max(1, mission_day - 2))
]

recent_alerts = []

for _, row in recent_data.iterrows():
    recent_alerts.extend(detect_changes(row, baseline))

# Identify repeated signals
persistent_alerts = []

for signal in set(recent_alerts):
    if recent_alerts.count(signal) >= 2:
        persistent_alerts.append(signal)

# Determine prototype severity
if len(current_alerts) >= 3:
    severity = "CRITICAL"
elif len(current_alerts) >= 2 and persistent_alerts:
    severity = "CRITICAL"
elif current_alerts or persistent_alerts:
    severity = "WARNING"
else:
    severity = "NORMAL"


# Display alert summary
col1, col2, col3 = st.columns(3)

col1.metric("Current Changes", len(current_alerts))
col2.metric("Persistent Patterns", len(persistent_alerts))
col3.metric("Alert Status", severity)

st.divider()

if severity == "CRITICAL":
    st.error(
        "CRITICAL: Multiple unusual health indicators "
        "or persistent changes detected. Review required."
    )

elif severity == "WARNING":
    st.warning(
        "WARNING: Unusual health changes detected. "
        "Monitor the astronaut's health trend."
    )

else:
    st.success(
        "NORMAL: No configured prototype alert "
        "conditions detected."
    )


# Explain current changes
st.markdown("### Current Health Findings")

if current_alerts:
    for signal in current_alerts:
        st.write("⚠️", signal)
else:
    st.write("No current changes exceeded the configured rules.")


# Explain persistent changes
st.markdown("### Persistent Health Patterns")

if persistent_alerts:
    for signal in persistent_alerts:
        st.write("🔁", signal)
else:
    st.write("No repeated alert patterns detected in the recent 3-day window.")


st.caption(
    "CrewPulse uses illustrative, configurable rules for demonstration. "
    "Alert severity is not a clinical risk classification, "
    "NASA-approved threshold, or medical diagnosis."
)


# Data table
with st.expander("View Mission Health Data"):
    st.dataframe(df, width="stretch")

st.info(
    "All readings are simulated demonstration data. "
    "They are not real astronaut measurements or "
    "clinically validated medical thresholds."
)

st.divider()

st.caption(
    "CrewPulse | NASA Space Apps Challenge 2026"
)
