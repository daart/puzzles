def two_sum(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        if target - nums[left] == nums[right]:
            return [left + 1, right + 1]
        elif target - nums[right] > nums[left]:
            left += 1
        else:
            right -= 1

    return []


t1 = two_sum([2,7,11,15], 9)
print(t1) # [1, 2]
t2 = two_sum([2,3,4], 6)
print(t2) # [1, 3]
t3 = two_sum([-1,0], -1)
print(t3) # [1, 2]
t4 = two_sum([1,3,4,5,7,8], 8)
print(t4) # [1, 5]
t5 = two_sum([1,3,4,5,6,8], 8)
print(t5) # [2, 4]