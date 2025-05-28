/**
Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
 */

// this is not optimal solution a recursive one but the first that came to my mind
// we use recursion to traverse deep into list untill we hit the base case
// a node points to null. In that case we return the node. The trick here is that
// during the bubble phase (when recursion goes up) we need to reassign pointers
// thx to closure we have a current node, so we reassign <current_node>.next.next = <current_node>
// and break the next pointer of the next <current_node>.next = null

// O(n) Time and O(n) Space
class ListNode {
  constructor(val, next) {
    this.val = null;
    this.next = null;
  }
}

const traverseList = (node) => {
  // base case
  if (!node || !node.next) {
    return node;
  }

  let newHead = traverseList(node.next);

  node.next.next = node;
  node.next = null;

  return newHead;
};

const reverseList = (listHead) => {
  return traverseList(listHead);
};
