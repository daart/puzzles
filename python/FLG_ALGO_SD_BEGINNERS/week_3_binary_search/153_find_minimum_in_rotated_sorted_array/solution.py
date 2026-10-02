""""
The idea is that we know the mechanics of the array rotation
and thus we need to check on every iteration the mid element
with the right pointing element. If mid element is less then
the right element, it means that the right part tis already sorted properly
and we have to look in the left part, otherwise in the right part.
"""
def find_min_in_rotated(nums):
    l, r = 0, len(nums) - 1

    while l < r:
        mid = (l + r) // 2
        
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid


    return nums[l]


t1 = find_min_in_rotated([1, 2, 4, 5, 6, 7, 0])
print(t1)

t2 = find_min_in_rotated([6, 7, 0, 1, 2, 4, 5])
print(t2)

t3 = find_min_in_rotated([4, 5, 6, 7, 0, 1, 2])
print(t3)
