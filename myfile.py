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
@st.cache_data
def generate_customer_data():
    np.random.seed(42)
    n_customers = 300
    
    segments = ['Champions', 'Loyalists', 'At Risk', 'Hibernating']
    weights = [0.30, 0.40, 0.20, 0.10]
    
    data = {
        'CustomerID': [f"CU-{i:04d}" for i in range(1001, 1001 + n_customers)],
        'Segment': np.random.choice(segments, size=n_customers, p=weights),
        'Monthly_Spend': np.random.uniform(50, 800, size=n_customers).round(2),
        'Tenure_Months': np.random.randint(2, 60, size=n_customers),
        'Support_Tickets': np.random.randint(0, 10, size=n_customers),
        'Engagement_Score': np.random.uniform(15, 100, size=n_customers).round(1)
    }
    
    df = pd.DataFrame(data)
    # Define an algorithmic ground-truth target for Churn Risk
    df['Churn_Risk'] = (100 - df['Engagement_Score'] + (df['Support_Tickets'] * 7.5)).clip(0, 100).round(1)
    return df

df = generate_customer_data()

# ==========================================
# 3. MACHINE LEARNING ENGINE
# ==========================================
@st.cache_resource
def train_retention_model(data):
    # Features (X) must be purely numeric for the model
    X = data[['Monthly_Spend', 'Tenure_Months', 'Support_Tickets', 'Engagement_Score']]
    y = data['Churn_Risk']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the Random Forest Regressor
    model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    
    # Extract Feature Importances
    importances = model.feature_importances_
    feat_imp_df = pd.DataFrame({
        'Feature': X.columns,
        'Importance': importances
    }).sort_values(by='Importance', ascending=False)
    
    # Return statistical bounds for the inputs
    stats = {
        'means': X.mean().to_dict(),
        'mins': X.min().to_dict(),
        'maxs': X.max().to_dict()
    }
    
    return model, feat_imp_df, stats

with st.spinner("🤖 Training predictive risk model..."):
    model, feat_imp, data_stats = train_retention_model(df)

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
    st.metric(label="Total Portfolio Revenue", value=f"${filtered_df['Monthly_Spend'].sum():,.0f}", delta="+14.2% MoM")
with m2:
    st.metric(label="Avg Account Longevity", value=f"{filtered_df['Tenure_Months'].mean():.1f} Months")
with m3:
    st.metric(label="Mean Engagement Rating", value=f"{filtered_df['Engagement_Score'].mean():.1f} / 100")
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
        title={'text': "Predicted Churn Probability (%)", 'font': {'size': 16}},
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
    st.markdown("### 💡 Actionable Strategic Directive")
    
    # Dynamic insight text generation based on the ML prediction outcome
    if predicted_churn > 70:
        st.error(f"🚨 **High Alert Alert:** Simulated parameters generate a **{predicted_churn:.1f}%** churn probability. The custom account exhibits high risk markers. Immediately dispatch a client success manager.")
    elif predicted_churn > 40:
        st.warning(f"⚠️ **Precautionary Watch:** Simulated parameters yield a **{predicted_churn:.1f}%** risk factor. Recommend monitoring support volumes over the next 14 business days.")
    else:
        st.success(f"✅ **Account Stable:** Churn forecast is minimal (**{predicted_churn:.1f}%**). This behavior profile sits well within the healthy portfolio benchmark metrics.")