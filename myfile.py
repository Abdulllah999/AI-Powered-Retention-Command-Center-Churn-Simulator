import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# ==========================================
# 1. PAGE CONFIGURATION & STYLING
# ==========================================
st.set_page_config(
    page_title="AI Retention Command Center",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Premium front-end banner using custom markdown tokens
st.markdown("""
    <div style="background: linear-gradient(90deg, #1e3a8a 0%, #0f172a 100%); padding: 25px; border-radius: 15px; margin-bottom: 25px;">
        <h1 style="color: white; margin: 0; font-family: sans-serif;">⚡ AI Retention Command Center</h1>
        <p style="color: #94a3b8; margin: 5px 0 0 0; font-size: 1.1rem;">Predictive Machine Learning Simulator & Customer Risk Matrix</p>
    </div>
""", unsafe_allow_html=True)

# ==========================================
# 2. DATA GENERATION PIPELINE
# ==========================================
from retention import generate_customer_data as generate_data, fit_model
@st.cache_data
def generate_customer_data():
    return generate_data()
@st.cache_resource
def train_retention_model(data):
    return fit_model(data)
df = generate_customer_data()

with st.spinner("🤖 Training predictive risk model..."):
    model, feat_imp, data_stats, evaluation = train_retention_model(df)
st.info("Synthetic educational simulator: the score approximates an invented formula, not a measured churn probability. No real customers or measured revenue growth.")
with st.expander("Held-out evaluation and baseline"):
    st.json(evaluation)

# ==========================================
# 4. SIDEBAR CONTROL & SIMULATOR
# ==========================================
st.sidebar.markdown("### 🎛️ Cohort Filters")
all_segments = list(df['Segment'].unique())
selected_segments = st.sidebar.multiselect("View Segments:", all_segments, default=all_segments)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🔮 Real-Time What-If Simulator")
st.sidebar.markdown("Modify a hypothetical customer's metrics to predict their churn risk live:")

# Generate interactive inputs based on data parameters
sim_inputs = {}
friendly_names = {
    'Monthly_Spend': "Monthly Spend ($)",
    'Tenure_Months': "Account Tenure (Months)",
    'Support_Tickets': "Support Tickets Filed",
    'Engagement_Score': "App Engagement Score (0-100)"
}

for col in ['Monthly_Spend', 'Tenure_Months', 'Support_Tickets', 'Engagement_Score']:
    min_v = float(data_stats['mins'][col])
    max_v = float(data_stats['maxs'][col])
    mean_v = float(data_stats['means'][col])
    
    # Check if column is integer based
    step_val = 1.0 if col in ['Tenure_Months', 'Support_Tickets'] else (max_v - min_v) / 100
    
    sim_inputs[col] = st.sidebar.slider(
        label=friendly_names[col],
        min_value=min_v,
        max_value=max_v,
        value=mean_v,
        step=step_val
    )

# Filter global dataframe based on user selections
filtered_df = df[df['Segment'].isin(selected_segments)]

# ==========================================
# 5. FRONT-END INTERFACE: KPI METRICS
# ==========================================
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.metric(label="Synthetic Monthly Spend", value=f"${filtered_df['Monthly_Spend'].sum():,.0f}")
with m2:
    st.metric(label="Avg Account Longevity", value=f"{filtered_df['Tenure_Months'].mean():.1f} Months" if len(filtered_df) else "No data")
with m3:
    st.metric(label="Mean Engagement Rating", value=f"{filtered_df['Engagement_Score'].mean():.1f} / 100" if len(filtered_df) else "No data")
with m4:
    critical_churn_count = len(filtered_df[filtered_df['Churn_Risk'] > 75])
    st.metric(label="High Risk Anomalies", value=critical_churn_count, delta=f"{critical_churn_count/len(df)*100:.1f}% base", delta_color="inverse")

st.markdown("---")

# ==========================================
# 6. VISUALIZATION LAYOUT GRID
# ==========================================
col1, col2 = st.columns([6, 4])

with col1:
    st.markdown("### 📊 Portfolio Matrix (Spend vs. Engagement)")
    fig_scatter = px.scatter(
        filtered_df, 
        x="Monthly_Spend", 
        y="Engagement_Score",
        size="Monthly_Spend",
        color="Segment",
        hover_data=['CustomerID', 'Churn_Risk'],
        color_discrete_sequence=px.colors.qualitative.Bold,
        labels={"Monthly_Spend": "Monthly Spend ($)", "Engagement_Score": "Engagement Score"}
    )
    fig_scatter.update_layout(
        margin=dict(l=10, r=10, t=10, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

with col2:
    st.markdown("### 🔮 Real-Time Prediction Gauge")
    
    # Construct input dataframe for the model prediction
    input_df = pd.DataFrame([sim_inputs])
    predicted_churn = model.predict(input_df)[0]
    
    # Styled Indicator Chart
    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=predicted_churn,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Synthetic Risk Score (0–100)", 'font': {'size': 16}},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "#ef4444" if predicted_churn > 60 else "#3b82f6"},
            'steps': [
                {'range': [0, 40], 'color': "#e2e8f0"},
                {'range': [40, 70], 'color': "#cbd5e1"},
                {'range': [70, 100], 'color': "#94a3b8"}
            ],
        }
    ))
    fig_gauge.update_layout(margin=dict(l=20, r=20, t=40, b=20), height=350)
    st.plotly_chart(fig_gauge, use_container_width=True)

st.markdown("---")

# ==========================================
# 7. BUSINESS INSIGHTS & FEATURE ATTRIBUTION
# ==========================================
infra_left, infra_right = st.columns([5, 5])

with infra_left:
    st.markdown("### 🧬 Global ML Model Feature Importance")
    fig_imp = px.bar(
        feat_imp, 
        x='Importance', 
        y='Feature', 
        orientation='h',
        color='Importance',
        color_continuous_scale='Blues'
    )
    fig_imp.update_layout(
        margin=dict(l=10, r=10, t=10, b=10),
        yaxis={'categoryorder':'total ascending'},
        height=250,
        showlegend=False
    )
    st.plotly_chart(fig_imp, use_container_width=True)

with infra_right:
    st.markdown("### 💡 Illustrative Scenario Note")
    
    # Dynamic insight text generation based on the ML prediction outcome
    if predicted_churn > 70:
        st.error(f"🚨 **High synthetic score:** Simulated parameters generate a **{predicted_churn:.1f}/100** synthetic risk score. The custom account exhibits high risk markers. Review this fictional scenario; no intervention effect is estimated.")
    elif predicted_churn > 40:
        st.warning(f"⚠️ **Precautionary Watch:** Simulated parameters yield a **{predicted_churn:.1f}/100** risk factor. The thresholds are illustrative and have not been validated for business decisions.")
    else:
        st.success(f"✅ **Account Stable:** Synthetic score is low (**{predicted_churn:.1f}/100**). This behavior profile sits well within the low-score region of the invented formula.")