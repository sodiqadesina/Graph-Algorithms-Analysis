### 🔺 Triangle Detection in Graphs

This module identifies whether a given undirected graph contains a **triangle** (a cycle of three vertices).

Two approaches are implemented:

---

### Adjacency Matrix Method**

### 🧩 Algorithm
- Check all triplets of vertices (u, v, w).  
- Verify if all three edges `(u,v)`, `(v,w)`, and `(w,u)` exist.  
- Return the triangle once found.

**Time Complexity:** O(|V|³)  
**Space Complexity:** O(1)

---

### Adjacency List Method**

### 🧩 Algorithm
- For each pair of vertices `(u, v)`, compute their **common neighbors**.  
- If a common neighbor exists, a triangle is found.  

**Time Complexity:** O(|V||E|)  
**Space Complexity:** O(|V| + |E|)

---

## 📘 Insight

Triangle detection is fundamental in **network analysis** (e.g., social clustering) and graph-pattern mining.
