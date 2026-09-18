def product_of_the_array(nums):
    res = [1] * len(nums)

    # left pass
    l_accum = r_accum = 1

    for i in range(1, len(nums)):
        l_accum = nums[i - 1] * res[i - 1]
        res[i] = l_accum
    
    for j in range(len(nums) - 1, - 1, -1):
        res[j] *= r_accum
        r_accum = r_accum * nums[j]

    return res

test1 = product_of_the_array([1,2,3,4])
res1 = print(test1)

test2 = product_of_the_array([-1,1,0,-3,3])
res2 = print(test2)