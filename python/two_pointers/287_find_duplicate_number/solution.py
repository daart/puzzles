def findDuplicate(nums):
    turtle, hare = 0, 0

    while True:
        turtle = nums[turtle]
        hare = nums[nums[hare]]
        if turtle == hare:
            break
    
    turtle = 0

    while turtle != hare:
        turtle = nums[turtle]
        hare = nums[hare]

        if turtle == hare:
            return turtle
        

t1 = findDuplicate([1,3,4,2,2])
t2 = findDuplicate([3,1,3,4,2])
t3 = findDuplicate([3, 3, 3, 3, 3])

print(t1);
print(t2);
print(t3);