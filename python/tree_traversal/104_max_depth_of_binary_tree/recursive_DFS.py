"""
naturally recursive solution comes to mind instantly. We will always have 
a root node that is depth 1, but we can't now which branch is deeper left or right
unless we traverse down to it's leaves. So the idea is that we will return 0 as a base case
meaning that we've reached the leaves, in other scenario we are returning 1[as root node] + 
math max of either left node or right node.    
"""

def recursive_dfs(root):
    if not root:
        return 0
    
    return 1 + max(recursive_dfs(root.left), recursive_dfs(root.right))