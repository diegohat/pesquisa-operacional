#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

// Estrutura para representar uma aresta
struct Edge {
    int destination;
    int weight;

    Edge(int dest, int w) : destination(dest), weight(w) {}
};

// Classe para representar um grafo
class Graph {
    int numVertices;
    vector<vector<Edge>> adjacencyList;

public:
    Graph(int vertices) : numVertices(vertices) {
        adjacencyList.resize(numVertices);
    }

    // Função para adicionar uma aresta direcionada ao grafo
    void addEdge(int source, int destination, int weight) {
        adjacencyList[source].emplace_back(destination, weight);
    }

    // Função que implementa o Algoritmo de Dijkstra
    vector<int> dijkstra(int startNode) {
        // Vetor de distâncias inicializado com infinito
        vector<int> distances(numVertices, INT_MAX);
        distances[startNode] = 0;

        // Fila de prioridade para selecionar o nó de menor distância
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        pq.push(make_pair(0, startNode));

        while (!pq.empty()) {
            int currentNode = pq.top().second;
            int currentDistance = pq.top().first;
            pq.pop();

            // Ignora nós que já foram processados com distâncias menores
            if (currentDistance > distances[currentNode])
                continue;

            // Percorre os vizinhos do nó atual
            for (const Edge& edge : adjacencyList[currentNode]) {
                int neighbor = edge.destination;
                int weight = edge.weight;
                int distance = currentDistance + weight;

                // Atualiza a distância se encontrarmos um caminho mais curto
                if (distance < distances[neighbor]) {
                    distances[neighbor] = distance;
                    pq.push(make_pair(distance, neighbor));
                }
            }
        }

        return distances;
    }
};

// Exemplo de uso
int main() {
    // Cria um grafo de exemplo
    int numVertices = 5;
    Graph graph(numVertices);

    graph.addEdge(0, 1, 5);
    graph.addEdge(0, 2, 2);
    graph.addEdge(1, 3, 4);
    graph.addEdge(2, 1, 1);
    graph.addEdge(2, 3, 7);
    graph.addEdge(3, 4, 3);

    int startNode = 0;
    vector<int> distances = graph.dijkstra(startNode);

    cout << "Menor distancia partindo do no " << startNode << ":" << endl;
    for (int i = 0; i < numVertices; ++i) {
        cout << "Distancia ate o no " << i << ": " << distances[i] << endl;
    }

    return 0;
}