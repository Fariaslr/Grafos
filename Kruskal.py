import networkx as nx
import matplotlib.pyplot as plt
import os


def draw_graph_with_kruskal_mst(graph):
    # Cria um grafo ponderado
    G = nx.Graph()

    # Adiciona as arestas e pesos ao grafo
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors:
            G.add_edge(node, neighbor, weight=weight)

    # Calcula a Árvore Geradora Mínima usando o Algoritmo de Kruska
    mst = nx.minimum_spanning_tree(G, algorithm='kruskal')

    # Define a posição dos nós
    pos = nx.spring_layout(G, seed=42)


    # Desenha o grafo original
    plt.figure(figsize=(14, 7))
    plt.subplot(121)
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightcoral',
            edge_color='gray', font_size=15, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Grafo Original - Kruskal")

    # Desenha a árvore geradora mínima
    plt.subplot(122)
    nx.draw(mst, pos, with_labels=True, node_size=500, node_color='lightyellow',
            edge_color='blue', font_size=15, font_weight='bold')
    labels = nx.get_edge_attributes(mst, 'weight')
    nx.draw_networkx_edge_labels(mst, pos, edge_labels=labels)
    plt.title("Árvore Geradora Mínima (MST) - Kruskal")

    # Salva a imagem na pasta 'image'
    plt.savefig("image/grafico kruskal mst.png")
    plt.close()


# Exemplo de grafo ponderado para Kruskal
graph_kruskal = {
    '1': [('2', 2), ('3', 3), ('4', 7)],
    '2': [('1', 2), ('3', 1), ('4', 5)],
    '3': [('1', 3), ('2', 1), ('4', 4)],
    '4': [('1', 7), ('2', 5), ('3', 4)]
}

# Executa o algoritmo de Kruskal
draw_graph_with_kruskal_mst(graph_kruskal)
