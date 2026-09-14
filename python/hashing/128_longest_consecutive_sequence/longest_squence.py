"""
in order to achieve O(n) time we don't want to use sort, so we'll put a list of numbers in a set instead. That will remove duplicates
and will get ass O(1) access time to any number. Then we will iterate over each number in a set, and check if we are potentially in a 
sequence. How to achieve that? It's simple we just have to check if current_num - 1 (which is adjacent to the left) is NOT already in a set.

---[1, 2, 3, 4]----[100]----[200]

if 0, 99 or 199 are not in a set, those are potential sequence starters.

Within that condition, we have to initiate current_max_sequence_length, candidate which initializes as a current set value, and another loop with a condition that candidate is already in a set.
On each iteration of that inner loop, we increment candidate and current_sequence_length by one. After we've exited inner loop we should update
max_sequence_length which is a max of 2 possible values, current_sequence_length and max_sequence_length.

"""
def longest_seq(nums):
    hash_set = set(nums)
    max_sequence = 0
    
    for val in iter(hash_set):
        if val - 1 not in hash_set:
            current_sequence = 0
            candidate = val
            while candidate in hash_set:
                candidate += 1
                current_sequence += 1
            max_sequence = max(current_sequence, max_sequence)
    
    return max_sequence

t1 = longest_seq([100,4,200,1,3,2])
print(t1) # 4 1-4
t2 = longest_seq([0,3,7,2,5,8,4,6,0,1])
print(t2) # 9 0-8
t3 = longest_seq([1, 3, 5, 2, 4])
print(t3) # 5
t4 = longest_seq([1, 1, 2, 2, 3])
print(t4) # 3
t5 = longest_seq([1, 100, 200, 300])
print(t5) # 1
t6 = longest_seq([-1, 0, 1, 2, -2])
print(t6) # 5
