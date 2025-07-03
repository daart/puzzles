
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
