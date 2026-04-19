import numpy as np

class InventoryScience:
    """Implements ABC-XYZ classification and replenishment logic."""
    
    def classify(self, skus_data):
        """
        skus_data: List of dicts with {id, revenue, demand_history}
        """
        # 1. ABC Analysis (Revenue)
        total_rev = sum(d['revenue'] for d in skus_data)
        sorted_skus = sorted(skus_data, key=lambda x: x['revenue'], reverse=True)
        
        cumulative_rev = 0
        for sku in sorted_skus:
            cumulative_rev += sku['revenue']
            share = cumulative_rev / total_rev
            if share <= 0.7:
                sku['abc'] = 'A'
            elif share <= 0.9:
                sku['abc'] = 'B'
            else:
                sku['abc'] = 'C'

        # 2. XYZ Analysis (Predictability / CoV)
        for sku in skus_data:
            history = np.array(sku['demand_history'])
            cov = np.std(history) / np.mean(history) if np.mean(history) != 0 else 999
            
            if cov <= 0.2:
                sku['xyz'] = 'X' # High predictability
            elif cov <= 0.5:
                sku['xyz'] = 'Y' # Medium
            else:
                sku['xyz'] = 'Z' # Lumpy/Unpredictable

        return skus_data

    def calculate_replenishment(self, sku, service_level=0.99):
        """Calculates Safety Stock and Reorder Point (ROP)."""
        # Safety Stock = Z-Score * StdDev_Demand * sqrt(LeadTime)
        # Assuming LeadTime = 3 days and Z-Score for 99% = 2.33
        z_score = 2.33 if sku['abc'] == 'A' else 1.64 # Slightly lower for B/C
        std_dev = np.std(sku['demand_history'])
        avg_demand = np.mean(sku['demand_history'])
        lead_time = 3
        
        safety_stock = z_score * std_dev * np.sqrt(lead_time)
        rop = (avg_demand * lead_time) + safety_stock
        
        return {
            "safety_stock": round(safety_stock, 1),
            "reorder_point": round(rop, 1),
            "recommended_order": round(avg_demand * 7, 1) # 1 week supply
        }
