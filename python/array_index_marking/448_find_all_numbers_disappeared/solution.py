"""
The solution is a trick how we can utilize the fact that we have only positive nums in the array in the range of [1, n] where
n is len(nums). We have a direct mapping for a ranged nums array
indices: [0, 1, 2, 3, 4]  =>
values:  [1, 2, 2, 3, 2]  => value 1 is at 1 - 1 position (shift one position leftward because indices start from 0) =>
We want to somehow mark values that have already appeared. For that we can multiply on -1, meaning that if a val is negative
it has already been seen. And since there can be repetitive nums and current val can be negative we should use absolute method
to turn value to positive value. So during our first iteration, we are marking values that have already occurred in the sequence.
In the second iteration we will check if val is positive, means it was missing in the first passage, we will append in the resulting
array not the value itself, but it's indice val + 1 (shift to the right)  


!!!GROK explanation:
Step-by-Step ExplanationMapping Numbers to Indices:Each number x in nums (where 1 <= x <= n) corresponds to index x-1 in the array. For example:nums = [4,3,2,7,8,2,3,1], n=8, range [1,8].
Number 4 maps to index 4-1 = 3.
Number 1 maps to index 1-1 = 0.

This is why you compute i = abs(n) - 1: it maps value n to its “ideal” index.

Marking Seen Numbers:For each number n in nums, go to index abs(n) - 1 and make the value there negative (nums[i] = -1 * abs(nums[i])).
Why abs(n)? Because nums may have duplicates (e.g., 2 appears twice), and during the loop, some values may already be negative from prior markings. abs(n) ensures we map to the correct index.
Why abs(nums[i])? When marking, nums[i] might already be negative (from a previous iteration), but we want its absolute value to preserve the number’s identity before flipping its sign.
Effect: If a number x appears in nums, the value at index x-1 becomes negative, marking that x is present.

Finding Missing Numbers:After the first loop, indices with positive values correspond to numbers that were never marked (i.e., missing).
For index i, if nums[i] > 0, then number i+1 is missing (add i+1 to result).
Why i+1? Because indices are 0-based (0 to n-1), but numbers are 1-based (1 to n).

Example 1: nums = [4,3,2,7,8,2,3,1]Initial: nums = [4,3,2,7,8,2,3,1], n=8, range [1,8].
First Loop (Marking):
n=4: i = abs(4)-1 = 3, nums[3] = 7, make it -7: nums = [4,3,2,-7,8,2,3,1].
n=3: i = abs(3)-1 = 2, nums[2] = 2, make it -2: nums = [4,3,-2,-7,8,2,3,1].
n=2: i = abs(2)-1 = 1, nums[1] = 3, make it -3: nums = [4,-3,-2,-7,8,2,3,1].
n=7: i = abs(7)-1 = 6, nums[6] = 3, make it -3: nums = [4,-3,-2,-7,8,2,-3,1].
n=8: i = abs(8)-1 = 7, nums[7] = 1, make it -1: nums = [4,-3,-2,-7,8,2,-3,-1].
n=2: i = abs(2)-1 = 1, nums[1] = -3, make it -3 (use abs): nums = [4,-3,-2,-7,8,2,-3,-1].
n=3: i = abs(3)-1 = 2, nums[2] = -2, make it -2: nums = [4,-3,-2,-7,8,2,-3,-1].
n=1: i = abs(1)-1 = 0, nums[0] = 4, make it -4: nums = [-4,-3,-2,-7,8,2,-3,-1].

Second Loop (Result):
i=0: nums[0] = -4 (negative, skip).
i=1: nums[1] = -3 (negative, skip).
i=2: nums[2] = -2 (negative, skip).
i=3: nums[3] = -7 (negative, skip).
i=4: nums[4] = 8 (positive, add i+1 = 5 to result).
i=5: nums[5] = 2 (positive, add i+1 = 6 to result).
i=6: nums[6] = -3 (negative, skip).
i=7: nums[7] = -1 (negative, skip).

Result: [5,6] (missing numbers).

Example 2: 
nums = [1,1]
Initial: nums = [1,1], n=2, range [1,2].
First Loop:n=1: i = abs(1)-1 = 0, nums[0] = 1, make it -1: nums = [-1,1].
n=1: i = abs(1)-1 = 0, nums[0] = -1, make it -1: nums = [-1,1].

Second Loop:i=0: nums[0] = -1 (negative, skip).
i=1: nums[1] = 1 (positive, add i+1 = 2 to result).

Result: [2] (missing number).


"""

def find_disappeared_nums(nums):
    # mar existing nums
    for n in nums:
        i = abs(n) - 1
        nums[i] = -1 * abs(nums[i])

    res = []

    for i, val in enumerate(nums):
        if val > 0:
            res.append(i + 1)

    return res

t1 = find_disappeared_nums([4,3,2,7,8,2,3,1]) # [5, 6]
t1 = find_disappeared_nums([1, 1]) # [2]