"""
the idea is that we don't need additional memory storage for passing array. We will just have
2 variables that keep track of counter and another one of a current integer
According to description we can be sure that there is always a majority element
and we now for sure that it has to appear at least len(array) / 2 + 1 times.
So that means on each iteration we will check if current el equals to candidate. If yes increment counter by one.
If current counter reached zero update current integer (candidate), and reset counter to be 1.
In other case we will decrement current_counter. After we passed through the entire
array we will just return current element
"""

def majorityElement(nums):
    current_num = nums[0];
    current_num_counter = 1

    for i in range(1, len(nums)):
        if nums[i] == current_num:
            current_num_counter += 1
        elif current_num_counter == 0:
                current_num = nums[i]
                current_num_counter = 1
        else:
            current_num_counter -= 1
    
    return current_num

t1 = majorityElement([3,2,3])
print(t1)
        
t2 = majorityElement([2,2,1,1,1,2,2])
print(t2)

t3 = majorityElement([2, 1, 2, 1, 2])
print(t3)

t4 = majorityElement([6, 5, 5])
print(t4)