import networkx as nx
import matplotlib.pyplot as plt
import os


def is_planar_and_draw(graph, name):

    G = nx.Graph()
    G.add_edges_from(graph)

    is_planar, _ = nx.check_planarity(G)

    pos = nx.spring_layout(G, seed=42)

    if not os.path.exists('image'):
        os.makedirs('image')

    plt.figure(figsize=(8, 8))
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue',
            edge_color='gray', font_size=15, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title(f"{name} - {'Planar' if is_planar else 'Não Planar'}")

    plt.savefig(f"image/{name.lower().replace(' ', '_')}_planar.png")
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

dodecahedron_edges = [
    (0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
    (1, 2), (1, 6), (2, 7), (3, 8), (4, 9),
    (5, 10), (6, 7), (6, 11), (7, 12), (8, 13),
    (9, 14), (10, 15), (11, 12), (11, 16), (12, 17),
    (13, 18), (14, 19), (15, 16), (16, 17), (17, 18),
    (18, 19), (19, 14)
]

icosahedron_edges = [
    (0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
    (1, 2), (1, 6), (2, 7), (3, 8), (4, 9),
    (5, 10), (6, 7), (6, 11), (7, 12), (8, 13),
    (9, 14), (10, 15), (11, 12), (11, 16), (12, 17),
    (13, 18), (14, 19), (15, 16), (16, 17), (17, 18),
    (18, 19), (19, 14)
]

solids = {
    "Tetraedro": tetrahedron_edges,
    "Cubo": cube_edges,
    "Octaedro": octahedron_edges,
    "Dodecaedro": dodecahedron_edges,
    "Icosaedro": icosahedron_edges
}

for name, edges in solids.items():
    is_planar = is_planar_and_draw(edges, name)
    print(f"{name} é {'Planar' if is_planar else 'Não Planar'}")
