function bellmanFord(graph, startNode) {
  const distances = {};
  const previous = {};

  // Inicializa todas as distâncias como infinito, exceto o nó inicial
  for (const node in graph) {
    distances[node] = Infinity;
    previous[node] = null;
  }
  distances[startNode] = 0;

  // Relaxamento das arestas
  for (let i = 0; i < Object.keys(graph).length - 1; i++) {
    for (const [source, edges] of Object.entries(graph)) {
      for (const [destination, weight] of Object.entries(edges)) {
        if (distances[source] + weight < distances[destination]) {
          distances[destination] = distances[source] + weight;
          previous[destination] = source;
        }
      }
    }
  }

  // Verifica se há ciclos negativos
  for (const [source, edges] of Object.entries(graph)) {
    for (const [destination, weight] of Object.entries(edges)) {
      if (distances[source] + weight < distances[destination]) {
        throw new Error("O grafo contém um ciclo negativo.");
      }
    }
  }

  return { distances, previous };
}

// Exemplo de uso:

const graph = {
  A: { B: 5, C: 2 },
  B: { A: 5, C: 1, D: 3 },
  C: { A: 2, B: 1, D: 1 },
  D: { B: 3, C: 1, E: 2 },
  E: { D: 2 },
};

const startNode = "A";
const { distances, previous } = bellmanFord(graph, startNode);

console.log("Distâncias a partir do nó inicial:");
console.log(distances);

console.log("Caminhos mais curtos:");
for (const node in previous) {
  const path = [];
  let current = node;
  while (current !== null) {
    path.unshift(current);
    current = previous[current];
  }
  console.log(`${startNode} -> ${node}: [${path.join(" -> ")}]`);
}
