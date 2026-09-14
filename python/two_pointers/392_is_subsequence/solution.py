"""
The main idea is to have a matched characters counter (first pointer) that will be incremented every time 
character from string s matches character from string t. 2nd pointer will be a current iteration index of string t
If s[counter] == t[current_index] increment counter, if not only current_index is incremented. If length of s
equals to counter return true, if not false.
"""
def isSubSeq(s, t):
    if len(s) == 0:
        return True
    if not t:
        return False
    matches_counter = 0

    for current_pos in range(len(t)):
        if matches_counter < len(s) and t[current_pos] == s[matches_counter]:
            matches_counter += 1
        if matches_counter == len(s):
            return True
        
    return matches_counter == len(s)


t1 = isSubSeq('abc', 'ahbgdc')
t2 = isSubSeq('axc', 'ahbgdc')
t3 = isSubSeq('acvm', 'afm');
t4 = isSubSeq('', 'abv');

print(t1)
print(t2)
print(t3)
print(t4)