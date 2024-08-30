import networkx as nx
import matplotlib.pyplot as plt
import os


def draw_graph_with_prim_mst(graph):

    G = nx.Graph()

    for node, neighbors in graph.items():
        for neighbor, weight in neighbors:
            G.add_edge(node, neighbor, weight=weight)

    mst = nx.minimum_spanning_tree(G, algorithm='prim')

    pos = nx.spring_layout(G, seed=42)

    if not os.path.exists('image'):
        os.makedirs('image')

    plt.figure(figsize=(14, 7))
    plt.subplot(121)
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightgreen',
            edge_color='gray', font_size=15, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Grafo Original - Prim")

    plt.subplot(122)
    nx.draw(mst, pos, with_labels=True, node_size=500, node_color='lightblue',
            edge_color='red', font_size=15, font_weight='bold')
    labels = nx.get_edge_attributes(mst, 'weight')
    nx.draw_networkx_edge_labels(mst, pos, edge_labels=labels)
    plt.title("Árvore Geradora Mínima (MST) - Prim")

    plt.savefig("image/grafico prim mst.png")
    plt.close()


graph_prim = {
    'A': [('B', 7), ('C', 9), ('D', 14)],
    'B': [('A', 7), ('C', 10), ('E', 15)],
    'C': [('A', 9), ('B', 10), ('D', 2), ('F', 11)],
    'D': [('A', 14), ('C', 2), ('F', 9)],
    'E': [('B', 15), ('F', 6)],
    'F': [('C', 11), ('D', 9), ('E', 6)]
}

draw_graph_with_prim_mst(graph_prim)
