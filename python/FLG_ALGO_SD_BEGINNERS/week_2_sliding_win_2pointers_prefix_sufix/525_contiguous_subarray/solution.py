def contiguous(nums):
    res, balance = 0, 0
    balance_by_index_map = {}

    for i, num in enumerate(nums):
        balance += 1 if num == 1 else -1

        if balance not in balance_by_index_map:
            balance_by_index_map[balance] = i
        elif balance == 0:
            res = i + 1
        else:
            res = max(res, i - balance_by_index_map[balance])

    return res

t1 = contiguous([1,0,1,1,1,0,0,1,1,0,0,0])
print(t1)

t2 = contiguous([1,0,1,0])
print(t2)