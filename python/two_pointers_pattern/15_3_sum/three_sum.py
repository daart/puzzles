"""
At first we want to make sure that the array is sorted so we use sort method. The idea is that we will have an outer pointer
(current_iteration_index) and two pointers left and right (left will be current_iteration_index + 1, and right will point to the end)
We have to check if current value (nums[current_iteration_index] is positive > 0) and break out of the loop, since we can't sum up to 0
at this point. And check for duplication of triplets. If current_iteration_index > 0 and previous value == nums[current_iteration_index]
we should skip this iteration. On every iteration of current_iteration_index, we will initialize left, right pointers. Check the current sum
if it sums to 0. If the sum is greater than 0, we have to decrease the sum by decrementing right pointer. If the sum is less than 0, increment
left pointer. If the sum equals to 0, append the triplet array to resulting array, decrement right pointer and increment left. But we have to check for duplicate triplets in the inner loop
too for numbers two and three in the triplet. The first one is checked with previous value == nums[current_iteration_index]. Example [-2, -2, 0, 0, 2, 2] , current_iteration_index = 0, nums[current_iteration_index] = -2, left = 2, right = 5;
first triplet [-2, 0, 2] 
"""
def three_sum(nums):
    res = []
    nums.sort()

    for index, val in enumerate(nums):
        # if current value is positive, than all the next values are positive too, 
		# there is no way those can sum up to 0
        if val > 0:
            break
        # only use unique first value once
        if index > 0 and val == nums[index - 1]:
            continue
        left, right = index + 1, len(nums) - 1

        while left < right:
            temp_sum = val + nums[left] + nums[right]
            if temp_sum > 0:
                right -= 1
            elif temp_sum < 0:
                left += 1
            else:
                res.append([val, nums[left], nums[right]])
                left += 1
                right -= 1
                
                # skip duplicate values of nums[left] and nums[right] after finding valid triplet [-2, -2, 0, 0, 2, 2]
                # should return only one triplet [-2, 0, 2]
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
                while nums[right] == nums[right + 1] and left < right:
                    right -= 1

    return res


t1 = three_sum([-1,0,1,2,-1,-4])
print(t1) #[[-1,-1,2],[-1,0,1]]
t2 = three_sum([-2, -2, 0, 0, 2, 2])
print(t2)
