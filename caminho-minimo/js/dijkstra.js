class PriorityQueue {
  constructor() {
    this.elements = [];
  }

  enqueue(element, priority) {
    this.elements.push({ element, priority });
    this.elements.sort((a, b) => a.priority - b.priority);
  }

  dequeue() {
    return this.elements.shift().element;
  }

  isEmpty() {
    return this.elements.length === 0;
  }
}

function dijkstra(graph, startNode) {
  const distances = {};
  const previous = {};
  const queue = new PriorityQueue();

  for (const node in graph) {
    distances[node] = Infinity;
    previous[node] = null;
  }

  distances[startNode] = 0;
  queue.enqueue(startNode, 0);

  while (!queue.isEmpty()) {
    const currentNode = queue.dequeue();

    for (const neighbor in graph[currentNode]) {
      const distance = distances[currentNode] + graph[currentNode][neighbor];

      if (distance < distances[neighbor]) {
        distances[neighbor] = distance;
        previous[neighbor] = currentNode;
        queue.enqueue(neighbor, distance);
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
const { distances, previous } = dijkstra(graph, startNode);

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
