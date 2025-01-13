def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arr = [64, 25, 12, 22, 11]
print("Sorted array:", quick_sort(arr))





















# Explanation: The array is split into three parts: elements smaller than the pivot,
# elements equal to the pivot, and elements larger than the pivot.
# This is recursively applied to each part.