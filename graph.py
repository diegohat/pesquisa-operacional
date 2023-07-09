import sys

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 in self.graph:
            self.graph[vertex1].append((vertex2, weight))
        else:
            self.graph[vertex1] = [(vertex2, weight)]

    def get_vertices(self):
        return list(self.graph.keys())

    def get_edges(self):
        edges = []
        for vertex in self.graph:
            for neighbor, weight in self.graph[vertex]:
                edges.append((vertex, neighbor, weight))
        return edges

    def dijkstra(self, start_vertex):
        distances = {vertex: sys.maxsize for vertex in self.graph}
        distances[start_vertex] = 0

        visited = set()

        while len(visited) < len(self.graph):
            min_distance = sys.maxsize
            min_vertex = None

            for vertex in self.graph:
                if vertex not in visited and distances[vertex] < min_distance:
                    min_distance = distances[vertex]
                    min_vertex = vertex

            if min_vertex is None:
                break

            visited.add(min_vertex)

            if min_vertex not in self.graph:
                continue

            for neighbor, weight in self.graph[min_vertex]:
                distance = distances[min_vertex] + weight
                if distance < distances.get(neighbor, sys.maxsize):
                    distances[neighbor] = distance

        return distances

    def bellman_ford(self, start_vertex):
        distances = {vertex: sys.maxsize for vertex in self.graph}
        distances[start_vertex] = 0

        # Relaxation step
        for _ in range(len(self.graph) - 1):
            for vertex in self.graph:
                if vertex not in distances:
                    continue
                for neighbor, weight in self.graph[vertex]:
                    if neighbor not in distances:
                        distances[neighbor] = sys.maxsize
                    if distances[vertex] + weight < distances[neighbor]:
                        distances[neighbor] = distances[vertex] + weight

        # Negative cycle detection
        for vertex in self.graph:
            if vertex not in distances:
                continue
            for neighbor, weight in self.graph[vertex]:
                if neighbor not in distances:
                    distances[neighbor] = sys.maxsize
                if distances[vertex] + weight < distances[neighbor]:
                    print("Negative cycle detected.")
                    continue

        return distances

    def floyd_warshall(self):
        vertices = self.get_vertices()
        num_vertices = len(vertices)

        # Inicializar a matriz de distâncias com infinito para todos os pares de vértices
        distances = [[sys.maxsize] * num_vertices for _ in range(num_vertices)]
        for i in range(num_vertices):
            distances[i][i] = 0

        # Preencher as distâncias conhecidas do grafo
        for vertex in self.graph:
            vertex_index = vertices.index(vertex)
            for neighbor, weight in self.graph[vertex]:
                if neighbor in vertices:
                    neighbor_index = vertices.index(neighbor)
                    distances[vertex_index][neighbor_index] = weight

        # Algoritmo de Floyd-Warshall
        for k in range(num_vertices):
            for i in range(num_vertices):
                for j in range(num_vertices):
                    if distances[i][k] != sys.maxsize and distances[k][j] != sys.maxsize:
                        distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

        return distances

    def __str__(self):
        graph_str = ""
        for vertex in self.graph:
            graph_str += f"{vertex} -> "
            graph_str += ", ".join(f"{neighbor}:{weight}" for neighbor, weight in self.graph[vertex])
            graph_str += "\n"
        return graph_str
