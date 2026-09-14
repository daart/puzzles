"""
there is a trick how we can utilize XOR operator. XOR only returns 1 if
it is compared with 0. If 1 is XORed against 1, it resets to 0. 
Given the fact that every integer appears twice
except one, we will implement XOR on each and every integer in nums,
while storing a result of a current el XOR. In the end the result will store
a single element without a pair in nums
"""

def binary_solution(nums):
    result = 0

    for num in nums:
        result = num ^ result

    return result

print(binary_solution([4,1,2,1,2]))