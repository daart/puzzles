def maxSubArray(nums, k):
    current_window_subarray_sum = 0

    for sub_num in nums[:k]:
        current_window_subarray_sum += sub_num

    max_sum = current_window_subarray_sum

    for right in range(k, len(nums)):
        left_bound = right - k
        current_window_subarray_sum = current_window_subarray_sum - nums[left_bound] + nums[right]
        max_sum = max(current_window_subarray_sum, max_sum)

    return max_sum / k