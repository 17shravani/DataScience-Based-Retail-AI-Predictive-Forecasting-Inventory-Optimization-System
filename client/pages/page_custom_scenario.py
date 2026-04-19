import streamlit as st
import numpy as np

def render_custom_scenario():
    st.title("Custom Scenario Builder 🛠️")
    st.markdown("<p class='themeable-text'>Manually input SKU data to see how the AI resolves Stockouts and Overstocking issues dynamically.</p>", unsafe_allow_html=True)
    
    st.markdown("### Input Retail Parameters")
    
    with st.form("custom_sku_form"):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("**Financials**")
            cost = st.number_input("Unit Cost ($)", value=25.0, min_value=1.0)
            base_price = st.number_input("Current Selling Price ($)", value=45.0, min_value=1.0)
            competitor_price = st.number_input("Competitor Price ($)", value=40.0, min_value=1.0)
            
        with col2:
            st.markdown("**Inventory & Demand**")
            inventory = st.number_input("Current Inventory (Units)", value=200, min_value=0)
            demand_mean = st.number_input("Average Daily Demand (Units)", value=15.0, min_value=0.1)
            
        with col3:
            st.markdown("**External Factors**")
            seasonality = st.slider("Seasonality Index (1.0 = normal)", 0.5, 2.0, 1.2)
            is_promo = st.checkbox("Currently on Promotion?")
            
        submit_btn = st.form_submit_button("Run AI Optimization")
        
    if submit_btn:
        st.markdown("<hr style='border-color:#2A303C'>", unsafe_allow_html=True)
        st.markdown("### 🔍 The Problem Statement Diagnosis")
        
        # 1. Capital Tie-Up (Overstocking)
        capital_tied = inventory * cost
        days_of_supply = inventory / demand_mean if demand_mean > 0 else 0
        
        # 2. Stockout Risk
        stockout_risk_score = 100 - np.clip(days_of_supply / 14 * 100, 0, 100)
        
        diag1, diag2 = st.columns(2)
        with diag1:
            st.warning(f"**Capital Tied Up (Overstock Risk):** ${capital_tied:,.2f}")
            st.caption(f"You have {days_of_supply:.1f} days of supply. Holding excess inventory drastically drains working capital and requires eventual discounting.")
            
        with diag2:
            st.error(f"**Stockout Risk Score:** {stockout_risk_score:.1f}%")
            if stockout_risk_score > 70:
                st.caption("WARNING: Inventory is dangerously low compared to current velocity. Prepare to lose imminent revenue due to out-of-stock items.")
            else:
                st.caption("Inventory levels are currently adequate for short-term demand.")
                
        st.markdown("### 🤖 Prescriptive AI Solution")
        
        # Optimized Logic
        elasticity_factor = -2.0 
        optimal_markup = -1 / (1 + elasticity_factor)
        optimal_price = cost * optimal_markup if elasticity_factor < -1 else base_price
        
        if competitor_price > base_price * 1.05:
            optimal_price = min(optimal_price, competitor_price * 0.98)
            
        optimal_price = np.clip(optimal_price, base_price * 0.85, base_price * 1.15)
        
        # Recalculate projected velocity and ROI using ML engine simulation logic
        price_diff_pct = (optimal_price - base_price) / base_price
        new_daily_demand = demand_mean * (1 - (price_diff_pct * 2.0)) * seasonality
        new_velocity = new_daily_demand if not is_promo else new_daily_demand * 1.3
        
        st.success(f"**AI Recommended Price Adjustment:** Change from ${base_price:.2f} to **${optimal_price:.2f}**")
        
        sol1, sol2 = st.columns(2)
        with sol1:
            st.info(f"- **Simulated New Velocity:** {new_velocity:.1f} units/day")
        with sol2:
            st.info(f"- **ROI Improvement:** Moving closer to the absolute constraint boundary of competitor framing (${competitor_price:.2f}) maximizes Gross Margin Return on Inventory.")
