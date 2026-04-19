import streamlit as st
import pandas as pd

def render_executive_center(df):
    st.title("Executive Center 📈")
    st.markdown("<p class='themeable-text'>High-level business intelligence and strategic prescriptive recommendations.</p>", unsafe_allow_html=True)
    
    st.markdown("### Executive KPIs")
    col1, col2, col3 = st.columns(3)
    
    # Calculate mock metrics based on data
    avg_sell_through = (df['recent_30d_sales'] / (df['inventory'] + 1)).mean() * 10
    projected_revenue = (df['recommended_price'] * df['demand_mean']).sum() * 30
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <p style="color: #94A3B8; font-size: 14px; margin: 0;">Avg Sell-Through</p>
            <h2 style="margin: 5px 0;">{avg_sell_through:.2f}X <span class="status-healthy" style="font-size: 16px;">Healthy</span></h2>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="metric-card">
            <p style="color: #94A3B8; font-size: 14px; margin: 0;">Avg Sell-Through Growth</p>
            <h2 style="margin: 5px 0;">~99.6% <span class="status-fast" style="font-size: 16px;">Fast</span></h2>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <p style="color: #94A3B8; font-size: 14px; margin: 0;">Projected Monthly Revenue</p>
            <h2 style="margin: 5px 0;">${projected_revenue/100000:.2f}L</h2>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br><hr style='border-color: #2A303C;'><br>", unsafe_allow_html=True)
    
    st.markdown("### 💡 Prescriptive Price Recommendations")
    st.caption("AI-driven price optimization balancing elasticity, competitor pricing, and stockout risk.")
    
    # Select columns for table
    display_df = df[['item_id', 'abc_xyz', 'price', 'competitor_price', 'recommended_price', 'gmroi', 'urgency']].copy()
    display_df = display_df.head(20).sort_values(by='urgency') # show top 20
    
    # Stylize dataframe
    # Format columns safely without breaking Pandas 3.x with Streamlit Styler issues
    display_df['price'] = display_df['price'].apply(lambda x: f"${x:.2f}")
    display_df['competitor_price'] = display_df['competitor_price'].apply(lambda x: f"${x:.2f}")
    display_df['recommended_price'] = display_df['recommended_price'].apply(lambda x: f"${x:.2f}")
    display_df['gmroi'] = display_df['gmroi'].apply(lambda x: f"{x:.2f}")
    
    st.dataframe(display_df, use_container_width=True, height=500)
