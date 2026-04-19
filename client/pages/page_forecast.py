import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from ml_engine import generate_forecast, get_feature_importance
from datetime import datetime, timedelta

def render_forecast_engine(df):
    st.title("Forecast Transparency & Explainability 📈")
    st.markdown("<p class='themeable-text'>Interactive Demand Forecasting with ML Explainability (XAI).</p>", unsafe_allow_html=True)
    
    col_main, col_sidebar = st.columns([3, 1])
    
    with col_sidebar:
        st.markdown("### 🎚️ Controls")
        st.markdown("##### Simulate Global Price Change (%)")
        price_sim = st.slider("Adjust Global Pricing", min_value=-10, max_value=20, value=0, step=1)
        
        st.markdown("---")
        sku_options = df['item_id'].head(20).tolist()
        selected_sku = st.selectbox("Analyze Specific SKU", sku_options)
        
        sku_data = df[df['item_id'] == selected_sku].iloc[0]
        
    with col_main:
        st.markdown("### 📈 Demand Forecast Simulator")
        
        # Generate Forecast Model
        history = list(sku_data['sales_history'])
        forecast = generate_forecast(
            history, 
            price_change_pct=price_sim, 
            seasonality=sku_data['seasonality_index'],
            is_promo=sku_data['promo_flag']
        )
        
        # Plotting
        days_history = len(history)
        days_forecast = len(forecast)
        
        # Dates for X-axis
        base_date = datetime.now()
        dates_hist = [(base_date - timedelta(days=x)).strftime("%Y-%m-%d") for x in range(days_history, 0, -1)]
        dates_fore = [(base_date + timedelta(days=x)).strftime("%Y-%m-%d") for x in range(1, days_forecast + 1)]
        
        fig_ts = go.Figure()
        
        # Actual Data
        fig_ts.add_trace(go.Scatter(
            x=dates_hist, 
            y=history,
            mode='lines+markers',
            name='Actual Demand',
            line=dict(color='#3B82F6', width=2),
            marker=dict(size=4)
        ))
        
        # Forecast Data (connector point to make line continuous)
        x_fore = [dates_hist[-1]] + dates_fore
        y_fore = [history[-1]] + forecast
        
        fig_ts.add_trace(go.Scatter(
            x=x_fore, 
            y=y_fore,
            mode='lines+markers',
            name='Predicted Demand',
            line=dict(color='#8B5CF6', width=3, dash='dash'),
            marker=dict(size=5),
            hovertemplate="Date: %{x}<br>Final Forecast: %{y} units<extra></extra>"
        ))
        
        fig_ts.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', 
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='#E2E8F0',
            hovermode="x unified",
            margin=dict(l=0, r=0, t=10, b=0),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_ts, use_container_width=True)
        
        st.markdown("### 📊 ML Feature Importance (XAI)")
        st.caption("SHAP Values: Understanding what drives the predictive model.")
        
        importance_df = get_feature_importance()
        
        fig_xai = px.bar(
            importance_df, 
            x='Importance', 
            y='Feature', 
            orientation='h',
            color='Importance',
            color_continuous_scale='Purp'
        )
        fig_xai.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', 
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='#E2E8F0',
            margin=dict(l=0, r=0, t=20, b=0),
            height=250
        )
        st.plotly_chart(fig_xai, use_container_width=True)
