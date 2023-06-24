#include <iostream>
#include <vector>
#include <climits>

using namespace std;

// Função para imprimir a matriz de distâncias
void printMatrix(const vector<vector<int>>& matrix) {
    int numVertices = matrix.size();
    cout << "Matriz de distâncias:" << endl;
    for (int i = 0; i < numVertices; ++i) {
        for (int j = 0; j < numVertices; ++j) {
            if (matrix[i][j] == INT_MAX)
                cout << "INF\t";
            else
                cout << matrix[i][j] << "\t";
        }
        cout << endl;
    }
}

// Função que implementa o algoritmo Floyd-Warshall
void floydWarshall(vector<vector<int>>& graph) {
    int numVertices = graph.size();

    // Inicializa a matriz de distâncias com os pesos das arestas
    vector<vector<int>> distances(graph);

    // Atualiza as distâncias considerando todos os nós intermediários
    for (int k = 0; k < numVertices; ++k) {
        for (int i = 0; i < numVertices; ++i) {
            for (int j = 0; j < numVertices; ++j) {
                // Verifica se a rota passando por k é mais curta
                if (distances[i][k] != INT_MAX && distances[k][j] != INT_MAX &&
                    distances[i][k] + distances[k][j] < distances[i][j]) {
                    distances[i][j] = distances[i][k] + distances[k][j];
                }
            }
        }
    }

    printMatrix(distances);
}

// Exemplo de uso
int main() {
    // Cria um grafo de exemplo (matriz de adjacência)
    vector<vector<int>> graph = {
        {   0   ,   5   ,INT_MAX,   10  },
        {INT_MAX,   0   ,   3   ,INT_MAX},
        {INT_MAX,INT_MAX,   0   ,   1   },
        {INT_MAX,INT_MAX,INT_MAX,   0   }  
    };

    floydWarshall(graph);

    return 0;
}