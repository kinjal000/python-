def matrix_addition(A, B):
    result = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    return result

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print("Matrix Sum:", matrix_addition(A, B))





















# Explanation: Each element of one matrix is added to the corresponding
# element of the other matrix.