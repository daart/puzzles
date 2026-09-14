def rotate(nums, k):
    i = k % len(nums)
    l, r = 0, len(nums) - 1

    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

    l2, r2 = 0, i - 1 
    while  l2 <= r2:
        nums[l2], nums[r2] = nums[r2], nums[l2]
        l2 += 1
        r2 -= 1

    l3, r3 = i, len(nums) - 1
    while  l3 <= r3:
        nums[l3], nums[r3] = nums[r3], nums[l3]
        l3 += 1
        r3 -= 1
    return nums


t1 = rotate([1,2,3,4,5,6,7], 3)
print(t1)
t2 = rotate([-1,-100,3,99], 2)
print(t2)