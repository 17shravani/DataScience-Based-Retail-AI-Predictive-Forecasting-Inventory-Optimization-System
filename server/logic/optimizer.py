import numpy as np
from scipy.optimize import minimize

class PriceOptimizer:
    """Uses SciPy's SLSQP to find the optimal price point based on demand elasticity."""
    
    def __init__(self, cost=20.0, base_price=35.0, base_demand=100.0, elasticity=1.5):
        self.cost = cost
        self.base_price = base_price
        self.base_demand = base_demand
        self.elasticity = elasticity # |e| > 1 means elastic

    def _demand_model(self, price):
        """Constant Elasticity Demand Model: D = A * P^(-e)"""
        return self.base_demand * (price / self.base_price)**(-self.elasticity)

    def _objective_function(self, price):
        """Minimize Negative Profit -> Maximize Profit"""
        demand = self._demand_model(price)
        profit = (price - self.cost) * demand
        return -profit

    def optimize(self, price_bounds=(25.0, 60.0)):
        """Finds the 'Sweet Spot' price within constraints."""
        initial_guess = self.base_price
        
        # Constraints: price must be within bounds
        bounds = [price_bounds]
        
        res = minimize(
            self._objective_function, 
            initial_guess, 
            bounds=bounds, 
            method='SLSQP'
        )
        
        opt_price = float(res.x[0])
        opt_demand = self._demand_model(opt_price)
        opt_profit = (opt_price - self.cost) * opt_demand
        
        return {
            "optimal_price": round(opt_price, 2),
            "expected_demand": round(opt_demand, 1),
            "expected_profit": round(opt_profit, 2),
            "margin_pct": round(((opt_price - self.cost) / opt_price) * 100, 1),
            "is_converged": res.success
        }

    def simulate_curve(self, range_start=20, range_end=100, points=50):
        """Simulates the profit curve for visualization."""
        prices = np.linspace(range_start, range_end, points)
        profits = [ (p - self.cost) * self._demand_model(p) for p in prices ]
        return {"prices": prices.tolist(), "profits": profits}
