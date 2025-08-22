def minDistance(word1, word2):
    cache = {}

    def recursive_check(pos1, pos2):
        cache_key = (pos1, pos2)
        
        if cache_key in cache:
            return cache[cache_key]
        
        # Base cases
        if pos1 == len(word1):
            return len(word2) - pos2
        if pos2 == len(word2):
            return len(word1) - pos1
        
        # If characters match, no operation needed
        if word1[pos1] == word2[pos2]:
            return recursive_check(pos1 + 1, pos2 + 1)
        
        # Consider all three operations
        insert = 1 + recursive_check(pos1, pos2 + 1)  # Insert word2[pos2] into word1 at pos1
        remove = 1 + recursive_check(pos1 + 1, pos2)  # Remove word1[pos1] from word1
        replace = 1 + recursive_check(pos1 + 1, pos2 + 1)  # Replace word1[pos1] with word2[pos2]
        
        # Take the minimum of all operations
        temp = min(insert, remove, replace)
        
        cache[cache_key] = temp
        return temp
    
    return recursive_check(0, 0)

t1 = distance('horse', 'ros')
print(t1)
