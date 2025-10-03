"""
The idea is we need to somehow calculate difference between the expected nums sum and actual nums sum.
Actual nums sum for arr=[3, 0, 1] => 3 + 0 + 1 = 4 and the EXPECTED sum is for range [0, 3] could be found
with formula n(n + 1) / 2 => (3 * 4) / 2 = 6. For that we will need 2 passes making time complexity O(2n)
but we can make it in one pass with a slight trick. For array of nums the expected sum of numbers will equal to
the sum of it's indices + the length of nums array => [0, 1, 2] + len(nums) => 0 + 1 + 2 + 3 => 6
We will initialize res to len(nums), and on each iteration we will just subtract current nums value from indice and
add it to res. When all of the values are eliminated, the remaining number will be our missing number.
"""
def find_missing_num_diff(nums):
    res = len(nums)

    for i in range(nums):
        res += (i - nums[i])

    return res

"""
The idea is very similar to previous, the only difference is that we will utilize XOR operator that works like this
3 ^ 2 => 011 ^ 010 => 001 => 3 ^ 2 = 1; And we don't care about the order here because for 3 ^ 4 ^ 3 => 3 ^ 3 => 0; 0 ^ 4 = 4
So on each iteration we will eliminate a matching pair found, leaving the single unpaired value as our missing value.
!!!NOTE:!!! For both solutions the formula is for range [0, n] expected sum is 0 through n - 1 (included) + n. But since python's
range excludes last el, we use nums(len) here. 
"""
def find_missing_num_xor(nums):
    res = len(nums)

    for i in range(len(nums)):
        res ^= i ^ nums[i]
    
    return res

t1 = find_missing_num_diff([0,1])
t2 = find_missing_num_diff([9,6,4,2,3,5,7,0,1])
t_1 = find_missing_num_xor([3, 0, 1])
t_2 = find_missing_num_xor([9,6,4,2,3,5,7,0,1])