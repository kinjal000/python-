def transpose_matrix(matrix):

    return [list(row) for row in zip(*matrix)]

def is_symmetric(matrix):
    return matrix == transpose_matrix(matrix)

matrix = [[1, 2], [2, 1]]
print("Is symmetric:", is_symmetric(matrix))
























# Explanation: The matrix is symmetric if it equals its transpose.