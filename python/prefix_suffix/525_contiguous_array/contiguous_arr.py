"""
the idea is to use hash map to track occurrences of ones to zeros balance. So we will initialize two counters for ones and zeros
and on each iteration we will increase either of those. Next we want only to make a record in our hash only if diff (ones - zeros) has
not been recorded to hash. If it's the first occurrence we set key to be total ones minus total zeros, and value is the current iteration
index. We define our edge case is when number of zeros is equal to the number of ones, so we update our result to be their sum. In other case
we've already marked the first occurrence of that balance before, so we want to get that value from the hash, and it is going to be our 
shift index. And we want to calc that distance from that balance was first recorded up until the current iteration index. And we need
to update res value that will be max of either current_res or iteration index - shift_index (the one we got from the hash)
"""

def longest_contiguous_array(nums):
    ones, zeros = 0, 0
    longest_length = 0
    diff_to_index_map = {}

    for i, n in enumerate(nums):
        if n == 1:
            ones += 1
        else:
            zeros += 1

        if ones - zeros not in diff_to_index_map:
            diff_to_index_map[ones - zeros] = i
        
        if zeros == ones:
            longest_length = zeros + ones
        else:
            shift_index = diff_to_index_map[ones - zeros]
            longest_length = max(longest_length, i - shift_index)


    return longest_length
            
t1 = longest_contiguous_array([0,1,1,1,1,1,0,0,0])
print(t1) # 6
t2 = longest_contiguous_array([1,1,1,0,0])
print(t2) # 4