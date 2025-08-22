
def three_sum(nums):
    res = []
    nums.sort()

    for index, val in enumerate(nums):
        # avoid duplicates in triplets
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

                while nums[left] == nums[left - 1] and left < right:
                    left += 1

    return res


t1 = three_sum([-1,0,1,2,-1,-4])
print(t1) #[[-1,-1,2],[-1,0,1]]