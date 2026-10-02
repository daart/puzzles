def search_in_rotated_sorted(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid
        # check if left slice is already sorted
        elif nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return - 1


t1 = search_in_rotated_sorted([4,5,6,7,0,1,2], 0)
print(t1)

t2 = search_in_rotated_sorted([4,5,6,7,0,1,2], 3)
print(t2)

t3 = search_in_rotated_sorted([6, 7, 0, 1, 2, 3, 4, 5], 7)
print(t3)

t4 = search_in_rotated_sorted([6, 7, 0, 1, 2, 3, 4, 5], 4)
print(t4)