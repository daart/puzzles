def max_water(nums):
    left, max_area, right = 0, 0, len(nums) - 1

    while left <= right:
        current_max_area = min(nums[left], nums[right]) * (right - left)
        max_area = max(current_max_area, max_area)

        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1


    return max_area

res1 = max_water([1,8,6,2,5,4,8,3,7])
print(res1)