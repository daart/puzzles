arr1 = [3,2,1,5,6,4]
arr2 = [3,2,3,1,2,4,5,5,6]
k1 = 2
k2 = 4

def find_Kth_largest(nums, k):
    target_index = len(nums) - k
    
    def quick_select(left, right):
        store_index = left

        for i in range(left, right):
            if nums[i] <= nums[right]:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1

        nums[store_index], nums[right] = nums[right], nums[store_index]

        if store_index > target_index:
            return quick_select(left, store_index - 1)
        elif store_index < target_index:
            return quick_select(store_index + 1, right)
        else:
            return nums[store_index]
    
    return quick_select(0, len(nums) - 1)



print(find_Kth_largest(arr1, k1))
print(find_Kth_largest(arr2, k2))