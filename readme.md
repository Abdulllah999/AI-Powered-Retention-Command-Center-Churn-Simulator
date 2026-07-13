# ⚡ AI-Powered Retention Command Center & Churn Simulator

An eye-catching, high-performance data science dashboard built with Python and Streamlit. This application trains a Machine Learning model under the hood and allows users to simulate hypothetical customer behaviors to predict churn risk in real-time.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML--Engine-F7931E.svg)
![Vercel](https://img.shields.io/badge/Deploy-Vercel-000000.svg)

---

## 🎯 Project Overview

Bridging the gap between complex machine learning pipelines and functional corporate strategy, this **Retention Command Center** serves as a dual-purpose analytical playground. 

Instead of dealing with static plots, business managers can interactively tweak customer behaviors (e.g., support tickets filed, app engagement scores) via sidebar controllers. The app passes these inputs to a pre-trained machine learning model and returns an instantaneous, live prediction via a high-contrast visual interface.

### Key Architecture Features
* **Machine Learning Pipeline:** Trains a `RandomForestRegressor` to map correlation vectors between account engagement matrices and user churn probabilities.
* **Aggressive UI Caching:** Utilizes Streamlit's `@st.cache_resource` mechanics to keep predictive latency down to zero milliseconds during user slider updates.
* **Premium Glassmorphism UX:** Designed with custom inline HTML/CSS gradient injection, fluid typography, and high-contrast Plotly graphics.
* **Automated Logic Insights:** An rule-based text engine triggers immediate color-coded strategic response action items depending on risk probability levels.

---

## ⚙️ Repository File Structure

To deploy seamlessly, ensure your GitHub repository contains the following files in its root directory:

```text
├── app.py                  # Core Streamlit application code
├── requirements.txt        # Python dependency specifications
└── README.md               # Project documentation (this file)