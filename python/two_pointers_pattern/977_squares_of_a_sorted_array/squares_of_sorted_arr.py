"""
The idea is straightforward we will have two pointers and insertion index. One pointer will point to start of a list the other to the end.
Insertion position will be decremented on each iteration. On each step we will compare squared values for left and right pointers and 
if left is greater than the right we put left squared value in insertion position and increment left pointer, else we put right pointer squared
and decrement it by one. While loop with a condition left is smaller or equal than the right. We will also need a res array to fill with squared 
values. 
"""

def squares_of_sorted(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    pos = n - 1
    
    while left <= right:
        left_square = nums[left] * nums[left]
        right_square = nums[right] * nums[right]
        
        if left_square > right_square:
            result[pos] = left_square
            left += 1
        else:
            result[pos] = right_square
            right -= 1
        pos -= 1
    
    return result

t1 = squares_of_sorted([-4,-1,0,3,10])
print(t1)
t2 = squares_of_sorted([-7,-3,2,3,11])
print(t2)
