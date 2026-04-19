# 🛒 Retail AI: Predictive Forecasting & Inventory Optimization System

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Machine Learning](https://img.shields.io/badge/ML-Hybrid_Forecasting-orange.svg)]()
[![Inventory Science](https://img.shields.io/badge/Inventory-ABC--XYZ_Optimization-green.svg)]()
[![Business Intelligence](https://img.shields.io/badge/BI-Financial_KPIs-red.svg)]()
[![UI/UX](https://img.shields.io/badge/UI%2FUX-Premium_Executive_Dashboard-purple.svg)]()

> **Transforming Retail Operations from Reactive to Prescriptive.** An industry-grade intelligence engine that solves the twin challenges of **Stockout Prevention** and **Working Capital Optimization** using Hybrid Machine Learning, Mathematical optimization, and a world-class UI/UX.

---

## 🛑 The Problem Statement
In the fast-paced retail sector, manual supply chain management leads to two critical operational failures:
1. **Stockouts:** Missed sales opportunities and damaged customer trust due to out-of-stock items, especially during unexpected demand spikes or seasonal shifts.
2. **Overstocking & Capital Tie-Up:** Holding dead inventory that drains working capital, incurs high warehouse holding costs, and ultimately requires deep, margin-eating discounting.

Traditional "gut-feel" and static spreadsheet models fail to capture complex retail dynamics like price elasticity, intermittent demand, and macro-trends. The result? Sub-optimal margins and operational inefficiencies.

## ⚡ Executive Summary & Real-Life Working Model
This system acts as a digital **Autonomous Supply Chain Analyst**. Imagine a national retail chain with thousands of SKUs where varying demand velocity makes manual tracking impossible. 

**How it works in the real world:**
1. **Ingest:** The system digests daily sales data, promotions, and historical trends.
2. **Predict:** It deploys tailored ML models (Random Forest for high-velocity items, Croston for slow-movers) to accurately forecast the next 30 days of demand.
3. **Prescribe:** It dynamically recalculates Safety Stock, ROP (Reorder Point), and EOQ (Economic Order Quantity). 
4. **Action:** The Store Manager opens the Executive Dashboard to find actionable, plain-English recommendations (e.g., *"Order 50 units of SKU X immediately to prevent a 95% probability of stockout by Friday"*).

---

## 💎 Outstanding UI/UX: The Executive Dashboard
Designed for C-suite executives and Supply Chain Managers, the Streamlit-powered dashboard sets a new standard for internal tools:
*   **Immersive Analytics:** Dark-mode optimized, modern glassmorphism design that feels premium, professional, and focused.
*   **Revenue Heatmaps & KPI Cards:** Instant visual visibility into GMROII (Gross Margin Return on Inventory Investment) and capital health.
*   **Stockout Risk Risk Engine:** An intuitive red/yellow/green alert system for critical inventory gaps, ensuring the user immediately knows where their attention is needed.
*   **AI Justification Narratives:** Automated, plain-English explanations detailing *why* the AI recommended a specific action, building human trust in machine-driven operations.

---

## 🛠️ Core Technical Pillars

### 1. Hybrid Demand Forecasting Engine
*   **Integrated Multi-Model Approach:** Combines **Random Forest** (for stable, high-volume demand) with **Croston & SBA (Syntetos-Boylan Approximation)** models mathematically designed for intermittent "lumpy" demand.
*   **Feature Engineering:** Extracts seasonality, promotion lift, and rolling-window statistics to capture complex macro and micro retail trends.

### 2. Prescriptive AI & Price Optimization
*   **Elasticity-Based Pricing:** Uses **SciPy’s Constrained Optimization (SLSQP)** to determine the "Sweet Spot" price that maximizes expected profit while respecting strict business constraints.
*   **Demand Sensitivity:** Dynamically calculates demand elasticity to simulate how micro-price changes will positively or negatively impact volume and margin.

### 3. Advanced Inventory Science (ABC-XYZ)
*   **ABC Analysis:** Segregates inventory by revenue contribution (Pareto Principle), ensuring you prioritize high-yield capital.
*   **XYZ Analysis:** Classifies SKUs based on demand predictability (Coefficient of Variation).
*   **Dynamic Safety Stock & ROP:** Automated calculation of Reorder Points to minimize holding costs while ensuring a **99% service level** for 'A-Class' items.

### 4. Executive Financial Intelligence
*   **GMROII Tracking:** Ensures working capital is systematically re-allocated to high-yield products rather than decaying in dead stock.
*   **Sell-Through Real-Time Metrics:** Analyzes historical vs. forecasted velocity to flag slow-moving inventory before it becomes a liability.

---

## 🚀 Visionary Feature Add-Ons (Ecosystem Roadmap)
To push this ecosystem further toward a complete Enterprise Resource Planning (ERP) module, the architecture supports:
*   **Supplier Risk Scoring:** Integrating geopolitical and localized weather data APIs to predict supplier lead-time delays and auto-adjust safety stock.
*   **Multi-Echelon Inventory Optimization (MEIO):** Balancing inventory across regional distribution centers and local storefronts, rather than just single-node optimization.
*   **Generative AI Chatbot (LLM Integration):** Allowing managers to ask plain-text questions (e.g., *"Why did we stock out of SKU-104 last week?"*) and receive data-backed answers from the system's historical logs.

---

## 🏗️ Technical Stack & Architecture
*   **Language:** Python 3.9+
*   **Modeling:** Scikit-Learn, SciPy (Optimization), Statsmodels, NumPy, Pandas
*   **Visualization & UI:** Streamlit, Plotly, Seaborn (Premium customized UI components)
*   **Data Integrity:** Automated Anomaly Detection and Data Guardrails
*   **Deployment:** Dockerized for cloud-agnostic scalability (AWS/Azure/GCP ready)

---


## 💼 Industry Relevance & Portfolio Value
This project implements the same rigorous mathematical logic found in Tier-1 Supply Chain platforms like **SAP IBP (Integrated Business Planning)** and **Oracle SCM**. It serves as a comprehensive demonstration of:
- **Predictive Analytics:** Handling time-series, regression, and volatility at scale.
- **Operations Research:** Mathematical optimization for high-stakes business decision support.
- **Product Engineering:** Building a user-centric, visually stunning product rather than just a dry script.

---


