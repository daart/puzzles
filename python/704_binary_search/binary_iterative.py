"""
similar time complexity O(log n), but better time sine we don't create helper functions and 
do not use recursive calls O(1) against O(log n ) in recursive solution.
Main idea is similar, we will have left right and mid indexes that will be updated on each
iteration (division). We start with left=0, right=last index of an array, mid will be
calculated within the loop since left, right could be changed. So we check if
current element equals target (this is loop brake case), if yes we return mid. If
current element is less then target, we need to update left which is going to be mid + 1 and
keep searching in the right part. If current element is greater then target we should update
right to be mid - 1 and keep searching in the left part. Iterate until left < right, if we havent found the target we return -1.
"""
def search(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target: #search in left slice
            right = mid - 1
        elif nums[mid] < target: #search in right slice
            left = mid + 1
    
    return -1

t1 = search([-1,0,3,5,9,12], 9)
print(t1)
t2 = search([-1,0,3,5,9,12], 4)
print(t2)
t3 = search([5], 5)
print(t3)