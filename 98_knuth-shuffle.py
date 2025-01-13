

import random

def knuth_shuffle(arr):
    for i in range(len(arr)-1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = [6, 2, 7, 4, 5]
print("Shuffled list:", knuth_shuffle(arr))





















# Explanation: The algorithm iterates over the list in reverse and swaps each
# element with a random element before it.

# The Fisher-Yates algorithm shuffles a list randomly by swapping 
# each element with another randomly chosen element.