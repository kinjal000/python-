def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  

arr = [11, 22, 33, 44, 55]
print("Element found at index:", binary_search(arr, 33))

















# Explanation: The array is divided in half at each step until the target element
# is found or the search range is exhausted.