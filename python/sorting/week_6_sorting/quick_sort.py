arr1 = [20, 2, 7, 12, 15, 1, 6, 8]


def quick_sort(arr):

    if len(arr) <= 1:
        return arr
    
    pivot_point = arr.pop()

    items_lower = []
    items_greater = []

    for item in arr:
        if item > pivot_point:
            items_greater.append(item)
        else:
            items_lower.append(item)

        
    return quick_sort(items_lower) + [pivot_point] + quick_sort(items_greater)



print(quick_sort(arr1))