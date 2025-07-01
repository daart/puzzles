"""
The idea is to utilze bucket sort algorithm since we know that there will be only 3 possible ints [0, 1, 2]. This is a O(n) time and O(1) space
but not optimal since it has 2 passes not 1 as requested in description. So we will initialize an array of fixed len 3 of 0s. We will iterate over
nums and on each occurance we will increment corresponding value in counters arr by index. After that we have to refill nums array. We will need 
an outside counter that will be insertion index. We will iterate over counters, on each iteration we will start inner loop until we reached max number
of times this digit occured in the nums array, so we will update nums arr by insertion index (m) and increase that insertion index m +=1 
"""

def sort_colors(nums):
    counters = [0] * 3

    for i in range(len(nums)):
        counters[nums[i]] += 1

    m = 0
    for j in range(len(counters)):
        for _ in range(counters[j]):
            nums[m] = j
            m += 1

    return nums


t1 = sort_colors([2,0,2,1,1,0])
print(t1)
t2 = sort_colors([2, 0, 1])
print(t2)
