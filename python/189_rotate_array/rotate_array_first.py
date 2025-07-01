"""
the idea is simple but this solution can't be submitted since it is required to solve it with in place substitution and O(1) space.

It's O(n) time and space solution. So we initiate an empty array of 0 of same len as nums. The trick is to fill the array with a shifted
values. In order to do that we have to use % division. In order to fill left part of the resulting array before the revert index k, we have to
divide (i + k) % len(nums), so when we reach the last element, insertion index will be set to 0.

"""

def rotate(nums, k):
    res = [0] * len(nums)

    for i in range(len(nums)):
        res[(i + k ) % (len(nums))] = nums[i]

    return res

t1 = rotate([1,2,3,4,5,6,7], 3)
print(t1)
t2 = rotate([-1,-100,3,99], 2)
print(t2)
