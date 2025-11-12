# 🔄 Adjacency Matrix to Adjacency List Conversion

This project demonstrates how to convert a **graph represented as an adjacency matrix** into an **adjacency list** using Python.  
It highlights how storage and traversal efficiency improve when switching from dense to sparse graph representations.

---

## 🧩 Algorithm Overview

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
