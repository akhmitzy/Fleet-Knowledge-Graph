import streamlit as st
import pandas as pd
from neo4j import GraphDatabase

# -------------------------
# CONFIG
# -------------------------
URI = "bolt://localhost:7687"
AUTH = ("neo4j", "password")

driver = GraphDatabase.driver(URI, auth=AUTH)

st.set_page_config(page_title="Fleet Knowledge Graph", layout="wide")

st.title("🚗 Fleet Strategy Dashboard")
st.markdown("Knowledge Graph for Fleet Allocation & Rebalancing")

# -------------------------
# QUERIES
# -------------------------
def get_shortages():
    query = """
    MATCH (d:Demand)-[:AT]->(l:Location)
    MATCH (v:Vehicle)-[:LOCATED_IN]->(l)
    WHERE v.type = d.vehicle_type
    RETURN l.name AS location,
           d.vehicle_type AS type,
           d.demand AS demand,
           count(v) AS supply,
           d.demand - count(v) AS shortage
    ORDER BY shortage DESC
    """
    with driver.session() as session:
        return pd.DataFrame(session.run(query).data())

def get_rebalancing():
    query = """
    MATCH (l1:Location)<-[:LOCATED_IN]-(v:Vehicle),
          (l2:Location)<-[:AT]-(d:Demand)
    WHERE l1 <> l2 AND v.type = d.vehicle_type
    RETURN v.id AS vehicle,
           l1.name AS from_location,
           l2.name AS to_location
    LIMIT 20
    """
    with driver.session() as session:
        return pd.DataFrame(session.run(query).data())

# -------------------------
# SIDEBAR (Simulation)
# -------------------------
st.sidebar.header("⚙️ Simulation")

price_per_rental = st.sidebar.slider(
    "Price per rental ($)", 20, 200, 50
)

# -------------------------
# MAIN DASHBOARD
# -------------------------

# Shortages
st.subheader("📊 Fleet Shortages")
shortages_df = get_shortages()

if not shortages_df.empty:
    st.dataframe(shortages_df)

    total_shortage = shortages_df["shortage"].sum()
    st.metric("Total Shortage", int(total_shortage))
else:
    st.warning("No data available")

# -------------------------
# Rebalancing
# -------------------------
st.subheader("🔄 Rebalancing Suggestions")
rebalance_df = get_rebalancing()

if not rebalance_df.empty:
    st.dataframe(rebalance_df)
else:
    st.warning("No rebalancing suggestions")

# -------------------------
# Revenue Simulation
# -------------------------
st.subheader("💰 Revenue Simulation")

if not shortages_df.empty:
    shortages_df["revenue_opportunity"] = (
        shortages_df["shortage"] * price_per_rental
    )

    st.dataframe(shortages_df)

    total_revenue = shortages_df["revenue_opportunity"].sum()

    st.metric("Potential Revenue ($)", int(total_revenue))
else:
    st.warning("No data to simulate")

# -------------------------
# Footer
# -------------------------
st.markdown("---")
st.markdown("Built with Neo4j + Streamlit")
