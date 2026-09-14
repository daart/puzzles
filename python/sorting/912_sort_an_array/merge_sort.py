def merge(l, r):
    res = [0] * (len(r) + len(l))
    li = 0;
    rj = 0;
    insertion_idx = 0
    
    while li < len(l) and rj < len(r):
        if l[li] >= r[rj]:
            res[insertion_idx] = r[rj]
            rj += 1
        else:
            res[insertion_idx] = l[li]
            li += 1
        insertion_idx += 1

    # if some items left in the left part
    while li < len(l):
        res[insertion_idx] = l[li]
        li += 1
        insertion_idx += 1

    # if some items left in the right part
    while rj < len(r):
        res[insertion_idx] = r[rj]
        rj += 1
        insertion_idx += 1

    return res
        
def merge_sort(nums):
    mid = len(nums) // 2

    if len(nums) == 1:
        return nums
    
    left_arr_part = merge_sort(nums[:mid])
    right_arr_part = merge_sort(nums[mid:])

    return merge(left_arr_part, right_arr_part)

t1 = merge_sort([5,2,3,1])
print(t1)
t2 = merge_sort([5,1,1,2,0,0])
print(t2)
