

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap
    return arr

arr = [64, 25, 12, 22, 11]
print("Sorted array:", bubble_sort(arr))






















# Explanation: The outer loop ensures that all elements are checked.
# The inner loop compares adjacent elements and swaps them if necess

# Bubble sort repeatedly compares adjacent elements and swaps them if 
# they are in the wrong order.