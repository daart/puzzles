nums1 = [2, 7, 11, 15]
target1 = 9
nums2 = [3, 2, 4]
target2 = 6
nums3 = [3, 3]
target3 = 6
nums4 = [4, 1, 7, 13, 9]
target4 = 16
nums5 = [1, 3, 5, 6, 8, 11, 13, 15]
target5 = 24

def two_sum(nums, target):
	result_map = {}

	for i in range(len(nums)):
		diff = target - nums[i]
		if diff in result_map:
			return [result_map[diff], i]
		else: 
			result_map[nums[i]] = i
    # if no match found
	return None
    


res1 = two_sum(nums1, target1)
res2 = two_sum(nums2, target2)      
res3 = two_sum(nums3, target3)
res4 = two_sum(nums4, target4)
res5 = two_sum(nums5, target5)

print(res1)
print(res2)
print(res3)
print(res4)
print(res5)