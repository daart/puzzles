arr1 = [7, 5, 1, 6, 13, 4, 2, 8]
   #     ||
        
#      [7, 5, 1, 6]   [13, 4, 2, 8]
#      [7, 5] [1, 6]  [13, 4] [2, 8]
#    [7] [5] [1] [6]  [13] [4] [2] [8]

#        /     \
#    [5, 7]   [1, 6]  [4, 13]  [2, 8]
#    [1, 5, 6, 7]     [2, 4, 8, 13]
#        [1, 2, 4, 5, 6, 7, 8, 13]
 


# ier 0 arr = [7, 5, 1, 6, 13, 4, 2, 8]

# iter 1 arr = [7, 5, 1, 6,]
# iter 2 arr = [7, 5]
# iter 3 arr = [7] 
# iter 4 arr = 
def merge_sort_dive(arr):

    if len(arr) > 1:

        left_half = arr[:len(arr) // 2]
        right_half = arr[len(arr) // 2:]


        merge_sort_dive(left_half)
        merge_sort_dive(right_half)


        l_position = 0
        r_position = 0
        resulting_arr_position = 0

        while l_position < len(left_half) and r_position < len(right_half):
            if left_half[l_position] < right_half[r_position]:
                arr[resulting_arr_position] = left_half[l_position]
                l_position += 1
            else:
                arr[resulting_arr_position] = right_half[r_position]
                r_position += 1
            
            resulting_arr_position += 1


        while l_position < len(left_half):
            arr[resulting_arr_position] = left_half[l_position]
            l_position += 1
            resulting_arr_position += 1

        while r_position < len(right_half):
            arr[resulting_arr_position] = right_half[r_position]
            r_position += 1
            resulting_arr_position += 1


    return arr



print(merge_sort_dive(arr1))