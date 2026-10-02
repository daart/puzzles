"""
standard left, right, mid pointers for binary search.
On each section recalculate pointers. If mid pointing element
is greater then the one to the right, that means that we are
descending. So the peak is in the left part, we update right
to match mid. Not mid - 1 since the peak can still be on that element.
We only drop off mid pointer (mid + 1) when we are ascending/climbing
If mid pointing element is smaller -> look in the right part, 
update left to equal mid + 1. Chop untill the peak is found
and return left.
"""
def mountain_peak(nums):
    l, r = 0, len(nums) - 1

    while l < r:
        mid = (l + r) // 2

        # on descending steep 
        if nums[mid] > nums[mid + 1]:
            r = mid

        # on ascending steep
        else:
            l = mid + 1

    return l