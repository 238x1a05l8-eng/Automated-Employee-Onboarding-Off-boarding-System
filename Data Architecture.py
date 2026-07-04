import matplotlib.pyplot as plt
import networkx as nx

# Create directed graph
G = nx.DiGraph()

# Define architecture layers
nodes = {
    "Data Sources": (0, 3),
    "ERP System": (0, 2),
    "CRM System": (0, 1),
    "IoT Devices": (0, 0),

    "ETL Pipeline": (2, 1.5),

    "Data Lake": (4, 2.5),
    "Data Warehouse": (4, 0.5),

    "Analytics": (6, 2),
    "Machine Learning": (6, 1),
    "Dashboards": (6, 0),

    "Business Users": (8, 1)
}

# Add nodes
for node in nodes:
    G.add_node(node)

# Define connections
edges = [
    ("Data Sources", "ETL Pipeline"),
    ("ERP System", "ETL Pipeline"),
    ("CRM System", "ETL Pipeline"),
    ("IoT Devices", "ETL Pipeline"),

    ("ETL Pipeline", "Data Lake"),
    ("ETL Pipeline", "Data Warehouse"),

    ("Data Lake", "Machine Learning"),
    ("Data Warehouse", "Analytics"),
    ("Data Warehouse", "Dashboards"),

    ("Analytics", "Business Users"),
    ("Machine Learning", "Business Users"),
    ("Dashboards", "Business Users")
]

G.add_edges_from(edges)

# Draw
plt.figure(figsize=(14, 7))
nx.draw(
    G,
    pos=nodes,
    with_labels=True,
    node_size=3500,
    node_color="#87CEEB",
    edge_color="gray",
    arrows=True,
    arrowsize=20,
    font_size=9,
    font_weight="bold"
)

plt.title("Data Architecture", fontsize=16, fontweight="bold")
plt.axis("off")
plt.tight_layout()
plt.show()