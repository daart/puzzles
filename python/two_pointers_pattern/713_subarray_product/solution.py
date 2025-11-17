def subarray_product(nums, k):
    if k == 0:
        return 0
    sub_arrays_counter = 0
    left = 0
    sub_product = 1

    for r in range(len(nums)):
        sub_product *= nums[r]

        while left <= r and sub_product >= k:
            sub_product = sub_product // nums[left]
            left += 1
        sub_arrays_counter += (r - left + 1)
        
    
    return sub_arrays_counter
t1 = subarray_product([10,5,2,6], 100)
t2 = subarray_product([1,2,3], 0)

print(t1)
print(t2)