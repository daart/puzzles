""" 
#21 Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

"""

"""
Main Idea:
1) Create a dummy node that will be a starting point of a resulting linked list
2) Traverse through both input linked lists until at least one of them points to None
3) On every step compare current node of both lists to find the smaller one and put it to dummy.next
4) Check if there are any remaining nodes in one of the input lists. If yes, just put the remaining list to dummy.next
5) return dummy.next
"""
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1, list2):
    dummyNode = ListNode()
    tail = dummyNode

    while (list1 and list2):
        if (list1.val < list2.val):
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    if list1:
        tail.next = list1

    if list2:
        tail.next = list2

    return dummyNode.next

    
