""" 13 Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""

"""
    this is my brute force solution with explicit checks for edge cases and multiple
    repetitions of pretty much the same. Still optimal O(n) time and O(1) space
"""
def toInt(s):
    map_roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    i = 0
    result = 0

    while i < len(s):
        if i + 1 < len(s) and s[i] == 'I' and s[i + 1] == 'V':
            result += 4
            i += 2
            continue
        if i + 1 < len(s) and s[i] == 'I' and s[i + 1] == 'X':
            result += 9
            i += 2
            continue
        if i + 1 < len(s) and s[i] == 'X' and s[i + 1] == 'L':
            result += 40
            i += 2
            continue
        if i + 1 < len(s) and s[i] == 'X' and s[i + 1] == 'C':
            result += 90
            i += 2
            continue
        if i + 1 < len(s) and s[i] == 'C' and s[i + 1] == 'D':
            result += 400
            i += 2
            continue
        if i + 1 < len(s) and s[i] == 'C' and s[i + 1] == 'M':
            result += 900
            i += 2
            continue

        result += map_roman_to_int[s[i]]
        i += 1

    return result


"""
    this one is more coinsise and compact. Instead of 6 explicit checks, we will just subtract.
    There is only one possible way of subtraction - current roman char is less then the direct next to it.
    In that case we subtract corresponding value, and later we will just add the next one as usual.
    Same O(n) O(1)
"""
def romanToInt(s):
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    result = 0
    for i in range(len(s)):
        if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
            result -= roman_map[s[i]]
        else:
            result += roman_map[s[i]]
    
    return result



s1 = 'III'
s2 = 'LIV'
s3 = 'MCMXCIV'
print(toInt(s1)) #3
print(toInt(s2)) #54
print(toInt(s3)) #1994