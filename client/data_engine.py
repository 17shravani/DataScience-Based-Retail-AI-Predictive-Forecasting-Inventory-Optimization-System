import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def classify_abc_xyz(df):
    # Calculate Revenue
    df['total_revenue'] = df['demand_mean'] * df['price'] * 30 # approx monthly
    df = df.sort_values(by='total_revenue', ascending=False)
    
    # Calculate cumulative percentage
    df['cum_rev'] = df['total_revenue'].cumsum()
    df['cum_rev_ptg'] = df['cum_rev'] / df['total_revenue'].sum()
    
    # ABC Classification
    def abc_class(pct):
        if pct <= 0.70: return 'A'
        if pct <= 0.90: return 'B'
        return 'C'
    df['abc_rank'] = df['cum_rev_ptg'].apply(abc_class)
    
    # XYZ Classification based on CV (Coefficient of Variation) = std/mean
    df['cv'] = df['demand_std'] / (df['demand_mean'] + 1e-5)
    def xyz_class(cv):
        if cv <= 0.5: return 'X'
        if cv <= 1.0: return 'Y'
        return 'Z'
    df['xyz_rank'] = df['cv'].apply(xyz_class)
    
    return df

def generate_synthetic_data(num_skus=150):
    np.random.seed(42)
    random.seed(42)
    
    skus = []
    
    for i in range(num_skus):
        item_id = f"SKU-{1000 + i}"
        base_price = round(random.uniform(20, 300), 2)
        base_competitor_price = round(base_price * random.uniform(0.9, 1.1), 2)
        
        # Demand characteristics
        demand_mean = random.uniform(5, 100)
        # B, C items have higher variance/volatility
        if random.random() < 0.2:
            demand_std = demand_mean * random.uniform(1.2, 2.5) # highly volatile
        else:
            demand_std = demand_mean * random.uniform(0.2, 0.8) # stable
            
        inventory_level = int(random.uniform(0, demand_mean * 15)) # 0 to 15 days of stock
        seasonality_index = round(random.uniform(0.8, 1.5), 2)
        
        # Simulate 60 days of sales history
        history = [max(0, int(np.random.normal(demand_mean, demand_std))) for _ in range(60)]
        
        # Apply seasonality to last 14 days representing current season surge
        history[-14:] = [int(h * seasonality_index) for h in history[-14:]]
        
        cost = base_price * random.uniform(0.4, 0.7) # 30%-60% margin
        
        # Calculate GMROI = Gross Margin / Average Inventory Cost
        avg_inv_cost = (inventory_level * cost) if inventory_level > 0 else (demand_mean * cost)
        gmroi = ((base_price - cost) * (sum(history[-30:]))) / avg_inv_cost if avg_inv_cost > 0 else 0
        
        skus.append({
            "item_id": item_id,
            "category": random.choice(["Electronics", "Apparel", "Home Goods", "Accessories"]),
            "price": base_price,
            "competitor_price": base_competitor_price,
            "cost": cost,
            "inventory": inventory_level,
            "demand_mean": demand_mean,
            "demand_std": demand_std,
            "seasonality_index": seasonality_index,
            "promo_flag": int(random.random() < 0.3),
            "sales_history": history,
            "recent_30d_sales": sum(history[-30:]),
            "gmroi": round(gmroi, 2)
        })
        
    df = pd.DataFrame(skus)
    df = classify_abc_xyz(df)
    
    # Calculate Stockout Risk (0-100)
    # High risk if inventory < 7 days of mean demand
    df['days_of_supply'] = df['inventory'] / (df['demand_mean'] + 1e-5)
    df['stockout_risk_score'] = 100 - np.clip(df['days_of_supply'] / 14 * 100, 0, 100)
    
    # Determine Urgency
    def get_urgency(row):
        if row['stockout_risk_score'] > 85: return "CRITICAL"
        if row['stockout_risk_score'] > 60: return "HIGH"
        return "ADEQUATE"
    df['urgency'] = df.apply(get_urgency, axis=1)
    
    # Create combined ABC-XYZ string
    df['abc_xyz'] = df['abc_rank'] + df['xyz_rank']
    
    return df
