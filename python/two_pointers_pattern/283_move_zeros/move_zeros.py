def moveZeros(nums):
    non_zero_insertion_position = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_insertion_position] = nums[i]
            non_zero_insertion_position += 1
    
    for j in range(non_zero_insertion_position, len(nums)):
        nums[j] = 0

    return nums