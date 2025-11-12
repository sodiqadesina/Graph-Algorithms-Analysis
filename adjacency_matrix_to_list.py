def adjacency_matrix_to_list(matrix):
    adjacency_list = {}
    for i in range(len(matrix)):
        adjacency_list[i] = []
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:  # Check if there's an edge
                adjacency_list[i].append(j)
    return adjacency_list

# Example usage
adj_matrix = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]

adj_list = adjacency_matrix_to_list(adj_matrix)
print(adj_list)
