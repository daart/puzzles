"""
very silly solution he create a dictionary that will track number of times an integer appeared in the input array.
In the end another pass through the dictionary to check for majority element, the one that is greater than
input arrays's len / 2
"""

def majorityElement(nums):
    nums_hash = {}

    for i in nums:
        if i in nums_hash:
            nums_hash[i] += 1
        else:
            nums_hash[i] = 1
    
    for i in nums_hash.keys():
        if nums_hash[i] > (len(nums) / 2):
            return i
        
t1 = majorityElement([3,2,3])
print(t1)
        
t2 = majorityElement([2,2,1,1,1,2,2])
print(t2)