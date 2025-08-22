def longestSubstring(s):
    left = 0
    longest = 0

    unique_chars = set()

    for right in range(len(s)):
        # if subsequence is invalid remove left window boundary
        while s[right] in unique_chars:
            unique_chars.remove(s[left])
            left += 1
        current_window_len = (right - left) + 1
        longest = max(longest, current_window_len)
        unique_chars.add(s[right])

    return longest


t1 = longestSubstring('abcabcbb')
print(t1)
t2 = longestSubstring('bbbbb')
print(t2)
t3 = longestSubstring('pwwkew')
print(t3)