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
## 2️⃣ Optional: Add syntax highlighting

For trees, there isn’t a real programming language, but some people use `text` or `bash` for slight formatting:

```markdown
```text
fleet-knowledge-graph/
│
├── data/
├── src/
├── notebooks/
├── requirements.txt
└── README.md
```

