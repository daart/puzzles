"""
main idea is a recursive solution. We break the problem into a smallest bit, which is a node, define the base case 
that is when either node or node.left or node.right is None, swap left and right nodes. We can perform swap operation
either on downward recursive trajectory or upward, that doesn't matter on the final outcome. I'll go with swapping 
on upward.

     3
    / \
   1   2

   invert(3) #1
    not base case so we call for both children
    invert(1) #2
        hit base case and return None
    invert(2) #3
        hit base case and return None
    node.right, node.left = node.left, node.right
    so we perform swapping here and return parent node which is (3) while children already swapped
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def invertTree(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: Optional[TreeNode]
    """
    if not (root or root.left or root.right):
        return None
    
    self.invertTree(root.left)
    self.invertTree(root.right)
    temp = root.left
    root.left = root.right
    root.right = temp

    return root

