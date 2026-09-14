# Test file for merge_two_sorted_lists.py

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linked_list(lst):
    """Convert a Python list to a linked list"""
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    """Convert a linked list to a Python list for easy comparison"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Import your solution
from merge_two_sorted_lists import merge_two_lists

# Test cases
def test_merge_two_lists():
    test_cases = [
        # Both lists empty
        ([], [], []),
        
        # One list empty
        ([], [0], [0]),
        ([1, 2, 3], [], [1, 2, 3]),
        
        # Basic cases
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        
        # Lists with negative values
        ([-3, -1, 0, 5], [-10, -5, 2, 7], [-10, -5, -3, -1, 0, 2, 5, 7]),
        
        # Lists with duplicate values
        ([1, 1, 2], [1, 3, 3], [1, 1, 1, 2, 3, 3]),
        
        # One list completely smaller than the other
        ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
    ]
    
    for i, (list1, list2, expected) in enumerate(test_cases):
        l1 = list_to_linked_list(list1)
        l2 = list_to_linked_list(list2)
        result = merge_two_lists(l1, l2)
        result_list = linked_list_to_list(result)
        
        assert result_list == expected, f"Test case {i+1} failed: expected {expected}, got {result_list}"
        print(f"Test case {i+1} passed!")

if __name__ == "__main__":
    test_merge_two_lists()
    print("All tests passed!")