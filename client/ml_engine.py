import pandas as pd
import numpy as np

def optimize_price(df):
    """
    Simulates a Price Optimization ML Model.
    Calculates elasticity based on competitor price and current price.
    """
    recommendations = []
    
    for _, row in df.iterrows():
        base_p = row['price']
        comp_p = row['competitor_price']
        cost = row['cost']
        
        # Simple elasticity assumption (-1.5 to -2.5)
        elasticity = -2.0
        
        # Optimal price formulation for linear demand curve
        # Markup = -1 / (1 + elasticity)
        # Assuming constant elasticity, optimal price:
        optimal_price = cost * (elasticity / (1 + elasticity)) if elasticity < -1 else base_p
        
        # Constrain the optimization so it doesn't move too radically (+/- 15%)
        lower_bound = base_p * 0.85
        upper_bound = base_p * 1.15
        
        # If competitor ratio is high, we can price higher
        if comp_p > base_p * 1.05:
            optimal_price = min(optimal_price, comp_p * 0.98) # slightly undercut
            
        optimal_price = np.clip(optimal_price, lower_bound, upper_bound)
        
        recommendations.append(round(optimal_price, 2))
        
    df['recommended_price'] = recommendations
    return df

def generate_forecast(history, price_change_pct, seasonality, is_promo):
    """
    Simulates a time-series forecast (e.g. ARIMA / Random Forest)
    Returns list of 30 future demand points.
    """
    recent_mean = np.mean(history[-14:]) if len(history) >= 14 else np.mean(history)
    recent_std = np.std(history[-14:]) if len(history) >= 14 else np.std(history)
    
    # Elasticity effect
    price_effect = 1.0 - (price_change_pct / 100.0 * 2.0) # E.g. -10% price -> +20% demand
    
    # Promo effect
    promo_effect = 1.3 if is_promo else 1.0
    
    forecast = []
    base_trend = recent_mean * price_effect * promo_effect * seasonality
    
    for i in range(30):
        # Add random noise and slight weekly cyclicality
        day_of_week_effect = 1.0 + 0.2 * np.sin(i * (2 * np.pi / 7))
        noise = np.random.normal(0, recent_std * 0.5)
        val = max(0, int(base_trend * day_of_week_effect + noise))
        
        # Inject occasional spikes
        if np.random.random() < 0.05:
            val = int(val * 1.8)
            
        forecast.append(val)
        
    return forecast

def get_feature_importance():
    """Returns synthetic SHAP values for Explainable AI (XAI) feature importance chart."""
    return pd.DataFrame({
        'Feature': ['competitor_price', 'seasonality_index', 'promo_flag', 'inventory_level', 'historical_velocity'],
        'Importance': [0.35, 0.25, 0.15, 0.10, 0.15]
    }).sort_values(by='Importance', ascending=True)
