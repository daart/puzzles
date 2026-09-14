"""
O(1) time and O(1) space but not optimal. Because we will need to iterate every char although in a fixed
32 length. worst case smth like '10000000000000000000000000000000000001' We will utilize modulo
division and shift to right operators. On each iteration we will update counter that will equal to the sum
of current counter + n % 2 (LSB) rightmost. And we have to shift one position right afterwards
"""

def non_optimal(n):
    counter = 0

    while n:
        counter += n % 2
        n = n >> 1

    return counter


t1 = non_optimal(11)
print(t1)
t2 = non_optimal(128)
print(t2)
t3 = non_optimal(2147483645)
print(t3)