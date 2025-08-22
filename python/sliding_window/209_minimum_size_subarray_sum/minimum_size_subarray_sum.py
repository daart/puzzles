"""
we have to consider a so called diff of a target - current element. 
If a diff is greater than 0 we should move rightIndex, if less then we should move leftPointer
"""

def minSizeSubArray(target , nums):
    left = 0
    minSize = float('inf')
    current_sum = 0

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            minSize = min(minSize, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return 0 if minSize == float('inf') else minSize


t1 = minSizeSubArray(7, [2,3,1,2,4,3])
print(t1)
t2 = minSizeSubArray(4, [1, 4, 4])
print(t2)
t3 = minSizeSubArray(11, [1,1,1,1,1,1,1,1])
print(t3)