from collections import defaultdict

def characterReplacement(s, k):
    l, longest_consecutive_chars, max_frequency = 0, 0, 0
    chars_map = defaultdict(int)

    for r in range(len(s)):
        if r in chars_map:
            chars_map[r] += 1
        else:
            chars_map[r] = 1

        window_len = r - l + 1
        max_frequency = max(chars_map.values())

        if window_len - max_frequency > k:
            chars_map[s[l]] -= 1
            l += 1
        longest_consecutive_chars = max(longest_consecutive_chars, r - l + 1)
        

    return longest_consecutive_chars