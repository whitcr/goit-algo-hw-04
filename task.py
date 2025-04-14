import random
import timeit

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def timsort(arr):
    return sorted(arr)

sizes = [1000, 2000, 5000]
results = []

for size in sizes:
    data = [random.randint(0, 10000) for _ in range(size)]
    
    insertion_time = timeit.timeit(lambda: insertion_sort(data.copy()), number=1)
    merge_time = timeit.timeit(lambda: merge_sort(data.copy()), number=1)
    timsort_time = timeit.timeit(lambda: timsort(data.copy()), number=1)

    results.append((size, insertion_time, merge_time, timsort_time))

print("Розмір | Вставки (с) | Злиття (с) | Timsort (с)")
for r in results:
    print(f"{r[0]:6} | {r[1]:11.6f} | {r[2]:11.6f} | {r[3]:11.6f}")
