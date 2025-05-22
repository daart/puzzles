function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

const mergeTwoLists = (list1, list2) => {
  const dummyNode = new ListNode();
  let tail = dummyNode;

  while (list1 || list2) {
    if (list1.val <= list2.val) {
      tail.next = list1;
      list1 = list1.next;
    } else {
      tail.next = list2;
      list2 = list2.next;
    }
    tail = tail.next;

    if (list1) {
      tail.next = list1;
      break;
    }
    if (list2) {
      tail.next = list2;
      break;
    }
  }

  return dummyNode.next;
};
