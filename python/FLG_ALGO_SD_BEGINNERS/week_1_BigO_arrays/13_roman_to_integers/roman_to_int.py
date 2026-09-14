def roman_to_int(s):
    roman_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    result = 0
    for i in range(len(s)):
        if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
            result -= roman_map[s[i]]
        else:
            result += roman_map[s[i]]
    
    return result

t1 = 'III'
res1 = roman_to_int(t1)
print(res1)

t2 = 'LVIII'
res2 = roman_to_int(t2)
print(res2)

t3 = 'MCMXCIV'
res3 = roman_to_int(t3)
print(res3)