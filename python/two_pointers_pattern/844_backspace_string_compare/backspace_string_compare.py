"""
The idea is that we will traverse from the end of the strings and we will have a helper function that will 
check and return valid index. Within that function if current element is '#' we will have to increase backspace counter
But if backspace_counter is 0 (that means that all the chars were backspaced) and current char is NOT '#', we will just break
from the loop and return current index. And 3d scenario means that we are on a character that is exactly prior to '#' ('b' before '#')
and we have to execute backspace, that means decrement index (we are moving RTL) and decrement backspace_counter.

Within solution func body: start from the last indexes of each string. Iterate until any index is >= 0. Update
index on each iteration by assigning a value that is a result of a helper function for each string. And compare
each char by index. If updated index is out of bounds (<= 0) char is '' empty string. And we just compare the two chars,
if they are different return False. Decrement indexes on each iteration. If we passed the loop, that means that 
strings are equal so we return True.

"""

def backspaceCompare(s, t):
    def check_next_valid_char(string, index):
        backspace_count = 0
        while index >= 0:
            if backspace_count == 0 and string[index] != '#':
                break
            elif string[index] == '#':
                backspace_count += 1
            else:
                backspace_count -= 1

            index -= 1
        return index

    s_index, t_index = len(s) - 1, len(t) - 1

    while s_index >= 0 or t_index >= 0:
        s_index = check_next_valid_char(s, s_index)
        t_index = check_next_valid_char(t, t_index)

        char_s = s[s_index] if s_index >= 0 else ''
        char_t = t[t_index] if t_index >= 0 else ''

        if char_s != char_t:
            return False
        
        s_index -= 1
        t_index -= 1
    
    return True

        

t1 = backspaceCompare("ab#c","ad#c")
print(t1) # True
t2 = backspaceCompare("ab##", "c#d#")
print(t2) # True
t3 = backspaceCompare("a#c", "b")
print(t3) # False
t4 = backspaceCompare('s##r', 'rd#')
print(t4) # True