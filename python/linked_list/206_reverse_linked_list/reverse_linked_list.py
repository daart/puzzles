"""
Ok so the main idea is to use iterative approach which the most efficient, utilize two pointers and a temporary variable for swap operation. We will initialize 2 pointers, current will be the head of our linked list, which is 1->2->3->4, and previous that will be None, an empty value. We will traverse through the head (or input linkedList) until current pointer is truthy. 
On each iteration we will have temp variable in order not to loose reference to our current's node next. We will also reassign current nodes next pointer to point to previous node to reverse list in opposite direction. Then we will update the previous node to be a current node (move one node forward) and lastly update current node (which now basically becomes detached from the reversed linked list) to be that temp stored node.

Space complexity: O(n) and Time complexity O(1)
"""

def reverse_list(node):
    current, prev = node, None

    while current:
        place_holder = current.next
        current.next = prev
        prev = current
        current = place_holder

    return prev