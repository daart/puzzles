def numRescueBoats(people, limit) -> int:
    people.sort()
    l, r = 0, len(people) - 1
    boats = 0

    while l <= r:
        rem = limit - people[r]

        if rem >= people[l]:
            l += 1
        
        boats += 1
        r -= 1
        
    return boats

t1 = numRescueBoats([1,2], 3)
t2 = numRescueBoats([3,2,2,1], 3)
t3 = numRescueBoats([3,5,3,4], 5)

print(t1)
print(t2)
print(t3)