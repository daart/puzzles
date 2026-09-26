def minSubArraySum(nums, k):
    left = total = 0
    min_subarray_len = len(nums) + 1

    for right in range(len(nums)):
        total += nums[right]

        while total >= k:
            min_subarray_len = min(min_subarray_len, right - left + 1)
            total -= nums[left]
            left += 1

    if min_subarray_len == len(nums) + 1:
        return 0
    
    return min_subarray_len

t1 = minSubArraySum([2,3,1,2,4,3], 7)
print(t1)

t2 = minSubArraySum([1, 4, 4], 4)
print(t2)

t3 = minSubArraySum([1, 1, 1, 1, 1, 1], 11)
print(t3)