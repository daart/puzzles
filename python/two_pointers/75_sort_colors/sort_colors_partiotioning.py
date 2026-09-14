"""
This is a bit harder in implementation but gives us an ability to fullfil requirement of a single pass and in place update. Main idea:
since we have only 3 digits and we want an array in ascending order, we assume that all the 0s will be in the left part, 2s will be in the 
right part and 1s will be placed in the middle. So we can have 2 pointers left and right that will be pointing to left_index_insertion and right_index_insertion.
All the elements that are to the right of right_pointer are already sorted and there are only 2s. All the elements to the left of left_insertion are 0s and also sorted.
When left_insertion_index surpasses right one, we've reached our goal and we have to break out of the loop. 
There is a special case when left_insertion_index is currently at 1 so we won't increment left_insertion_index. In other cases if left_insertion_index points 
at 2 we should swap it with right_insertion_index. And if right_insertion_index points at 0 we should swap it with left.
"""

def sort_colors(nums):
    left, right = 0, len(nums) - 1
    iteration_index = 0

    def swap(i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    while iteration_index <= right:
        if nums[iteration_index] == 2:
            swap(iteration_index, right)
            right -= 1
            iteration_index -= 1
        elif nums[iteration_index] == 0:
            swap(left, iteration_index)
            left += 1

        iteration_index += 1

    return nums

t1 = sort_colors([2,0,2,1,1,0])
print(t1)
t2 = sort_colors([2, 0, 1])
print(t2)