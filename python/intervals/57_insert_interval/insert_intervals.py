def insert(intervals, newInterval):
    resulting_intervals = []

    for i in range(len(intervals)):
        # newInterval's max value is less then current intervals min value
        if newInterval[1] < intervals[i][0]:
            resulting_intervals.append(newInterval)
            return resulting_intervals + intervals[i:]
        # new intervals min value is greater then current intervals max value. So we insert current interval in resulting_interval
        # but do not exit the function because potentially there could be other overlaps in next iterations
        elif newInterval[0] > intervals[i][1]:
            resulting_intervals.append(intervals[i])
        # intervals are actually overlapping so we have to merge by calculating min and max values of a new interval   
        else:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

    resulting_intervals.append(newInterval)

    return resulting_intervals

t1 = insert([[1,3],[6,9]], [2,5]) 
print(t1) # [[1,5],[6,9]]

t2 = insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4, 8])
print(t2) # [[1,2],[3,10],[12,16]]

t3 = insert([[6,7],[8,10],[12,16]], [1,4])
print(t3) # [[1,4], [6,7],[8,10],[12,16]]
