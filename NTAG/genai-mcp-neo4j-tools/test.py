from langchain_neo4j import Neo4jGraph

graph = Neo4jGraph(
    url="neo4j+s://30270645.databases.neo4j.io:7687",
    username="neo4j",
    password="id1A0EHdl4niELe0MbBifZuSG1VinEQHYH04lj_qC98",
    database="neo4j"
)

try:
    result = graph.query("""
        MATCH (p:Person {name: "Tom Hanks"})-[:ACTED_IN]->(m:Movie)
        WHERE m.year > 1993
        RETURN m.title AS title, m.year AS year
        ORDER BY m.year DESC
        LIMIT 5
    """)
    print("✅ Connection successful!")
    for row in result:
        print(f"{row['title']} ({row['year']})")
except Exception as e:
    print("❌ Connection failed:")
    print(e)
