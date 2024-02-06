import networkx as nx


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph.nodes}
    distances[start] = 0
    unvisited = list(graph.nodes)

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor in graph.neighbors(current_vertex):
            weight = graph[current_vertex][neighbor]['weight']
            distance = distances[current_vertex] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances


if __name__ == "__main__":
    G = nx.Graph()

    edges_with_weights = [
        ("A", "B", 1), ("A", "C", 3), ("A", "D", 7),
        ("B", "E", 5), ("C", "F", 4), ("D", "G", 2),
        ("E", "F", 6), ("F", "G", 3), ("G", "H", 1),
        ("H", "I", 2), ("I", "J", 3), ("J", "E", 4),
        ("E", "H", 5)
    ]

    for edge in edges_with_weights:
        G.add_edge(edge[0], edge[1], weight=edge[2])

    paths = {vertex: dijkstra(G, vertex) for vertex in G.nodes}

    for k,v in paths.items():
        print(f"From vertex {k}:\n\tDistances : {v}\n")
