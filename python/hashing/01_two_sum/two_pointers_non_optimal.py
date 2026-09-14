nums1 = [2, 7, 11, 15]
target1 = 9
nums2 = [3, 2, 4]
target2 = 6
nums3 = [3, 3]
target3 = 6
nums4 = [4, 1, 7, 13, 9]
target4 = 16
nums5 = [1, 3, 5, 6, 8, 11, 13, 15]
target5 = 24

def twoPointers(nums, target):
    nums_indexed = [(val, i) for i, val in enumerate(nums)]
    nums_indexed.sort(key=lambda x: x[0])

    l, r = 0, len(nums) - 1

    while l < r:
        current_sum = nums_indexed[l][0] + nums_indexed[r][0]
        if current_sum == target:
            return [nums_indexed[l][1], nums_indexed[r][1]]
        elif current_sum > target:
            r -= 1
        else:
            l += 1

    return []

res1 = twoPointers(nums1, target1)
res2 = twoPointers(nums2, target2)      
res3 = twoPointers(nums3, target3)
res4 = twoPointers(nums4, target4)
res5 = twoPointers(nums5, target5)

print(res1)
print(res2)
print(res3)
print(res4)
print(res5)
