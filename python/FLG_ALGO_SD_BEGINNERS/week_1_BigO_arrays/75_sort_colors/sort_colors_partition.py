"""
Sort the list in place using three pointers:
- l: the next position where a 0 belongs.
- i: the current element to examine.
- r: the next position where a 2 belongs.

Throughout the loop:
- Elements before l are all 0s.
- Elements from l up to, but not including, i are all 1s.
- Elements from i through r are still unchecked.
- Elements after r are all 2s.

While i <= r:
- If cols[i] == 0, swap it with cols[l], then increment l and i.
  Advancing i is safe: either we swapped the element with itself,
  or the element moved from l was an already-checked 1.
- If cols[i] == 2, swap it with cols[r], then decrement r.
  Keep i unchanged because the incoming element still needs checking.
- Otherwise, the element is 1, so increment i.

When i > r, no unchecked elements remain and the list is sorted.
Time: O(n). Extra space: O(1).

"""
def sort_colors(cols):
    l = i = 0
    r = len(cols) - 1

    def swap(prev_position, next_position):
        cols[prev_position], cols[next_position] = cols[next_position], cols[prev_position]

    while i <= r:
        if cols[i] == 0:
            swap(i, l)
            l += 1
            i += 1
        elif cols[i] == 2:
            swap(i, r)
            r -= 1
        else:
            i += 1

    return cols

res1 = sort_colors([0, 1, 0, 2, 2, 1])

print(res1)

res2 = sort_colors([2,0,2,1,1,0])
print(res2)

res3 = sort_colors([2,0,1])
print(res3)


