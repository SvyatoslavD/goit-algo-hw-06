import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

edges = [
    ("A", "B"), ("A", "C"), ("A", "D"),
    ("B", "E"), ("C", "F"), ("D", "G"),
    ("E", "F"), ("F", "G"), ("G", "H"),
    ("H", "I"), ("I", "J"), ("J", "E"),
    ("E", "H")
]

G.add_edges_from(edges)

if __name__ == "__main__":
    print(f'{"кількість вершин":20}:', G.number_of_nodes())
    print(f'{"кількість ребер":20}:', G.number_of_edges())
    print(f'{"ступінь вершин":20}:', G.degree())

    plt.figure(figsize=(10, 8)).suptitle("Транспортна мережа СМТ Інгулець :)")
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=700, font_size=15)
    plt.show()
