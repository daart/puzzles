def getBiggestContainer(nums):
    max_area, left, right = 0, 0, len(nums) - 1

    while left < right:
        # find min height
        current_area = min(nums[left], nums[right]) * (right - left)
        max_area = max(max_area, current_area)

        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1
        
    return max_area

t1 = getBiggestContainer([1,8,6,2,5,4,8,3,7])
print(t1)
