def shuffle(nums, n):
    for i in range(n):
        nums[i] = (nums[i] << 10) | nums[i + n]
    
    # Extract and place values in their final positions
    for i in range(n - 1, -1, -1):  # Process backward to avoid overwriting
        y = nums[i] & (2 ** 10 - 1)  # Extract lower 10 bits (y value) using mask 1023
        x = nums[i] >> 10    # Extract upper bits (x value)
        nums[2*i + 1] = y
        nums[2*i] = x
        
    return nums

t1 = [2, 5, 1, 3, 4, 7]
t2 = [1, 2, 3, 4, 4, 3, 2, 1]
print(shuffle(t1, 3))  # Output: [2, 3, 5, 4, 1, 7]