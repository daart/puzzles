
def remove_element(nums, k):
    insertion_index = 0
    for i in range(len(nums)):
        if nums[i] != k:
            nums[insertion_index] = nums[i]
            insertion_index
    
    return insertion_index + 1