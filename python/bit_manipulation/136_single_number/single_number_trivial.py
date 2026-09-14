"""
Idea is super straightforward: we need a hasMap with integers as keys,
and their occurances as values. This is O(n) Time and O(n) space. 
One of the requirements is to decrease space to O(1).

"""
def single_num(nums):
    integersHash = {}

    for num in nums:
        if num in integersHash:
            integersHash += 1
        else:
            integersHash[num] = 1
    
    for key in integersHash:
        if integersHash[key] == 1:
            return key
    