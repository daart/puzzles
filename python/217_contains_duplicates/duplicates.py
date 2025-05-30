""" 217 Contains Duplicates
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

"""
Solution is super straightforward. There is no way we can get O(1) space complexity without sacrificing time.
We could have sorted the array to check if prev/next are equal but that will bump the time complexity to O(n*log(n)). So
standard approcah will be optimal we create a dictionary or a Set since we want unique nums, traverse through nums and check
if num is in set/dict return True without increment, we've found the duplicate. In other case set num counter to 1. If no duplicates found
return False.
"""
def containsDuplicate(nums):
    countNums = set()

    for num in nums:
        if num in countNums:
            return True
        countNums.add(1)
    
    return False