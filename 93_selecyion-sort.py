def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [64, 25, 12, 22, 11]

print("Sorted array:", selection_sort(arr))






















# Explanation: The algorithm selects the minimum element and swaps 
# it with the first unsorted element.