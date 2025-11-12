### 🔄 Adjacency Matrix to Adjacency List Conversion

This project demonstrates how to convert a **graph represented as an adjacency matrix** into an **adjacency list** using Python.  
It highlights how storage and traversal efficiency improve when switching from dense to sparse graph representations.

---

### 🧩 Algorithm Overview

Each vertex `i` is iterated through its row in the adjacency matrix.  
If an edge exists (`matrix[i][j] == 1`), vertex `j` is appended to `i`’s adjacency list.

**Pseudocode:**
```bash
for each vertex i:
adjacency_list[i] = []
for each vertex j:
if matrix[i][j] == 1:
adjacency_list[i].append(j)
```

### Results
<img width="1742" height="2071" alt="adjacency_matrix_to_list" src="https://github.com/user-attachments/assets/04b51f6e-7b78-4292-bd27-ccb52c30d48d" />

Output: {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}

### ⚙️ Complexity Analysis
| Type      | Description                       | Complexity   |
| --------- | --------------------------------- | ------------ |
| **Time**  | Iterates through all matrix cells | **O(n²)**    |
| **Space** | Stores only existing edges        | **O(n + m)** |

Let n represent the number of vertices (nodes) in the graph and m represent the number of edges.

⏱️ Time Complexity

The algorithm iterates over every cell in the adjacency matrix.

The matrix contains n × n entries, and each cell is checked once.

For each cell, it performs a constant-time operation to verify if an edge exists and add it to the adjacency list if needed.

✅ Overall Time Complexity: O(n²)

💾 Space Complexity

The adjacency list requires storage proportional to the number of vertices and edges.

Each vertex stores a list of its adjacent vertices, leading to a space requirement of O(n + m).

The adjacency matrix itself consumes O(n²) space.

If the adjacency matrix is discarded after conversion, total space reduces to O(n + m).
