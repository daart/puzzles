def longest_sub(text1, text2):
    """ create a 2D array + 1 row and + 1 cols not to hit out of bounds"""
    two_d_grid = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            """if chars match we set 1 (because we found a match and that is 1 length at least)
            + diagonal value"""
            if text2[j] == text1[i]:
                two_d_grid[i][j] = 1 + two_d_grid[i + 1][j + 1]
            else:
                """if chars do not match, look in either right or bottom adjacent position for max value"""
                two_d_grid[i][j] = max(two_d_grid[i + 1][j], two_d_grid[i][j + 1])

    return two_d_grid[0][0]