from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
AUTH = ("neo4j", "password")

driver = GraphDatabase.driver(URI, auth=AUTH)

def shortage_query(tx):
    result = tx.run("""
        MATCH (d:Demand)-[:AT]->(l:Location)
        MATCH (v:Vehicle)-[:LOCATED_IN]->(l)
        WHERE v.type = d.vehicle_type
        RETURN l.name AS location,
               d.vehicle_type AS type,
               d.demand AS demand,
               count(v) AS supply,
               d.demand - count(v) AS shortage
        ORDER BY shortage DESC
    """)
    return result.data()

def rebalance_query(tx):
    result = tx.run("""
        MATCH (l1:Location)<-[:LOCATED_IN]-(v:Vehicle),
              (l2:Location)<-[:AT]-(d:Demand)
        WHERE l1 <> l2 AND v.type = d.vehicle_type
        RETURN v.id AS vehicle,
               l1.name AS from_location,
               l2.name AS to_location
        LIMIT 10
    """)
    return result.data()

def run_queries():
    with driver.session() as session:
        print("\n--- Shortages ---")
        for row in session.execute_read(shortage_query):
            print(row)

        print("\n--- Rebalancing Suggestions ---")
        for row in session.execute_read(rebalance_query):
            print(row)

if __name__ == "__main__":
    run_queries()
