import networkx as nx
import matplotlib.pyplot as plt
import os


def draw_graph(graph, colors):
    G = nx.Graph()

    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G, seed=42)

    if not os.path.exists('image'):
        os.makedirs('image')

    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_size=500,
            node_color=colors, edge_color='gray', font_size=15, font_weight='bold')

    plt.title("Grafo Colorido")
    plt.savefig("image/Grafo_colorido.png")
    plt.show()


def greedy_coloring(graph):
    result = {}
    for node in graph:
        result[node] = -1  

    result[list(graph.keys())[0]] = 0

    available = [True] * len(graph)

    for u in graph:
        for neighbor in graph[u]:
            if result[neighbor] != -1:
                available[result[neighbor]] = False

        for color in range(len(graph)):
            if available[color]:
                result[u] = color
                break

        available = [True] * len(graph)

    color_map = [result[node] for node in graph]
    
    return color_map


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

colors = greedy_coloring(graph)

draw_graph(graph, colors)
