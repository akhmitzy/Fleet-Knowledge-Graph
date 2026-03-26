from neo4j import GraphDatabase
import pandas as pd

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

def create_vehicle(tx, vid, vtype, location):
    tx.run("""
        MERGE (v:Vehicle {id: $vid})
        SET v.type = $vtype
        WITH v
        MERGE (l:Location {name: $location})
        MERGE (v)-[:LOCATED_IN]->(l)
    """, vid=vid, vtype=vtype, location=location)

def load_vehicles():
    df = pd.read_csv("data/vehicles.csv")
    with driver.session() as session:
        for _, row in df.iterrows():
            session.write_transaction(create_vehicle, row['vehicle_id'], row['type'], row['location'])

if __name__ == "__main__":
    load_vehicles()
