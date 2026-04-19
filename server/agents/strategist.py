import random

class StrategistAgent:
    """Decision Agent: Optimizes resilience paths and solves multi-objective problems."""
    
    def __init__(self, world_engine):
        self.world_engine = world_engine

    def evaluate_contingencies(self, event):
        """Simulates different paths and returns the optimal recovery strategy."""
        if not event:
            return None
            
        # Strategy Logic: Cost vs Time vs Risk
        strategies = [
            {"name": "Aggressive Reroute", "cost_impact": "+15%", "recovery_time": "-48h", "risk_reduction": "High"},
            {"name": "Diversified Sourcing", "cost_impact": "+8%", "recovery_time": "-12h", "risk_reduction": "Medium"},
            {"name": "Buffer Utilization", "cost_impact": "+2%", "recovery_time": "+12h", "risk_reduction": "Low"}
        ]
        
        # Select the best based on event severity
        if event.get("severity") == "High":
             recommendation = strategies[0]
        else:
             recommendation = strategies[1]
             
        return {
            "agent": "Strategist",
            "event_linked": event.get("id"),
            "recommendation": recommendation,
            "rationale": f"Based on {event['type']} event severity, maximizing impact reduction."
        }
