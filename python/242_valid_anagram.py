
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

def anagram(s, t):
    if len(s) != len(t):
        return False
    
    abc = {}

    # Count frequencies for s
    for i in range(len(s)):
        if s[i] in abc:
            abc[s[i]] += 1
        else:
            abc[s[i]] = 1  # Start the count at 1, not 0
    
    # Decrement frequencies for t
    for j in range(len(t)):
        if t[j] in abc:
            abc[t[j]] -= 1
        else:
            return False  # If a letter in t isn't in s, they can't be anagrams
    
    # Check if all counts are 0
    all_zero = all(value == 0 for value in abc.values())

    return all_zero