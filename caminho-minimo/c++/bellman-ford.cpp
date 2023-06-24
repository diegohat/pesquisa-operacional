#include <iostream>
#include <vector>
#include <climits>

using namespace std;

// Estrutura para representar uma aresta
struct Edge {
    int source;
    int destination;
    int weight;

    Edge(int src, int dest, int w) : source(src), destination(dest), weight(w) {}
};

// Função que implementa o Algoritmo de Bellman-Ford
void bellmanFord(vector<Edge>& edges, int numVertices, int startNode) {
    vector<int> distances(numVertices, INT_MAX);
    distances[startNode] = 0;

    // Relaxa as arestas repetidamente num total de V-1 vezes
    for (int i = 1; i <= numVertices - 1; ++i) {
        for (const Edge& edge : edges) {
            int u = edge.source;
            int v = edge.destination;
            int weight = edge.weight;

            if (distances[u] != INT_MAX && distances[u] + weight < distances[v])
                distances[v] = distances[u] + weight;
        }
    }

    // Verifica se há ciclos de peso negativo
    for (const Edge& edge : edges) {
        int u = edge.source;
        int v = edge.destination;
        int weight = edge.weight;

        if (distances[u] != INT_MAX && distances[u] + weight < distances[v]) {
            cout << "O grafo contem ciclos de peso negativo!" << endl;
            return;
        }
    }

    // Imprime as distâncias
    cout << "Menor distancia partindo do no " << startNode << ":" << endl;
    for (int i = 0; i < numVertices; ++i) {
        cout << "Distancia ate o no " << i << ": " << distances[i] << endl;
    }
}

// Exemplo de uso
int main() {
    // Cria um grafo de exemplo
    int numVertices = 5;
    vector<Edge> edges;
    edges.emplace_back(0, 1, 5);
    edges.emplace_back(0, 2, 2);
    edges.emplace_back(1, 3, 4);
    edges.emplace_back(2, 1, 1);
    edges.emplace_back(2, 3, -7);
    edges.emplace_back(3, 4, 3);

    int startNode = 0;
    bellmanFord(edges, numVertices, startNode);

    return 0;
}