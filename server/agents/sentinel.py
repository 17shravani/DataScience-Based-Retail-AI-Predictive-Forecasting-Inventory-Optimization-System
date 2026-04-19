import random
from datetime import datetime

class SentinelAgent:
    """Monitoring Agent: Detects anomalies and global risks."""
    
    def __init__(self, world_engine):
        self.world_engine = world_engine
        self.risk_threshold = 30

    async def scan_global_signals(self):
        """Scans the world engine for new events and calculates risk impact."""
        snapshot = self.world_engine.get_snapshot()
        current_risk = snapshot.get("global_risk_index", 0)
        
        findings = []
        if current_risk > self.risk_threshold:
            findings.append({
                "agent": "Sentinel",
                "severity": "High" if current_risk > 60 else "Medium",
                "finding": f"Elevated Risk Index detected: {current_risk}",
                "timestamp": datetime.now().isoformat()
            })
            
        return findings

    def get_anomalies(self):
        # In a real scenario, this would use ML to detect statistical deviations
        # For now, we use the detected events from the world engine
        events = self.world_engine.events
        return events
