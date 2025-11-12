# 🧭 Graph Algorithms and Analysis

This repository explores a collection of **fundamental and advanced graph algorithms**, implemented in Python. 
Each problem demonstrates a different computational strategy involving **graph traversal, shortest paths, connectivity, and network embedding** — analyzed for both **time** and **space complexity**.

---

## 🧩 Areas Covered

| # | Algorithm / Concept | Description | Complexity |
|---|----------------------|--------------|-------------|
| 1 | **Topological Sorting (Simulation)** | Simulates vertex ordering in a DAG using in-degree updates | O(V + E) |
| 2 | **Adjacency Matrix ↔ List Conversion** | Converts dense graph matrix to adjacency list | O(V²) |
| 3 | **Expression Tree Evaluation** | Recursively computes arithmetic tree expressions | O(n) |
| 4 | **Triangle Detection** | Two methods: adjacency matrix (O(V³)) and adjacency list (O(VE)) | O(V³), O(VE) |
| 5 | **Tree Diameter (BFS x2)** | Finds longest path in a tree using double BFS | O(V + E) |
| 6 | **Max Induced Subgraph (k-core)** | Retains vertices with degree ≥ k | O(V + E) |
| 7 | **MST vs Shortest Path Proof** | Explains why MST paths may not be shortest | — |
| 8 | **Shortest Path with Constraints** | Modified Dijkstra ensuring route through z | O((V + E) log V) |
| 9 | **Max Vehicle Height Path** | Finds widest bottleneck path using max-priority Dijkstra | O((V + E) log V) |
| 10 | **Graph-to-Vector Embedding (MDS)** | Converts weighted graph into geometric embeddings | O(V³) |

---

## ⚙️ Implementation Details

Each problem includes:
- **Pure Python Implementation** (no built-in algorithm libraries)
- **Example Inputs and Outputs**
- **Complexity analysis**
- **Annotated comments for clarity**

The codes are modular, meaning each folder can be run independently.

---

## 🧠 Example Highlight — Graph Embedding (Problem 10)

This module demonstrates how to represent a graph as geometric vectors using **Multidimensional Scaling (MDS)**.  
It captures the **graph distances** and projects them into **2D Euclidean space**.

```python
embedding = graph_to_vector_embedding(G, n_dimensions=2)
print(embedding)
