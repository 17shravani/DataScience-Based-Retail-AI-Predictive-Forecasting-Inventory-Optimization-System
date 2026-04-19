import random
import time
import asyncio
from datetime import datetime, timedelta

class WorldEngine:
    def __init__(self):
        self.vessels = self._init_vessels()
        self.ports = ["Suez", "Singapore", "Rotterdam", "Hamburg", "Long Beach", "Shanghai"]
        self.events = []
        self.base_risk_score = 15

    def _init_vessels(self):
        vessels = []
        names = ["Ocean Titan", "Stella Maris", "Global Mariner", "Everest Express", "Pacific Voyager"]
        for i, name in enumerate(names):
            vessels.append({
                "id": f"V-{100 + i}",
                "name": name,
                "lat": random.uniform(-20, 50),
                "lng": random.uniform(-100, 150),
                "status": "In Transit",
                "destination": random.choice(["Rotterdam", "Singapore", "Suez"]),
                "cargo_value": random.randint(5000000, 50000000),
                "eta": (datetime.now() + timedelta(days=random.randint(2, 10))).isoformat()
            })
        return vessels

    async def update_state(self):
        """Simulate movement and event triggers"""
        for v in self.vessels:
            # Subtle movement
            v["lat"] += random.uniform(-0.1, 0.1)
            v["lng"] += random.uniform(-0.1, 0.1)
            
            # Random status changes
            if random.random() < 0.05:
                v["status"] = random.choice(["In Transit", "Anchored", "Port Operations"])

        # Random disruption events
        if random.random() < 0.02 and not self.events:
            event = {
                "id": f"EV-{int(time.time())}",
                "type": "Weather",
                "severity": "High",
                "location": "North Atlantic",
                "description": "Severe Tropical Storm detected near primary trade route.",
                "timestamp": datetime.now().isoformat()
            }
            self.events.append(event)
            return event
        
        return None

    def get_snapshot(self):
        return {
            "vessels": self.vessels,
            "events": self.events,
            "system_health": "Optimal" if not self.events else "Caution",
            "global_risk_index": self.base_risk_score + (len(self.events) * 45)
        }

world_engine = WorldEngine()
