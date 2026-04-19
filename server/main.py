import asyncio
import json
import random
import numpy as np
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from .logic.forecaster import HybridForecaster
from .logic.optimizer import PriceOptimizer
from .logic.inventory_science import InventoryScience

app = FastAPI(title="Retail AI Intelligence Server")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Logic
forecaster = HybridForecaster()
inventory_engine = InventoryScience()

# --- Mock Retail Data Engine ---
def generate_inventory_state():
    skus = []
    names = ["Nike Air Max", "Tech Fleece Hoodie", "Elite Running Shorts", "Gym Duffel Bag", "Yoga Mat Premium"]
    for i, name in enumerate(names):
        # Generate 30 days of synthetic demand
        avg_demand = random.uniform(5, 50)
        is_intermittent = random.random() < 0.3
        if is_intermittent:
            history = [random.choice([0, 0, random.randint(10, 30)]) for _ in range(30)]
        else:
            history = [max(0, int(np.random.normal(avg_demand, 5))) for _ in range(30)]
            
        skus.append({
            "id": f"SKU-{100+i}",
            "name": name,
            "category": "Apparel" if i < 3 else "Accessories",
            "price": 80.0 + (i * 20),
            "stock_on_hand": random.randint(20, 150),
            "demand_history": history,
            "revenue": sum(history) * (80.0 + (i * 20))
        })
    
    # Classify SKUs
    skus = inventory_engine.classify(skus)
    
    # Add Replenishment & Forecasts
    for sku in skus:
        sku["replenishment"] = inventory_engine.calculate_replenishment(sku)
        sku["forecast_7d"] = forecaster.forecast(
            sku["demand_history"], 
            demand_type="intermittent" if sku["xyz"] == "Z" else "stable"
        )
        
    return skus

@app.get("/")
async def root():
    return {"status": "Retail AI Core Active"}

@app.get("/optimize-price/{sku_id}")
async def optimize_price(sku_id: str):
    # Simulate finding SKU data
    optimizer = PriceOptimizer(cost=45.0, base_price=89.0, base_demand=120.0, elasticity=1.8)
    return optimizer.optimize()

@app.websocket("/ws/retail-stream")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # Generate real-time snapshot
            data = generate_inventory_state()
            
            # Global KPIs
            kpis = {
                "total_revenue": sum(s["revenue"] for s in data),
                "avg_sell_through": round(random.uniform(0.65, 0.85), 2),
                "stockout_risk_count": len([s for s in data if s["stock_on_hand"] < s["replenishment"]["reorder_point"]]),
                "gmroii": round(random.uniform(2.5, 4.2), 2)
            }
            
            payload = {
                "skus": data,
                "kpis": kpis,
                "timestamp": __import__("datetime").datetime.now().isoformat()
            }
            
            await websocket.send_text(json.dumps(payload))
            await asyncio.sleep(5)  # Update every 5 seconds
    except WebSocketDisconnect:
        pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
