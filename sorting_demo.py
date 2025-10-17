# A simple demo for comparing sorting algorithms
# For CS101: Introduction to Algorithms

import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    data = [random.randint(0, 1000) for _ in range(1000)]
    for sort_func in [bubble_sort, quick_sort]:
        arr_copy = data.copy()
        start = time.time()
        sort_func(arr_copy)
        print(f"{sort_func.__name__}: {time.time() - start:.4f}s")
