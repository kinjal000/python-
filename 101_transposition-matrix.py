def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

matrix = [[1, 2], [3, 4]]
print("Transpose:", transpose_matrix(matrix))




























# Explanation: Rows become columns and columns become rows in the matrix.