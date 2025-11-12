### 🌲 Tree Diameter Calculation

This program computes the **diameter of a tree**, i.e., the longest path between any two nodes.

---

### 🧩 Algorithm Overview

1. Perform BFS from an arbitrary node to find the farthest vertex `A`.  
2. Perform BFS again from `A` to find the farthest vertex `B`.  
3. The distance between `A` and `B` is the diameter.

---

### ⚙️ Complexity Analysis

| Metric | Description | Complexity |
|---------|--------------|-------------|
| ⏱️ Time | Two BFS traversals | **O(V + E)** |
| 💾 Space | Queue + distance array | **O(V)** |

---

## 📘 Insight

This double-BFS method efficiently determines the longest path in trees, commonly used in **network topology** and **hierarchical data analysis**.
