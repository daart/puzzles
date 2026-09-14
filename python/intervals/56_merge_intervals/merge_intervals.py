"""
The idea is we have to sort the array of intervals by intervals start value, since it is not sorted. So we can't make a solution better then O(n*logn) time.
We will also need some extra space so space complexity will be O(n). Identify edge case if there is 0 or 1 interval in intervals array, we should return intervals.
So we sort intervals array by interval[0] value in ascending order. We should also store currently merged interval, that will be initiated to intervals[0][0] and
intervals[0][1]. We will start iterating from 2nd interval, since currently merged interval is already set. On each iteration we want to compare current_merged
end value current_merged[1], as the current interval end with a current interval's starting value. If current_merged[1] >= intervals[i][0] we have to update
current_merged[1] to max value of either current interval's end value or current_merged[1]. In other case we have to append current_merged interval to resulting
intervals array, and update currently merged interval to be current interval's [start, end] values. After we exit the loop we have to append latest current_merged array into
res array, since within the loop we only append current_merged to res if intervals don't overlap and if intervals DO overlap, we only update current_merged[1], without
appending it to res.

"""

def merge_intervals(intervals):
    if len(intervals) <= 1:
        return intervals
    
    res = []
    intervals.sort(key=lambda x: x[0])
    current_merged = [intervals[0][0], intervals[0][1]]

    for i in range(1, len(intervals)):
        if current_merged[1] >= intervals[i][0]:
            current_merged[1] = max(intervals[i][1], current_merged[1])
        else:
            res.append(current_merged)
            current_merged = [intervals[i][0], intervals[i][1]]
    
    res.append(current_merged)

    return res


t1 = merge_intervals([[1,3],[2,6],[8,10],[15,18]])
print(t1)
t2 = merge_intervals([[1,3],[2,6],[8,10],[12,15],[14, 16], [16, 18]])
print(t2)
