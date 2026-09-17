def find_anagrams(s, p):
    res = []
    p_dict = dict()
    s_dict = dict()

    for char in p:
        if char in p_dict:
            p_dict[char] += 1
        else:
            p_dict[char] = 1
    
    left = 0

    for right, c in enumerate(s):
        if c in s_dict:
            s_dict[c] += 1
        else:
            s_dict[c] = 1
        
        if right - left + 1 > len(p):
            left_char = s[left]
            s_dict[left_char] -= 1

            if s_dict[left_char] == 0:
                del s_dict[left_char]
        
            left += 1

        if s_dict == p_dict and right - left + 1 == len(p):
            res.append(left)
        
    return res

test1 = find_anagrams("cbaebabacd", "abc")
res1 = print(test1)

test2 = find_anagrams("abab", "ab")
res2 = print(test2)