def longest_substr(s):
    window_start = 0
    longest_substr = 0
    window = set()

    for window_end in range(len(s)):
        while s[window_end] in window:
            window.remove(s[start])
            start += 1
        window.add(s[end])
        current_substr_len = (window_end - window_start) + 1
        longest_substr = max(longest_substr, current_substr_len)

    return longest_substr

res1 = longest_substr("abcabcbb")
print(res1)
res2 = longest_substr("abcbbbbbbcda")
print(res2)

