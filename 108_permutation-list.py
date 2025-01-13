import itertools

def generate_permutations(arr):
    return list(itertools.permutations(arr))

arr = [1, 2, 3,4]
print("Permutations:", generate_permutations(arr))


























# Explanation: itertools.permutations generates all possible permutations
# of the input list.