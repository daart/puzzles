def isBalanced( root) -> bool:

    return getTreeHeight(root) != -1

def getTreeHeight( node):
    if not node:
        return 0
    left_subtree = getTreeHeight(node.left)

    if left_subtree == -1:
        return -1

    right_subtree = getTreeHeight(node.right)

    if right_subtree == -1:
        return - 1

    if abs(left_subtree - right_subtree) > 1:
        return -1

    return 1 + max(right_subtree, left_subtree)