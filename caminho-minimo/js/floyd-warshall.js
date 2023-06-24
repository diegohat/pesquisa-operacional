function floydWarshall(graph) {
  const numNodes = Object.keys(graph).length;
  const distances = {};
  const next = {};

  // Inicializa as matrizes de distâncias e próximo
  for (const source in graph) {
    distances[source] = {};
    next[source] = {};
    for (const destination in graph) {
      if (source === destination) {
        distances[source][destination] = 0;
      } else if (graph[source][destination] !== undefined) {
        distances[source][destination] = graph[source][destination];
      } else {
        distances[source][destination] = Infinity;
      }
      next[source][destination] = destination;
    }
  }

  // Algoritmo de Floyd-Warshall
  for (const k in graph) {
    for (const i in graph) {
      for (const j in graph) {
        const newDistance = distances[i][k] + distances[k][j];
        if (newDistance < distances[i][j]) {
          distances[i][j] = newDistance;
          next[i][j] = next[i][k];
        }
      }
    }
  }

  return { distances, next };
}

// Exemplo de uso:

const graph = {
  A: { B: 5, C: 2 },
  B: { A: 5, C: 1, D: 3 },
  C: { A: 2, B: 1, D: 1 },
  D: { B: 3, C: 1, E: 2 },
  E: { D: 2 },
};

const { distances, next } = floydWarshall(graph);

console.log("Distâncias entre todos os pares de nós:");
console.log(distances);

console.log("Próximo nó no caminho mais curto:");
console.log(next);
