def findKthLargest(nums, k):
    min_num = min(nums)
    freq = [0] * (max(nums) - min(nums) + 1)

    for val in nums:
        freq[val - min_num] += 1


    target_pos = len(freq) - 1
    freq_pos = k
    while freq_pos > 0:
        freq_pos -= freq[target_pos]
        target_pos -= 1

    return target_pos + 1 + min_num