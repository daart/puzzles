import heapq

arr1 = [3,2,1,5,6,4]
arr2 = [3,2,3,1,2,4,5,5,6]
k1 = 2
k2 = 4


def find_Kth_largest(nums, k):
    # beacuse heapq is min heap in python so we invert values

    for i in range(len(nums)):
        nums[i] = -nums[i]

    # build a heap with heapify method
    heapq.heapify(nums)

    for _ in range(k-1):
        heapq.heappop(nums)
    return - heapq.heappop(nums)



print(find_Kth_largest(arr1, k1))
print(find_Kth_largest(arr2, k2))