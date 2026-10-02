def max_subarray(nums):
    max_subarray_sum = nums[0]
    current_sum = 0

    for n in nums:
        if current_sum < 0:
            current_sum = 0

        current_sum += n
        max_subarray_sum = max(max_subarray_sum, current_sum)

    return max_subarray_sum

t1 = max_subarray([-2,1,-3,4,-1,2,1,-5,4])
print(t1)

