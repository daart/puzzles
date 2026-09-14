"""solution idea:
it's a classic two pointer pattern. One pointer points into current iterable element, the other one
onto current write position. We check only for non zero elements, and if the element is non zero we put
it into current write position and increment write index. To limit number of operations we can additionally
check on whether the current write element equals iterable element
""" 

def move_zeros(nums):
    i = j = 0

    while i < len(nums):
        if nums[i] != 0:
            if nums[j] != nums[i]:
                nums[j] = nums[i]
            j += 1
        i += 1
    
    while j < len(nums):
        if nums[j] != 0:
            nums[j] = 0
        j += 1

    return nums

t1 = [0,1,0,3,12]
res1 = move_zeros(t1)
print(res1)
t2 = [0]
res2 = move_zeros(t2)
print(res2)
t3 = [0, -2, 0, 1]
res3 = move_zeros(t3)
print(res3)