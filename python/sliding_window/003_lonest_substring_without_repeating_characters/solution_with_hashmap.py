def longestSubstring(s):
    leftIndex = 0
    longestCount = 0
    mapCharByIndex = {}

    for rightIndex in range(len(s)):
        if s[rightIndex] in mapCharByIndex and mapCharByIndex[s[rightIndex]] >= leftIndex:
            leftIndex = mapCharByIndex[s[rightIndex]] + 1
        else:
            longestCount = max(longestCount, rightIndex - leftIndex + 1)

        mapCharByIndex[s[rightIndex]] = rightIndex

    return longestCount

t1 = longestSubstring('abcabcbb')
print(t1)
t2 = longestSubstring('bbbbb')
print(t2)
t3 = longestSubstring('pwwkew')
print(t3)