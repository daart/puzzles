def subarray_sum(nums, k):
    res = prefix_sum = 0
    # we start with 0: 1 since we have an empty space before the start of the array
    subarray_sum_map = {0: 1} 

    for num in nums:
        prefix_sum += num
        diff = prefix_sum - k

        if diff in subarray_sum_map:
            res += subarray_sum_map[diff]
        else:
            subarray_sum_map[prefix_sum] = subarray_sum_map.get(prefix_sum, 0) + 1

    return res
t1 = subarray_sum([1, -1, 2, 3, -2, 4], 3)
print(t1)
