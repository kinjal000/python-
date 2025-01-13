def matrix_multiplication(A, B):
    result = [[0 for i in range(len(B[0]))] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print("Matrix Product:", matrix_multiplication(A, B))
























# Explanation: The element at position (i, j) is calculated as the dot product
# of row i from matrix A and column j from matrix B.