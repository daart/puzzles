def partition(arr, start, end):
    insertion_index = start - 1
    pivot = arr[end]

    for current_idx in range(start, end):
        if arr[current_idx] <= pivot:
            insertion_index += 1
            arr[current_idx], arr[insertion_index] = arr[insertion_index], arr[current_idx]
    
    arr[end], arr[insertion_index + 1] = arr[insertion_index + 1], arr[end]

    return insertion_index + 1


def quick_sort(arr, start, end):

    """
    Base case is if start is greater or equal than end
    """
    if start >= end:
        return
    
    pivot_index = partition(arr, start, end)
    quick_sort(arr, start, pivot_index - 1)
    quick_sort(arr, pivot_index + 1, end)
    
    return arr


def sort_array(nums):
    quick_sort(nums, 0, len(nums) - 1)
    return nums

t1 = sort_array([5,2,3,1])
print(t1)
t2 = sort_array([5,1,1,2,0,0])
print(t2)