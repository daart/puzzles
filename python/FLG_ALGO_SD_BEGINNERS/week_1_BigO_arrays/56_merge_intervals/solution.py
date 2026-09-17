def merge_intervals(intervals):
    if len(intervals) <= 1:
        return intervals

    intervals.sort(key=lambda interval: interval[0])
    merged_interval = [intervals[0][0], intervals[0][1]]
    res = []

    for i in range(1, len(intervals)):
        if merged_interval[1] >= intervals[i][0]:
            merged_interval[1] = max(
                merged_interval[1], intervals[i][1]
            )
        else:
            res.append(merged_interval)
            merged_interval = [intervals[i][0], intervals[i][1]]

    res.append(merged_interval)
    return res

res1 = merge_intervals([[1,3],[2,6],[8,10],[15,18]])
print(res1)

res2 = merge_intervals([[1,4],[4,5]])
print(res2)

res3 = merge_intervals([[4,7],[1,4]])
print(res3)

