# ⚡ NEXUS: Codeforces Intelligence Engine

> An advanced algorithmic telemetry, difficulty spectrum mapping, and dynamic practice charting system built to analyze competitive programming telemetry and engineer targeted skill progression.

[![Live Demo](https://img.shields.io/badge/Streamlit-Live_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://codeforces-nexus-analytics.streamlit.app)
[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/SURYANSH-55555/codeforces-nexus-analytics)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

---

## 📌 Executive Overview

**NEXUS** transforms raw submission history from the Codeforces platform into actionable competitive programming intelligence. Instead of manually sifting through unsolved problem archives, NEXUS processes real-time telemetry from the official Codeforces REST API to evaluate problem-solving patterns, isolate domain weaknesses, and compute personalized progression ladders.

Key engineering goals:
* Eliminate bias towards over-practiced topics by mapping tag density distributions.
* Automate rating ladder escalation ($+100$, $+200$, and $+300$ delta targets above median solved difficulty).
* Provide a high-density, low-latency dark terminal user interface for effortless diagnostics during practice sessions.

---

## 🔬 Core System Architecture & Logic
┌───────────────────────┐
│ Codeforces REST API   │
└───────────┬───────────┘
│ (Raw JSON Data Ingestion)
▼
┌───────────────────────┐
│ Pipeline & Cleaning   │ ◄── Deduplication, Time Normalization,
└───────────┬───────────┘     Administrative Tag Stripping
│
▼
┌───────────────────────┐
│ Analytics & Modeling  │ ◄── Active Range Filtering, Median Target Logic,
└───────────┬───────────┘     Tag Density Calculations
│
▼
┌───────────────────────┐
│ Dynamic UI Component  │ ◄── Custom CSS Terminal Theme, Streamlit Metrics,
└───────────────────────┘     Interactive Distribution Charts


### 1. Telemetry Ingestion & Data Pipeline
The core data ingestion module interacts with `https://codeforces.com/api/user.status` to extract submission logs.
* **Deduplication:** Filters out repeated attempts, retaining only unique Verdicts (`VERDICT_OK` / `OK`).
* **Tag Cleansing:** Strips administrative/meta tags (such as `*special`, `interactive`, or unrated problems) to prevent skewing skill distribution metrics.
* **Bounded Filtering:** Allows configurable rating bounds ($800 - 3500$) to isolate active performance zones from historical or warm-up submissions.

### 2. Predictive Practice Escalation Ladder
To optimize rating growth without inducing cognitive fatigue, NEXUS calculates an **Adaptive Growth Target**:
1. Computes the user's **Median Solved Rating** within the active filter bounds.
2. Constructs a progressive progression ladder:
   * **Base Target:** $\text{Median Rating} + 100$ (Optimal Consistency Zone)
   * **Stretch Target:** $\text{Median Rating} + 200$ (Growth/Push Zone)
   * **Peak Target:** $\text{Median Rating} + 300$ (Boundary Challenge Zone)

### 3. Tag Density Analysis
Aggregates topic frequencies across algorithm tags (e.g., *Dynamic Programming*, *Graphs*, *Number Theory*, *Greedy*, *Data Structures*) to illuminate topic over-reliance versus underdeveloped areas.

---

## 🛠️ Tech Stack & Dependencies

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Language** | Python 3.9+ | Core application logic and algorithmic processing |
| **UI Framework** | Streamlit | Rapid front-end rendering and interactive state management |
| **Data Engine** | Pandas | High-performance DataFrame indexing, grouping, and aggregation |
| **Networking** | Requests | Asynchronous HTTP polling of official Codeforces API endpoints |
| **Styling** | Custom CSS / Markdown | Sleek, dark terminal dashboard aesthetic |

---

## 🚀 Local Installation & Setup

Want to run NEXUS on your local environment?

### Prerequisites
* Python 3.9 or higher
* Git

### Step-by-Step Instructions

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/SURYANSH-55555/codeforces-nexus-analytics.git](https://github.com/SURYANSH-55555/codeforces-nexus-analytics.git)
   cd codeforces-nexus-analytics
Create & Activate a Virtual Environment (Recommended)

Bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
Install Dependencies

Bash
pip install -r requirements.txt
Launch the Streamlit Server

Bash
streamlit run app.py
The application will automatically launch in your default browser at http://localhost:8501.

📁 Repository Structure
codeforces-nexus-analytics/
│
├── app.py                 # Main Streamlit application and UI layout logic
├── python_processdata.py  # API communications, pipeline cleaning, & metrics processing
├── requirements.txt       # Production dependency manifest
├── LICENSE                # MIT Open Source License
└── README.md              # Project documentation
🤝 Contributing
Contributions, feedback, and bug reports are welcome!

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git checkout -b feature/AmazingFeature)

Open a Pull Request

📜 License
Distributed under the MIT License. See LICENSE for more information.


---
## 👤 Author

**Suryansh**
* GitHub: [@SURYANSH-55555](https://github.com/SURYANSH-55555)
* Project: [NEXUS Codeforces Intelligence Engine](https://codeforces-nexus-analytics.streamlit.app)
