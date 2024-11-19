import networkx as nx
import random
import matplotlib.pyplot as plt

def criar_grafo(numero_cidades):
    directed_graph = nx.DiGraph()

    for i in range(1, numero_cidades + 1):
        directed_graph.add_node(f"Cidade {i}")

    for cidade1 in directed_graph.nodes():
        for cidade2 in directed_graph.nodes():
            if cidade1 != cidade2:
                peso = random.randint(1, 100)
                directed_graph.add_edge(cidade1, cidade2, weight=peso)

    return directed_graph

def mostrar_grafo(grafo):
    pos = nx.spring_layout(grafo)  # Layout do grafo
    labels = nx.get_edge_attributes(grafo, 'weight')
    nx.draw(grafo, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', edge_color='gray')
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels)
    print("Caminho menos custoso: ", caminho_menos_custoso(grafo))
    plt.show()

def caminho_menos_custoso(grafo):
    return min(nx.all_pairs_dijkstra_path_length(grafo), key=lambda x: min(x[1].values()))


numero_cidades = 5
grafo = criar_grafo(numero_cidades)

mostrar_grafo(grafo)


