def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  

arr = [64, 25, 12, 22, 11]
print("Element found at index:", linear_search(arr, 22))





















# Explanation: Each element is checked one by one until a match is found.