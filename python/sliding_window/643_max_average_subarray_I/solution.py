def findMaxAverage(nums, k):
    if not nums or k <= 0 or k > len(nums):
        return 0.0
    
    current_subseq_sum = float(sum(nums[:k]))
    max_subseq_sum = current_subseq_sum

    for i in range(k, len(nums)):
        current_subseq_sum = current_subseq_sum + nums[i] - nums[i - k]
        max_subseq_sum = max(current_subseq_sum, max_subseq_sum)

    return max_subseq_sum / k

t1 = findMaxAverage([1,12,-5,-6,50,3], 4)
print(t1)
t2 = findMaxAverage([5], 1)
print(t2)