def product_of_the_array(nums):
    res = [1] * len(nums)

    # left pass
    l_accum = r_accum = 1
    n = len(nums)

    for i in range(1, n):
        l_accum *= nums[i]
        res[i] = l_accum

    for j in range(n - 1, -1, -1):
        res[j] = r_accum
        r_accum *= nums[j]

    return res

def product_of_the_array2(nums):
    res = [1] * len(nums)

    # left pass
    l_accum = r_accum = 1
    n = len(nums)

    for i in range(n):
        res[i] = l_accum
        l_accum *= nums[i]

    for j in reversed(range(n)):
        res[j] *= r_accum
        r_accum *= nums[j]

    return res

test1 = product_of_the_array([1,2,3,4])
res1 = print(test1)

test2 = product_of_the_array([-1,1,0,-3,3])
res2 = print(test2)