### 🌳 Expression Tree Evaluation

This project demonstrates how to evaluate an **arithmetic expression tree**, where each internal node represents an operator (`+`, `-`, `*`, `/`) and each leaf node is an operand (integer).

---

### 🧩 Algorithm Overview

The algorithm recursively evaluates the left and right subtrees, applies the operator at the current node, and returns the computed result.

### 🧠 Pseudocode
```bash
FUNCTION evaluate(node):
IF node is NULL:
RETURN 0
IF node is a leaf (integer):
RETURN node.value
leftValue = evaluate(node.left)
rightValue = evaluate(node.right)
SWITCH node.value:
CASE '+': RETURN leftValue + rightValue
CASE '-': RETURN leftValue - rightValue
CASE '*': RETURN leftValue * rightValue
CASE '/': RETURN leftValue / rightValue
```

## ⚙️ Complexity Analysis

| Metric | Description | Complexity |
|---------|--------------|-------------|
| ⏱️ Time | Each node is visited once | **O(n)** |
| 💾 Space | Depends on recursion depth | **O(h)** |
| 🔹 Note | For balanced trees, h = log n; for skewed trees, h = n |

---

## 📘 Insight

Expression tree evaluation is used in compilers, calculators, and interpreters to compute arithmetic results from structured expressions.
