def three_sum_closest(nums, target):
    nums.sort()
    closest_sum = float('inf')
    end = len(nums)
    
    for i in range(end):
        # skip the same value
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        li, ri = i + 1, end - 1

        while li < ri:
            current_sum = nums[i] + nums[li] + nums[ri]
            
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum

            if current_sum == target:
                return current_sum
            elif current_sum - target < 0:
                li += 1
            else:
                ri -= 1

    return closest_sum

t1 = three_sum_closest([-1,2,1,-4], 1)
t2 = three_sum_closest([0, 0, 0], 1)
print(t1)
print(t2)