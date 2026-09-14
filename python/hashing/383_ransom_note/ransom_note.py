""" 383 Ransom Note
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.


Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

Example 4:
Input: ransomNote = "audio", magazine = "auidiggo"
Output: true

Example 5:
Input: ransomNote = "audio", magazine = "audigg"
Output: false

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""

# not optimal O (m + n) Time complexity and O(n) Space
"""
main idea: we create an empty dictionary or hashMap with letters occured in magazine as keys
and their quantifier as value. On first iteration we fill the hashMap, if char is in hashMap increment, if not set to 1.
On the 2nd iteration we traverse ransomNote, if char is in HashMap and it's quantity is greater then 0,
decrement by 1, if not - return False.
If above conditions are met, that means that all the values in the hashMap are greater or equal than 0 thus return true
"""
def ransom_note(ransomNote, magazine):
    hashMap = {}

    for char in magazine:
        if char in hashMap:
            hashMap[char] += 1
        else:
            hashMap[char] = 1

    for char2 in ransomNote:
        if char2 in hashMap and hashMap[char2] > 0:
            hashMap[char2] -= 1
        else:
            return False
    return True



"""
Optimal solution is to utilise on of the restrictions and that is all characters are small english characters
In that case we can create an empty array of 26 zeros in it. There are 26 characters in English and we know that in 
ASCII 'a' has an index of 97. So we can just do ord(currentChar) - ord('a') to get current char's index in the array
and increment/decrement it. 
Same time complexity but improved space to O(1) since array is of fixed size 26
"""
def awesome_ransom_note(ransomNote, magazine):
    chars_count = [0] * 26;

    for char in magazine:
        chars_count[ord(char) - ord('a')] += 1
    
    for char2 in ransomNote:
        if chars_count[ord(char2) - ord('a')] > 0:
            chars_count[ord(char2) - ord('a')] -= 1
        else:
            return False
        return True


print(ransom_note('audio', 'auidiggo'))
print(ransom_note('aa', 'aab'))
print(awesome_ransom_note('audio', 'auidiggo'))
print(awesome_ransom_note('aa', 'aab'))
