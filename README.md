# Fleet-Knowledge-Graph
Fleet Knowledge Graph for Demand-Aware Vehicle Allocation

# Fleet Knowledge Graph for Demand-Aware Vehicle Allocation

## 🚗 Overview
This project demonstrates how a **Knowledge Graph (Neo4j)** can be used to improve **fleet strategy and planning decisions**.

It models relationships between:
- Vehicles
- Locations
- Demand
- Reservations

and answers key business questions such as:
- Where do we have vehicle shortages?
- How should we rebalance the fleet?
- What is the revenue impact?

---

## 🎯 Business Problem
Fleet operators often face:
- Underutilized vehicles in low-demand areas
- Shortages in high-demand locations
- Inefficient rebalancing decisions

---

## 💡 Solution
We build a **graph-based model** where:
- Vehicles are connected to locations
- Demand is linked to locations and time
- Queries identify shortages and rebalancing opportunities

---

## 🧠 Graph Model
```cypher
(Vehicle)-[:LOCATED_IN]->(Location)
(Demand)-[:AT]->(Location)
(Vehicle)-[:MATCHES]->(Demand)
```
## 📂 Project Structure

```markdown
fleet-knowledge-graph/
│
├── data/
├── src/
├── notebooks/
├── requirements.txt
└── README.md
```

## ⚙️ Setup 

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

## ⚙️ Run Neo4j (locally)

-Download: https://neo4j.com/download/
-Default:
-URI: bolt://localhost:7687
-user: neo4j
-password: password

## ▶️ Run Project

python src/build_graph.py
python src/queries.py

## 🔍 Example Insights
-Shortage Detection
-Identifies locations where demand exceeds supply.
-Fleet Rebalancing
-Suggests moving vehicles from low-demand to high-demand areas.

## 📈 Example Output

Location: Miami | Demand: 45 | Supply: 10 | Shortage: 35

## 🚀 Future Improvements

-Integrate real-time data (e.g., telematics platforms like Samsara)
-Add pricing optimization
-Build dashboard (Streamlit)

## 💼 Resume Bullet

Built a Neo4j-based knowledge graph to model fleet vehicles, locations, and demand, enabling demand-aware allocation and rebalancing decisions.

---

# 📦 requirements.txt
-neo4j
-pandas

