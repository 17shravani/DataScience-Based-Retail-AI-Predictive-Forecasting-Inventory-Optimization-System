class AdvisorAgent:
    """Communication Agent: Provides NLP interface and explains AI logic."""
    
    def __init__(self):
        pass

    def explain_action(self, event, strategy, action):
        """Generates a human-readable explanation of the system's actions."""
        if not event or not strategy or not action:
            return "System state: Normal operations. No autonomous actions required."
            
        return (
            f"Alert: {event['description']} at {event['location']}. "
            f"Action: ZenithFlow autonomously triggered '{strategy['recommendation']['name']}'. "
            f"Rationale: This path was selected to achieve a {strategy['recommendation']['recovery_time']} recovery "
            f"with a {strategy['recommendation']['risk_reduction']} risk reduction profile."
        )
