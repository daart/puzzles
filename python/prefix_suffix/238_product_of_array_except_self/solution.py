"""
Since we can't use division and we need solution to be of O(n) space
The idea is following: We will create a resulting array that will be of same length as nums and have all values set to 1
since 1 is always be the starting accumulator for out of bound elements and current.
We are going to iterate over nums array once to set current accumulator (product) on each position. With each iteration, 
the next value of the resulting array or accumulator (product) will equal to previous element multiplied by current accumulator.
Since we can't calculate the entire product in one pass, we will need to do another one, which is still O(2n) == O(n). In first 
pass we set products of each preceeding element * current accumulator, with the greatest be the last one. In the 2nd pass
we will traverse the array from the back, and update values in resulting array, that will equal to product of resulting_arr[<index>] * right_accumulator.
And we will also need to update accumulator that will equal to multiplication of current_accum * nums[j]. So we will set the final values for resulting array that will be a multiplication of left and right
accumulators.
For example 1: [1, 2, 3, 4]
First pass i = 1, res = [1, 1, 1, 1]
nums[1] = 2; res[1] = res[1 - 1] * nums[1 - 1] = 1 * 1
Second pass i = 2; res = [1, 1, 2, 1]
nums[2] = 3; res[2] = res[2-1] * nums[2 - 1] = 1 * 2
Third Pass i = 3; [1, 1, 2, 6]
nums[3] = 4; res[3] = res[3-1] * nums[3-1] = 2 * 3 

After first pass: res = [1, 1, 2, 6];

RIght Pass j = len(nums) - 1 == 4 - 1 = 3
First pass j = 3, right_accum = 1
res[j] = res[j] * right_accum = 6 = 6 * 1 = 6
right_accum = nums[j] * right_accum => 1 = 4 * 1 
Second pass j = 2, right_accum = 4
res[j] = res[j] * right_accum = 2 = 2 * 4 = 8
right_accum = nums[j] * right_accum => 3 = 3 * 4 = 12 
Third pass j = 1, right_accum = 12
res[j] = res[j] * right_accum = 1 = 1 * 12 = 12
right_accum = nums[j] * right_accum => 12 = 2 * 12 = 24
Fourth Pass j = 0, right_accum = 24 
res[j] = res[j] * right_accum = 1 = 1 * 24 = 24

After 2nd pass :res = [1 * 24, 1 * 12, 2 * 4, 6 * 1] => [24, 12, 8, 6]


"""
def product_of_array(nums):
    res = [1] * len(nums)

    # left to right accumulation pass
    for i in range(1, len(nums)):
        res[i] = res[i - 1] * nums[i - 1]

    right_accum = 1
    
    for j in range(len(nums) - 1, -1, -1):
        res[j] = res[j] * right_accum
        right_accum *= nums[j] 
    return res

t1 = product_of_array([1,2,3,4])
print(t1) # [24, 12, 8, 6]
t2 = product_of_array([2,4,6,8])
print(t2) # [192, 96, 64, 68]
t3 = product_of_array([1,2])
print(t3) # [1, 1]
t4 = product_of_array([-1,1,0,-3,3])
print(t4)