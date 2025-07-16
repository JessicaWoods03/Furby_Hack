import chromadb
from flask import Flask, request, jsonify
import pandas as pd
import json
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Initialize ChromaDB client
client = chromadb.Client()
xml_file_path = r'/Volumes/NO NAME/xml_chunks/Aalborg_ChromaDB_Entry.xml'

df = pd.read_xml(xml_file_path)
# Create a collection (or retrieve if already exists)
collection = client.create_collection(name="node_graphs_collection")

# Sample DataFrame (you already have this `df_grouped_nodes` with 'node_graph' column)
# need to debug this....Going to notebooks to debug and check structure of it in the database-


df_grouped_nodes = pd.DataFrame(data)

# Helper function to insert node graphs into ChromaDB
def insert_node_graphs_into_chromadb(df):
    for index, row in df.iterrows():
        node_graph_data = {
            "content": row['node_graph']['content'],
            "parent_child_structure": json.dumps(row['node_graph']['parent_child_structure']),
            "meta_namespace": 'Geographical Entities',
            "timestamp": datetime.utcnow().isoformat(),
            "meta_topic": 'Municipalities in Denmark, Geographical Locations, Cities in North Jutland',
            "semantic_tags": 'Aalborg Municipality, City, Administrative Division, Political Entity, Region'
        }

        # Insert into ChromaDB
        collection.add(
            documents=[node_graph_data["content"]],
            metadatas=[{
                "parent_child_structure": node_graph_data["parent_child_structure"],
                "meta_namespace": node_graph_data["meta_namespace"],
                "timestamp": node_graph_data["timestamp"],
                "meta_topic": node_graph_data["meta_topic"],
                "semantic_tags": node_graph_data["semantic_tags"]
            }],
            ids=[str(index)]
        )

@app.route('/insert_node_graphs', methods=['POST'])
def insert_node_graphs():
    # Insert the node_graph data into ChromaDB
    insert_node_graphs_into_chromadb(df_grouped_nodes)
    return jsonify({"message": "Node graphs inserted successfully!"}), 200

# Helper function to retrieve node graph by ID
@app.route('/retrieve_node_graph/<string:node_id>', methods=['GET'])
def retrieve_node_graph(node_id):
    # Query ChromaDB for the node graph using the ID
    result = collection.query(query_texts=[node_id], n_results=1)
    
    if result['documents']:
        retrieved_data = result['documents'][0]
        # Parse the parent-child structure
        parent_child_structure = json.loads(result['metadatas'][0]["parent_child_structure"])
        return jsonify({
            "content": retrieved_data,
            "parent_child_structure": parent_child_structure
        }), 200
    else:
        return jsonify({"message": "Node graph not found!"}), 404

# Route for querying node graphs based on semantic tags (example)
@app.route('/query_node_graphs', methods=['GET'])
def query_node_graphs():
    tags = request.args.get('tags', '').split(',')

    # Search for documents with the provided tags
    result = collection.query(query_texts=tags, n_results=5)

    if result['documents']:
        return jsonify({
            "documents": result['documents'],
            "metadatas": result['metadatas']
        }), 200
    else:
        return jsonify({"message": "No matching node graphs found!"}), 404

if __name__ == '__main__':
    app.run(debug=True)
