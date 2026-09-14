

nums1 = [1, 1, 2] # 2 => [1,2,_]
nums2 = [0,0,1,1,1,2,2,3,3,4] # 5 => [0,1,2,3,4,_,_,_,_,_]

def removeDuplicates(nums):
    if (len(nums) ==0):
        return 0
    placeholderInd = 0

    for currentInd in range(1, len(nums)):
        if nums[currentInd] != nums[placeholderInd]:
            placeholderInd += 1
            nums[placeholderInd] = nums[currentInd]
    
    return placeholderInd + 1

print(removeDuplicates(nums2))