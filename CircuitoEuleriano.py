import networkx as nx
import matplotlib.pyplot as plt
import os


def draw_graph(graph):
    G = nx.Graph()

    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G, seed=42)

    if not os.path.exists('image'):
        os.makedirs('image')

    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue',
            edge_color='gray', font_size=15, font_weight='bold')

    plt.title("Grafo Euleriano")
    plt.savefig("image/euleriano.png")
    plt.show()


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

draw_graph(graph)
