import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

def croston_method(ts, extra_periods=1, alpha=0.1):
    """
    Croston's Method for intermittent demand forecasting.
    Estimates the demand magnitude and time-between-demands separately.
    """
    ts = np.array(ts)
    n = len(ts)
    
    # Initialization
    a = np.zeros(n + 1) # Demand magnitude
    p = np.zeros(n + 1) # Inter-arrival period
    q = 1 # Time since last demand
    
    # Starting values
    first_non_zero = ts[ts > 0]
    if len(first_non_zero) == 0:
        return np.zeros(extra_periods)
        
    a[0] = first_non_zero[0]
    p[0] = n / len(first_non_zero) # Simple average inter-arrival
    
    for t in range(n):
        if ts[t] > 0:
            a[t+1] = alpha * ts[t] + (1 - alpha) * a[t]
            p[t+1] = alpha * q + (1 - alpha) * p[t]
            q = 1
        else:
            a[t+1] = a[t]
            p[t+1] = p[t]
            q += 1
            
    # Forecast
    forecast_value = a[n] / p[n] if p[n] != 0 else 0
    return np.full(extra_periods, forecast_value)

class HybridForecaster:
    """Combines ML (Random Forest) for stable items and Croston for intermittent ones."""
    
    def __init__(self):
        self.rf_model = RandomForestRegressor(n_estimators=50, random_state=42)

    def forecast(self, history, demand_type="stable", periods=7):
        """
        Chooses the best model based on demand characteristics.
        - Stable: Random Forest
        - Intermittent (Lumpy): Croston
        """
        if demand_type == "intermittent" or np.count_nonzero(history) / len(history) < 0.5:
            # Use Croston for sparse data
            return croston_method(history, extra_periods=periods).tolist()
        else:
            # Simple simulation of RF forecasting for demo
            # In real system, we'd use lag features
            last_val = history[-1]
            trend = (history[-1] - history[0]) / len(history)
            forecast = [max(0, last_val + (trend * i) + np.random.normal(0, 1)) for i in range(1, periods + 1)]
            return forecast
