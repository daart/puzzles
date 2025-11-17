"""
we have to keep track of frequency of occurence of all the characters in the short string
"""
def matches(a1, a2):
    for k in range(26):
        if a1[k] != a2[k]:
            return False
    return True

def find_permutated_sequence1(s1, s2):

    if len(s1) > len(s2):
        return False
    
    s1_arr = [0] * 26
    s2_arr = [0] * 26

    for i in range(len(s1)):
        s1_arr[ord(s1[i]) - ord('a')] += 1
        s2_arr[ord(s2[i]) - ord('a')] += 1
    
    if matches(s1_arr, s2_arr):
            return True
    
    for j in range(len(s2) - len(s1)):
        s2_arr[ord(s2[(j + len(s1))]) - ord('a')] += 1
        s2_arr[ord(s2[j]) - ord('a')] -= 1

        if matches(s1_arr, s2_arr):
            return True

    return False


def optimal_solution(s1, s2):
    if len(s1) > len(s2):
        return False
    
    s1_arr = [0] * 26
    s2_arr = [0] * 26

    for i in range(len(s1)):
        s1_arr[ord(s1[i]) - ord('a')] += 1
        s2_arr[ord(s2[i]) - ord('a')] += 1
    
    matches = 0

    for c in range(26):
        if s1_arr[c] == s2_arr[c]:
            matches += 1

    for j in range(len(s2) - len(s1)):
        if matches == 26:
            return True
        sliding_window_right_frame_position = ord(s2[j + len(s1)]) - ord('a')
        sliding_window_left_frame_position = ord(s2[j]) - ord('a')

        s2_arr[sliding_window_right_frame_position] += 1

        if s2_arr[sliding_window_right_frame_position] == s1_arr[sliding_window_right_frame_position]:
            matches += 1
        elif s1_arr[sliding_window_right_frame_position] + 1 == s2_arr[sliding_window_right_frame_position]:
            matches -=1
        
        s2_arr[sliding_window_left_frame_position] -= 1
        if s1_arr[sliding_window_left_frame_position] == s2_arr[sliding_window_left_frame_position]:
            matches += 1
        elif s1_arr[sliding_window_left_frame_position] - 1 == s2_arr[sliding_window_left_frame_position]:
            matches -=1

    return matches == 26