"""
The idea is to utilize operators // floor division and % modulo division. We will initialize an empty array
of length n with zeros. We'll iterate in range of n. On each iteration we will fill currents array position with
a calculated number of bits. i % 2 calculates LSB (Least Significant Bit). For example 7 % 2 => 7 is '0111' in binary
and LSB is rightmost char so it's 1. While // 2 calculates previous power of 2 bits number. For example 7 // 2 = 3.5 but 
discarding .5 will be just 3. res[3] = 2
"""

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