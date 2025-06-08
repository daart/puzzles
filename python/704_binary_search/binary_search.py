"""
This is non optimal recursive solution but withing required O(log n) solution. 
The main idea is that we will have a helper function that will accept 4 arguments
an array of numbers
left most element index
right most element index 
and target
on each function call we will calculate current mid index. Check if we reached one of base cases:
1) if left is less then right we return -1, since we out of bounds
2) if current element equals target we return current mid.

Check if nums[mid] is greater than target, we should continue searching in the left part of the
array. So we will call search function but with updated left and right. We know for sure that every element 
from mid index(included) in the array does not satisfy our target, so left will remain unchanged while
right will be mid - 1. 
And in other case if nums[mid] is less then target, we should look for in the right part of the nums array.
Left will be mid + 1, since everything before mid indexed element (included) should be dropped down,
right remains unchanged.

"""
def search(nums, left, right, target):
    mid = (left + right) // 2
    if left > right:
        return -1
    if nums[mid] == target:
        return mid
    if nums[mid] > target:
        return search(nums, left, mid - 1, target)
    if nums[mid] < target:
        return  search(nums, mid + 1, right, target)

def binary_search_naive(nums, target):
    left = 0
    right = len(nums) - 1
    
    return search(nums, left, right, target)

t1 = binary_search_naive([-1,0,3,5,9,12], 9)
print(t1)
t2 = binary_search_naive([-1,0,3,5,9,12], 4)
print(t2)