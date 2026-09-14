"""
pretty straightforward two pointers pattern. We will have two pointers one pointing start, another pointing end. On each iteration we will check

if target - nums[left] is equal to nums[right] we just return an array of those indexes + 1 (due to restriction in description). Elseif case

if sum of a left and right respective values is greater than the target, we should decrement right index, in all other cases (else clause) increment left.


"""

def two_sum(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        if target - nums[left] == nums[right]:
            return [left + 1, right + 1]
        elif nums[right] + nums[left] > target:
            right -= 1
        else:
            left += 1

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