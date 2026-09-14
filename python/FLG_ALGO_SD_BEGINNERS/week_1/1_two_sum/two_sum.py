"""
We will need a dictionary with key/value as num/index to find target indices.
"""
def two_sum(nums, target):
    res = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in res:
            return [res[diff], i]
        else:
            res[num] = i
    return None

res1 = two_sum([2,7,11,15], 9)
print(res1);

res2 = two_sum([3,2,4], 6)
print(res2)

res3 = two_sum([3, 3], 6);
print(res3)