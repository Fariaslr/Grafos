import networkx as nx
import matplotlib.pyplot as plt
import os

def is_planar_and_draw(graph, name):
    # Criar o grafo a partir da lista de arestas fornecida
    G = nx.Graph()
    G.add_edges_from(graph)

    # Verificar se o grafo é planar
    is_planar, _ = nx.check_planarity(G)

    # Escolher o layout mais apropriado para visualização
    if is_planar:
        pos = nx.planar_layout(G)
    else:
        pos = nx.spring_layout(G, seed=42)

    # Criar diretório para salvar as imagens
    if not os.path.exists('image'):
        os.makedirs('image')

    # Plotar o grafo
    plt.figure(figsize=(10, 10))
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue',
            edge_color='gray', font_size=10, font_weight='bold')
    plt.title(f"{name} - {'Planar' if is_planar else 'Não Planar'}")

    # Salvar a figura como uma imagem PNG
    plt.savefig(f"image/{name.lower().replace(' ', '_')}.png")
    plt.close()

    return is_planar

tetrahedron_edges = [
    (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)
]

cube_edges = [
    (0, 1), (0, 2), (0, 4), (1, 3), (1, 5), (2, 3), (2, 6), (3, 7),
    (4, 5), (4, 6), (5, 7), (6, 7)
]

octahedron_edges = [
    (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4),
    (2, 3), (2, 4), (3, 4)
]

# Arestas corrigidas para o Dodecaedro e Icosaedro
dodecahedron_edges = [
    (0, 1), (0, 4), (0, 5), (1, 2), (1, 6), (2, 3), (2, 7), (3, 4), (3, 8), (4, 9),
    (5, 10), (5, 14), (6, 7), (6, 11), (7, 8), (7, 12), (8, 9), (8, 13), (9, 14),
    (10, 11), (10, 15), (11, 12), (11, 16), (12, 13), (12, 17), (13, 14), (13, 18),
    (14, 19), (15, 16), (16, 17), (17, 18), (18, 19), (19, 15)
]

icosahedron_edges = [
    (0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
    (1, 2), (1, 6), (1, 7), (2, 3), (2, 8),
    (3, 4), (3, 9), (4, 5), (4, 10), (5, 6),
    (5, 11), (6, 7), (6, 11), (7, 8), (7, 12),
    (8, 9), (8, 13), (9, 10), (9, 14), (10, 11),
    (10, 15), (11, 16), (12, 13), (12, 17), (13, 14),
    (13, 18), (14, 15), (14, 19), (15, 16), (15, 20),
    (16, 17), (16, 21), (17, 18), (17, 22), (18, 19),
    (18, 23), (19, 20), (19, 24), (20, 21), (20, 25),
    (21, 22), (21, 26), (22, 23), (22, 27), (23, 24),
    (23, 28), (24, 25), (24, 29), (25, 26), (25, 30)
]

solids = {
    "Tetraedro": tetrahedron_edges,
    "Cubo": cube_edges,
    "Octaedro": octahedron_edges,
    "Dodecaedro": dodecahedron_edges,
    "Icosaedro": icosahedron_edges
}

# Iterar sobre cada sólido e verificar se é planar
for name, edges in solids.items():
    is_planar = is_planar_and_draw(edges, name)
    print(f"{name} é {'Planar' if is_planar else 'Não Planar'}")
