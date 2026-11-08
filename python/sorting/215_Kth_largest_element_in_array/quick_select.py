import random
arr1 = [3,2,1,5,6,4]
arr2 = [3,2,3,1,2,4,5,5,6]
k1 = 2
k2 = 4

def find_Kth_largest(nums, k):
    target_index = len(nums) - k

    def quick_select(left, right):
        left_part = left
        greater_part = right
        current_pos = left

        pivot = nums[random.randint(left, right)]

        while current_pos <= greater_part:
            if nums[current_pos] < pivot:
                nums[left_part], nums[current_pos] = (
                    nums[current_pos], nums[left_part]
                )
                left_part += 1
                current_pos += 1

            elif nums[current_pos] > pivot:
                nums[greater_part], nums[current_pos] = (
                    nums[current_pos], nums[greater_part]
                )
                greater_part -= 1

            else:
                current_pos += 1

        if target_index < left_part:
            return quick_select(left, left_part - 1)

        elif target_index > greater_part:
            return quick_select(greater_part + 1, right)

        else:
            return pivot

    return quick_select(0, len(nums) - 1)



print(find_Kth_largest(arr1, k1))
print(find_Kth_largest(arr2, k2))