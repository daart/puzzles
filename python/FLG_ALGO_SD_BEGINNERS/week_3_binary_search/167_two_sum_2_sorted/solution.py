def twoSum(nums, target):
    l, r = 0, len(nums) - 1

    while l < r:
        if target - nums[l] == nums[r]:
            return [l + 1, r + 1]
        elif target - nums[r] > nums[l]:
            l += 1
        else:
            r -= 1

    return []]
