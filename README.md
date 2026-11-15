# 🚀 CrewPulse — Astronaut Health Intelligence System

**Monitor. Detect. Protect.**

A simulated astronaut health monitoring and decision-support dashboard developed for the **2026 NASA Space Apps Challenge**.

## 🌌 About the Project

CrewPulse is a prototype designed to demonstrate how astronaut health indicators can be monitored throughout a space mission.

It brings together simulated health readings, personal baseline comparisons, interactive trend visualisations and an illustrative alert system in one mission-control dashboard.

The goal is to make unusual changes and repeated patterns easier to identify and review.

## 🎯 Problem Statement

Astronauts experience challenging conditions during space missions that can affect physical health, sleep and behavioural wellbeing.

Monitoring multiple health indicators over time can help mission teams understand changes in an astronaut's condition and identify patterns that may require further investigation.

## 💡 Our Solution

CrewPulse provides a centralised dashboard to monitor four key indicators:

- ❤️ Heart rate
- 🌡️ Body temperature
- 😴 Sleep duration
- 🧠 Wellness score

The application compares readings against an individual baseline, displays mission trends and identifies unusual changes using configurable demonstration rules.

## ✨ Key Features

### 1. Mission Health Overview
Displays the selected astronaut's current health indicators.

### 2. Interactive Health Trends
Visualises heart rate, temperature, sleep and wellness changes across mission days.

### 3. Personal Health Baseline
Uses the first five simulated mission days to establish a personal reference point.

### 4. Intelligent Mission Alerts
Identifies unusual changes in health indicators using configurable rules.

### 5. Persistent Pattern Detection
Checks a three-day window to identify repeated unusual signals.

### 6. Mission Data Explorer
Allows users to inspect the underlying simulated health records.

## 🛰️ NASA Research References

CrewPulse's monitoring concepts are informed by NASA research resources:

| Research resource | Relevance |
|---|---|
| NASA Open Science Data Repository (OSDR) | Space biology and human spaceflight research |
| SSM_Actigraphy | Sleep time, sleep efficiency and awakenings |
| SSM_Sleep_Quality | Sleep quality, sleep quantity, tiredness, energy and stress |
| NASA Human Research Program | Astronaut health and performance research |

**NASA resources:**

- [NASA OSDR](https://osdr.nasa.gov/bio/repo/)
- [NASA Life Sciences Portal](https://nlsp.nasa.gov/)
- [NASA Human Research Program](https://www.nasa.gov/hrp/)

The referenced Standard Measures datasets are restricted-access and require a data request. Actual NASA datasets have not been integrated into this prototype.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Interactive dashboard |
| Pandas | Data processing |
| Plotly | Interactive charts |
| CSV | Simulated health dataset |

## 📊 Dataset

The current prototype uses simulated demonstration data:

- 2 demonstration astronaut profiles
- 30 mission days per profile
- 60 total records
- 4 health indicators

The data is not sourced from actual astronaut medical records.

## 🚨 Alert Logic

CrewPulse currently uses illustrative rules to identify changes from the personal baseline:

| Indicator | Demonstration rule |
|---|---|
| Heart rate | Absolute change of at least 10% |
| Body temperature | Absolute change of at least 0.5°C |
| Sleep duration | Decrease of at least 1 hour |
| Wellness score | Decrease of at least 10 points |

Repeated signals are checked over the selected day and the preceding two days.

Alert levels are demonstration classifications, not clinical risk classifications.

## 💻 Installation and Setup

### Requirements

- Python 3.10 or later
- Visual Studio Code (recommended)
- Git (recommended)

### 1. Clone the repository

```bash
git clone https://github.com/Ankit-kumar-develop/CrewPulse.git
cd CrewPulse
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install streamlit pandas plotly
```

### 5. Run CrewPulse

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal, usually:

```text
http://localhost:8501
```

## 📁 Project Structure

```text
CrewPulse/
│
├── app.py
│
├── data/
│   └── astronaut_health.csv
│
├── README.md
│
└── .gitignore
```

## 🔮 Future Development

- Integration of approved and accessible NASA research datasets.
- Wearable sensor integration.
- More advanced anomaly detection.
- Expanded sleep and behavioural health monitoring.
- Improved mission-control reporting.

## ⚠️ Disclaimer

CrewPulse is an educational prototype developed for the NASA Space Apps Challenge 2026.

All current readings are simulated. The alert thresholds and wellness score are illustrative and have not been clinically validated or approved by NASA.

CrewPulse is not a medical device, does not provide medical diagnoses and does not currently connect to live astronaut telemetry.

## 👥 Team

Developed by a two-member team for the NASA Space Apps Challenge 2026.

## 🚀 Project Motto

**CrewPulse — Monitor. Detect. Protect.**