def countBits(n):
    res = [0] * (n + 1)

    for i in range(0, n + 1):
        res[i] = res[i // 2] + (i % 2)

    return res


t1 = countBits(2)
print(t1)
t2 = countBits(5)
print(t2)
t3 = countBits(17)
print(t3)