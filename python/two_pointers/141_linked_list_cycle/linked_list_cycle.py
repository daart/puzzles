"""
the main idea is we will have a fast and slow pointers that will traverse a linked list simultaniously.
Slow one will go one by one using next on each iteration, on contrast fast one will go twice faster using currentNode.next.next.
If the list is cycled, they will eventually cross and we return True, if not False.

"""
def has_cycle(head):
    slow = head
    fast = head

    if not (head or fast or slow):
        return False
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True 
    
    return False

