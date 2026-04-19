import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def render_supply_chain(df):
    st.title("Supply Chain Intelligence 📦")
    st.markdown("<p class='themeable-text'>Optimizing working capital through ABC-XYZ analysis and automated risk detection.</p>", unsafe_allow_html=True)
    
    selected_sku = st.selectbox("Select SKU for AI Report", df['item_id'].head(50))
    sku_data = df[df['item_id'] == selected_sku].iloc[0]
    
    st.markdown("### 🤖 AI Justification Report")
    
    # Generate dynamic text based on the SKU's data
    momentum = "high sales momentum" if sku_data['recent_30d_sales'] > sku_data['demand_mean'] * 30 else "stable demand"
    promo_status = "recent promotions" if sku_data['promo_flag'] == 1 else "organic seasonal surges"
    action = "expedite replenishment" if sku_data['urgency'] in ['HIGH', 'CRITICAL'] else "maintain current inventory levels"
    
    justification_text = f"""
    > **Model Insight:** The system detected {momentum} from {promo_status} with a Seasonality Index of {sku_data['seasonality_index']}.
    > **Recommendation:** Optimal order recommendation is to {action}. This balances holding costs (currently at {sku_data['inventory']} units) vs. a {sku_data['stockout_risk_score']:.1f}% stockout risk, maximizing GMROI.
    """
    st.info(justification_text)
    
    st.markdown("<hr style='border-color: #2A303C;'>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📊 Inventory Prioritization Matrix")
        st.caption("ABC/XYZ Classification showing Revenue impact vs Predictability")
        
        # Priority mapping for color
        priority_map = {
            'AX': 'P1 (Critical)', 'AY': 'P1 (Critical)', 'AZ': 'P2 (High)',
            'BX': 'P2 (High)',     'BY': 'P3 (Med)',      'BZ': 'P3 (Med)',
            'CX': 'P3 (Med)',      'CY': 'P4 (Low)',      'CZ': 'P4 (Low)'
        }
        
        matrix_df = df.copy()
        matrix_df['Priority'] = matrix_df['abc_xyz'].map(priority_map)
        
        fig1 = px.scatter(
            matrix_df, 
            x='abc_rank', 
            y='xyz_rank', 
            size='inventory', 
            color='Priority',
            hover_name='item_id',
            category_orders={"abc_rank": ["C", "B", "A"], "xyz_rank": ["Z", "Y", "X"]},
            color_discrete_map={
                'P1 (Critical)': '#EF4444', 
                'P2 (High)': '#F59E0B', 
                'P3 (Med)': '#3B82F6', 
                'P4 (Low)': '#10B981'
            }
        )
        fig1.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', 
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='#E2E8F0',
            margin=dict(l=20, r=20, t=20, b=20)
        )
        st.plotly_chart(fig1, use_container_width=True)
        
    with col2:
        st.markdown("### 📉 Stockout Risk Distribution")
        st.caption("Risk scores segregated by ABC revenue classifications.")
        
        fig2 = px.histogram(
            df, 
            x="stockout_risk_score", 
            color="abc_rank",
            nbins=20,
            category_orders={"abc_rank": ["A", "B", "C"]},
            color_discrete_map={'A': '#8B5CF6', 'B': '#EC4899', 'C': '#14B8A6'},
            barmode='stack'
        )
        fig2.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', 
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='#E2E8F0',
            margin=dict(l=20, r=20, t=20, b=20),
            xaxis_title="Stockout Risk Score (0-100)",
            yaxis_title="Number of SKUs"
        )
        st.plotly_chart(fig2, use_container_width=True)
