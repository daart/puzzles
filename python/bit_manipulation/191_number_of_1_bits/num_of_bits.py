"""
Still O(1) time and O(1) space but we don't need to iterate every char. Instead we will iterate only 
number of 1s found in a binary representation by utilizing & operator. This is logical AND and returns
1 if only both operands are 1. For example n(11) => binary '1011'. We need to think how to turn it into
'1010' for next iteration and increment counter. 
iteration 1:

'1011' - 1 => '0101'
so '1011' & '1010' = '1010'
counter = 1

iteration 2:
'1010' - 1 => '1000'
'1010' & '1000' => '1000'
counter = 2

iteration 3:
'1000' - 1 => '0111'
'1000' & '0111' => '0000'
counter = 3

exit loop since n is '0000'


For n = 33 => '100001'. How to turn it into '100000' and inc counter. By subtracting 1. 
next iteration '100000' - 1 => '0111111'. So '100000' & '0111111' => '0000000'
"""

def hammingWeight(n):
    counter = 0

    while n > 0:
        n = n & (n - 1)
        counter += 1

    return counter

t1 = hammingWeight(11)
print(t1)
t2 = hammingWeight(128)
print(t2)
t3 = hammingWeight(2147483645)
print(t3)