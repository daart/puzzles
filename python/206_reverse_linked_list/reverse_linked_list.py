"""
The main idea is in two pointers pattern. So we will have previous and current node pointers and also a temp
variable for swap operation. At first previous will point to None and current to head. Traverse
the list until current is None and on every step we will reassign current node's next to point to
previous node, update previous node to point to current node and lastly reassign current node to point
to temp variable. In the end we return a new head which is a previous node.

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