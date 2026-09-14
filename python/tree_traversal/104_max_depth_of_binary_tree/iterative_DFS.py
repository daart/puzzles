def iterative_DFS(root):
    stack = [[root, 1]]
    res = 0

    while stack:
        node, depth = stack.pop()

        if node:
            res = max(depth, res)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])

    return res