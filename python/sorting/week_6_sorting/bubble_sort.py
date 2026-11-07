def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(1, n):
            if arr[j] < arr[j - 1]:
                arr[j- 1], arr[j] = arr[j], arr[j - 1]

    return arr


arr1 = [20, 2, 7, 12, 15, 1, 6, 8]

print(bubble_sort(arr1))