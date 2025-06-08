
def longestPalindrome(s):
    count_chars = [0] * 52

    for char in s:
        # decide if lower or upper case char:
        if ord('a') <= ord(char) <= ord('z'): #lowercase
            count_chars[ord(char) - ord('a')] += 1
        else: #uppercase
            count_chars[ord(char) - ord('A') + 26] += 1 # shift array to other half, since first half will be filled with lowercase

    
    palindrome_length = 0
    even_occurred_once = 0

    for i in range(len(count_chars)):
        if count_chars[i] % 2 == 0:
            palindrome_length += count_chars[i]
        else:
            palindrome_length += count_chars[i] - 1 # we can only add even at this point
            even_occurred_once = 1

    return palindrome_length + even_occurred_once

