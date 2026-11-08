"""
the idea is that we can't use sorting here. But we can utilize built in Math max method in python.
For example we are given the k as the largest element in the array, so if k is 2 in nums= [3, 2, 1, 5, 6, 4]
that means that the largest number is 6 in this array, and we want 2nd largest so it's 5. The idea is that
we'll have a counter that will start from 0 and will tick/increment on each round until it reaches k - 1 and on 
each iteration we will just pop that number from the arry. Why k-1 because pop does not return or save that element anywhere
and we need it. So on k-1 step we will no for sure that max element that left in the remaining array is currently equal to k.
So as a result we'll just return max(nums). It's not ideal in terms of time since it's O(n * k) where n is nums len.
In worst case it's O(n ** 2) 
"""

arr1 = [3,2,1,5,6,4]
arr2 = [3,2,3,1,2,4,5,5,6]
k1 = 2
k2 = 4

def find_Kth_largest(nums, k):
    counter = 0

    while counter < k - 1:
        nums.remove(max(nums))
        counter += 1

    return max(nums)

print(find_Kth_largest(arr1, k1))
print(find_Kth_largest(arr2, k2))