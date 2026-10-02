def intersection(nums1, nums2):
    counter = {}
    res = []

    for n1 in nums1: 
        if n1 in counter:
            counter[n1] += 1
        else:
            counter[n1] = 1

    for n2 in nums2:
        if n2 in counter and counter[n2] > 0:
            counter[n2] -= 1
            res.append(n2)

    return res


"""" if 2 arrays are already sorted, we use 2 pointers pattern and compare
num of each array. If there's a match, add to resulting array.
"""
def sorted_intersection(nums1, nums2):
    i = j = 0
    res = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            res.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        elif nums2[j] < nums1[i]:
            j += 1

    return res