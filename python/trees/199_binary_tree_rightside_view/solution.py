def get_rightside_view(root):
    res = []

    def dfs(node, depth):
        if not node:
            return

        if depth == len(res):
            res.append(node.val)

        dfs(node.right, depth + 1)
        dfs(node.left, depth + 1)

    dfs(root, 0)
    return res