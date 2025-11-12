### 🧭 Topological Sort Simulation

This example simulates the **Topological Sorting** process for a directed acyclic graph (DAG) using in-degree tracking and queue-based updates.

**Initial In-Degrees:**
A=0, B=1, C=2, D=1, E=2, F=2, G=3, H=1, I=1, J=1

**Execution Flow:**
1. Start with node A (in-degree 0).  
2. Iteratively add nodes with zero in-degree to the queue.  
3. Update the in-degree of connected nodes after each removal.  
4. Continue until all nodes are processed.

**Final Order:**  
A, B, D, E, C, H, F, J, G, I

**Result:**  
Topological Sort → **A → B → D → E → C → H → F → J → G → I**

---

📘 *This demonstrates the dependency resolution process in DAGs — fundamental to compiler design, scheduling, and task ordering.*
