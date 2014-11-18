from py2neo import neo4j, node

def initialise():
    global graph_db
    graph_db = None

def connect_to_database():
    if graph_db is None:
        graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")

def add_node(node_data):
    if graph_db is None:
        print("No database connection!")
    else:
        graph_db.create(node(node_data))
        print("Node added!")
