""" 707 
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3

Constraints:

0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        if not self.head:
            return "Empty"
        values = []
        current = self.head
        while current:
            values.append(str(current.val))
            current = current.next
        return "->".join(values)
    
    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        currentHead = self.head
        for i in range(index):
            currentHead = currentHead.next
        # return currentHead.val

        return print(currentHead.val)

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        newNode = ListNode(val);
        newNode.next = self.head
        self.head = newNode
        self.size += 1
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        newNode = ListNode(val);
        if not self.head:
            self.head = newNode
        else:
            currentHead = self.head

            while currentHead.next:
                currentHead = currentHead.next
            
            currentHead.next = newNode
        self.size += 1
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """

        if index < 0 or index > self.size:
            return None
        if index == self.size:
            return self.addAtTail(val)
        if index == 0:
            return self.addAtHead(val)
        
        newNode = ListNode(val)
        currentNode = self.head;

        for i in range(index - 1):
            currentNode = currentNode.next
        newNode.next = currentNode.next
        currentNode.next = newNode
        self.size += 1
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return None
        #delete first
        if index == 0:
            # if singe node in the list
            if not self.head.next:
                self.head = None
            else:
                self.head = self.head.next
        else:
            prevNode = self.head
            currentNode = prevNode.next;

            for i in range(1, index):
                if not currentNode:
                    return None
                prevNode = currentNode
                currentNode = currentNode.next

            if not currentNode:
                return None
            
            prevNode.next = currentNode.next
                
        self.size -= 1
    



emptyLinkedList = MyLinkedList()
emptyLinkedList.addAtHead(7)
emptyLinkedList.addAtHead(2)
emptyLinkedList.addAtHead(1)
print(emptyLinkedList)  # 1
emptyLinkedList.addAtIndex(3, 0)  # 1->2
print(emptyLinkedList)
emptyLinkedList.deleteAtIndex(2)  # 1->2
print(emptyLinkedList)
emptyLinkedList.addAtHead(6)
print(emptyLinkedList)
emptyLinkedList.addAtTail(4)
print(emptyLinkedList)
print(emptyLinkedList.get(4))  # 3

# emptyLinkedList.addAtIndex(1, 3)  # 1->3->2
# print(emptyLinkedList.get(1))  # 3
# emptyLinkedList.deleteAtIndex(1)  # 1->2
# print(emptyLinkedList)
# print(emptyLinkedList.get(1))  # 2