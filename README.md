# Shortest Path Algorithms in Weighted Graphs Analysis

## Introduction

Shortest path algorithms are fundamental tools in solving problems that involve finding the shortest path between two points in a weighted graph. These algorithms find applications in various domains such as computer networks, routing systems, logistics, and more. In this report, we will present three classical algorithms for solving the shortest path problem: Dijkstra, Bellman-Ford, and Floyd-Warshall.

## Theoretical Foundation

### Graphs

A graph is a structure composed of a set of vertices (or nodes) and a set of edges that connect these vertices. Vertices represent entities, and edges represent the relationships between these entities. In a weighted graph, each edge has an associated weight or cost, which can represent distances, times, costs, and more.

### Paths in Graphs

A path in a graph is a sequence of vertices connected by edges. The distance or cost of a path is determined by the sum of the weights of the edges along the path. The goal of shortest path algorithms is to find the path with the minimum cost between two specific vertices in a weighted graph.

### Dijkstra's Algorithm

Dijkstra's algorithm is used to find the shortest path between a source vertex and all other vertices in a weighted graph with non-negative weights. The algorithm employs a greedy approach, incrementally expanding the set of visited vertices starting from the source vertex. It maintains a list of minimum distances from the source vertex to each vertex in the graph.

### Bellman-Ford Algorithm

The Bellman-Ford algorithm is used to find the shortest path between a source vertex and all other vertices in a weighted graph, even when negative weights are present. The algorithm uses an iterative edge relaxation approach. The relaxation process involves comparing the current distances of vertices with distances through edges and updating them if necessary. The algorithm performs a total of V - 1 iterations, where V is the number of vertices in the graph.

### Floyd-Warshall Algorithm

The Floyd-Warshall algorithm is used to find the minimum distances between all pairs of vertices in a weighted graph. Unlike the previous algorithms, which find the shortest paths from a single source vertex, the Floyd-Warshall algorithm calculates the minimum distances between all possible combinations of vertices. It utilizes a dynamic programming approach to compute the minimum distances. It maintains a matrix of minimum distances, initially filled with the weights of known edges. The algorithm performs an iterative relaxation process on all vertex combinations, updating the minimum distances whenever a shorter path is found.

## Algorithm Specifications

### 1. Dijkstra's Algorithm
   - Finds the shortest path between a source vertex and all other vertices in a weighted graph with non-negative weights.
   - Maintains a list of minimum distances from the source vertex to each vertex in the graph.
   - Selects, in each iteration, the unvisited vertex with the smallest distance and updates the distances of its neighbors.

### 2. Bellman-Ford Algorithm
   - Finds the shortest path between a source vertex and all other vertices in a weighted graph, even with negative weights.
   - Iteratively performs edge relaxation, updating minimum distances for each vertex.
   - Executes a total of V - 1 iterations, where V is the number of vertices in the graph.

### 3. Floyd-Warshall Algorithm
   - Finds the minimum distances between all pairs of vertices in a weighted graph.
   - Utilizes a dynamic programming approach to calculate minimum distances.
   - Maintains a matrix of minimum distances, initially filled with the weights of known edges.
   - Performs an iterative relaxation process on all combinations of vertices, updating minimum distances whenever a shorter path is found.

## Experiment Descriptions

In this work, we implemented the Dijkstra, Bellman-Ford, and Floyd-Warshall algorithms in the Python programming language and conducted experiments on different randomly generated graphs. The provided code allows for the creation of random graphs with a specified number of vertices and edges, with an option to enable or disable negative edge weights.

Each experiment consisted of the following steps:

1. Obtaining the vertices and edges of the graph.
2. Printing the representation of the graph.
3. Executing the Dijkstra algorithm from a random vertex, with measurement of the execution time.
4. Printing the minimum distances from the random vertex.
5. Executing the Floyd-Warshall algorithm, with measurement of the execution time.
6. Printing the minimum distances between all pairs of vertices.
7. Executing the Bellman-Ford algorithm from the same random vertex used in Dijkstra, with measurement of the execution time.
8. Printing the minimum distances from the random vertex.

## Discussion and Results

The results of the experiments demonstrated the efficiency and correctness of the implemented shortest path algorithms. We observed distinct characteristics of each algorithm:

- Dijkstra's algorithm is efficient for graphs with non-negative weights, but its performance can degrade in graphs with many edges.

- The Bellman-Ford algorithm is robust in handling graphs with negative weights, but it has a higher time complexity compared to Dijkstra's algorithm.

- The Floyd-Warshall algorithm is suitable for finding the minimum distances between all pairs of vertices, regardless of edge weights. However, its time complexity is higher than that of the other algorithms.

In summary, the results highlighted the importance and utility of shortest path algorithms in solving practical problems involving weighted graphs.

## Conclusion

In this work, we explored shortest path algorithms, including Dijkstra, Bellman-Ford, and Floyd-Warshall. We gained an understanding of their theoretical foundations, specifications, and implementations, and conducted experiments on randomly generated graphs.

The results of the experiments emphasized the efficiency and suitability of each algorithm for different types of problems. Each algorithm has specific advantages and limitations, making them suitable for different contexts and applications.

Shortest path algorithms play a crucial role in various domains, such as computer networks, routing systems, logistics, and many more. Understanding these algorithms and knowing when to apply them is essential for solving complex problems involving weighted graphs.
