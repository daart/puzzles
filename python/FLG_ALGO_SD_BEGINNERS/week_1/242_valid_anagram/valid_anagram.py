"""
The idea is pretty simple we will need to have a dictionary with key as a character from the string
and a value as a counter of occurrences of that char. On the first run we are going to fill the dict 
with char occurrences in the 1st string, in the next run we will compare the 2nd string on the same 
number of char occurrences. If length of the 1st and 2nd strings are not equal, return False. 
If during 2nd run at least one char isn't found in the pre filled characters dict 
or it's value is already 0 -> return False. Otherwise return True

"""
def valid_anagram(s, t):
    if len(s) != len(t):
        return False

    abc = {}

    for char in s:
        if char in abc:
            abc[char] += 1
        else:
            abc[char] = 1

    for char in t:
        if char not in abc:
            return False
        if abc[char] == 0:
            return False
        
        abc[char] -= 1

    return True

res1 = valid_anagram("anagram", "nagaram")
print(res1)

res2 = valid_anagram("rat", "car")
print(res2)
