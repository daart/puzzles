""" 507
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Constraints:

0 <= n <= 30
"""

""" the idea is identical with climbing stairs O(n) time O(1) space"""
def fibo(n):
    if n == 0:
        return 0
    
    prev = 0;
    cur = 1

    for i in range(n - 1):
        temp = cur
        cur += prev
        prev = temp
    
    return cur

t1 = fibo(2)
t2 = fibo(3)
t3 = fibo(4)
t4 = fibo(5)
t5 = fibo(6)

print(t1)
print(t2)
print(t3)
print(t4)
print(t5)