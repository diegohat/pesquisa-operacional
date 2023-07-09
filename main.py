from graph import Graph
import random
import time

grafos = []

def generate_random_graph(num_vertices, num_edges, allow_negative_weights=False):
    grafo = Graph()

    # Lista de vértices já visitados
    visited = set()

    # Selecionando um vértice inicial aleatório
    start_vertex = random.randint(1, num_vertices)
    visited.add(start_vertex)

    # Adicionando vértices ao grafo
    for vertex in range(1, num_vertices + 1):
        if vertex != start_vertex:
            weight = random.randint(1, 10)
            
            if allow_negative_weights:
                weight = random.randint(-10, 10)

            grafo.add_edge(start_vertex, vertex, weight)

    # Construindo a ordem topológica
    topological_order = [start_vertex]
    while len(topological_order) < num_vertices:
        vertex = random.choice(list(visited))
        neighbor = random.randint(1, num_vertices)
        if neighbor not in visited:
            weight = random.randint(1, 10)
            if allow_negative_weights:
                weight = random.randint(-10, 10)
            grafo.add_edge(vertex, neighbor, weight)
            visited.add(neighbor)
            topological_order.append(neighbor)

    # Adicionando arestas aleatórias adicionais ao grafo
    for _ in range(num_edges - num_vertices):
        vertex1 = random.choice(topological_order[:-1])
        vertex2 = random.choice(topological_order[topological_order.index(vertex1) + 1:])
        weight = random.randint(1, 10)
        
        if allow_negative_weights:
            weight = random.randint(-10, 10)

        grafo.add_edge(vertex1, vertex2, weight)

    return grafo

grafos.append(generate_random_graph(10, 20, allow_negative_weights=False))
grafos.append(generate_random_graph(5, 10, allow_negative_weights=True))
grafos.append(generate_random_graph(8, 15, allow_negative_weights=True))
grafos.append(generate_random_graph(15, 50, allow_negative_weights=False))
grafos.append(generate_random_graph(6, 8, allow_negative_weights=True))
grafos.append(generate_random_graph(12, 30, allow_negative_weights=False))
# grafos.append(generate_random_graph(7, 12, allow_negative_weights=True))
# grafos.append(generate_random_graph(20, 50, allow_negative_weights=False))
# grafos.append(generate_random_graph(4, 5, allow_negative_weights=True))
# grafos.append(generate_random_graph(9, 18, allow_negative_weights=False))
# grafos.append(generate_random_graph(7, 15, allow_negative_weights=True))
# grafos.append(generate_random_graph(10, 25, allow_negative_weights=False))
# grafos.append(generate_random_graph(6, 10, allow_negative_weights=True))
# grafos.append(generate_random_graph(15, 40, allow_negative_weights=False))
# grafos.append(generate_random_graph(8, 12, allow_negative_weights=True))
# grafos.append(generate_random_graph(12, 30, allow_negative_weights=False))
# grafos.append(generate_random_graph(5, 8, allow_negative_weights=True))
# grafos.append(generate_random_graph(20, 40, allow_negative_weights=False))
# grafos.append(generate_random_graph(4, 6, allow_negative_weights=True))
# grafos.append(generate_random_graph(9, 20, allow_negative_weights=False))


for grafo in grafos:
    print(f"\n\n %%%%%%%%%%%%%%%%%%%%%%%%%% GRAFO {grafos.index(grafo) + 1} %%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    # Obtendo vértices e arestas do grafo
    vertices = grafo.get_vertices()
    arestas = grafo.get_edges()

    print("Vértices:", vertices)
    print("Arestas:", arestas)

    # Imprimindo o grafo
    print("\nRepresentação do grafo:")
    print(grafo)

    print("\n--------------DIJKSTRA--------------")
    # Executando o algoritmo de Dijkstra
    vertice_aleatorio = random.choice(vertices)
    start_time = time.time()
    distancias = grafo.dijkstra(vertice_aleatorio)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000 
    print(f"TEMPO DE EXECUÇÃO: {execution_time:.4f} milissegundos")
    # Imprimindo as distâncias mínimas a partir do vértice aleatório
    for vertex, distance in distancias.items():
        print(f"Distância mínima de {vertice_aleatorio} até {vertex}: {distance}")

    print("\n-----------FLOYD-WARSHALL-----------")
    # Executando o algoritmo de Floyd-Warshall
    start_time = time.time()
    distancias = grafo.floyd_warshall()
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000 
    print(f"TEMPO DE EXECUÇÃO: {execution_time:.4f} milissegundos")
    # Imprimindo as distâncias mínimas entre todos os pares de vértices
    for i in range(len(distancias)):
        for j in range(len(distancias[i])):
            print(f"Distância mínima entre {i} e {j}: {distancias[i][j]}")

    print("\n------------BELLMAN-FORD------------")
    # Executando o algoritmo de Bellman-Ford
    start_time = time.time()
    distancias = grafo.bellman_ford(vertice_aleatorio)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000 
    print(f"TEMPO DE EXECUÇÃO: {execution_time:.4f} milissegundos")
    # Imprimindo as distâncias mínimas a partir do vértice 1
    for vertex, distance in distancias.items():
        print(f"Distância mínima de {vertice_aleatorio} até {vertex}: {distance}")