"""
The idea is similar to 141 linked list cycle. We use tortoise and a hair technique here as well. The idea is we will
have fast and slow pointers. Slow will move one node next at a time, fast will move two nodes at a time. When fast node
reaches tail, slow one will be exactly in the middle. In order to handle even / odd linked list we just need a proper
loop condition. while fast and fast.next will cover both. For even cases 1 -> 2 -> 3 -> 4 fast will be none on 3d iteration
while slow will be on position 3. And for odd 1 -> 2 -> 3 -> 4 -> 5 
fast.next on 3d iteration will be none, so slow on pos 3 will be returned as a middle.
"""

def middle_of_the_linked_lis(head):
    fast = head
    slow = head

    while not fast and not fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow