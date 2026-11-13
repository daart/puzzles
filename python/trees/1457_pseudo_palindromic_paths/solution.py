# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode | None) -> int:
        palindromic_counter = 0
        freq_map = {}

        def is_pailndromic(map):
            odd_counter = 0

            for f in map.values():
                if f % 2 != 0:
                    odd_counter += 1
                
            return odd_counter <= 1
        
        def dfs(node, freq):
            nonlocal palindromic_counter
            
            if not node:
                return
            # we've entered the path
            freq_map[node.val] = freq_map.get(node.val, 0) + 1

            if not node.left and not node.right:
                # check if current path is pseudo-palidnromic
                if is_pailndromic(freq_map):
                    palindromic_counter += 1
            else:

                dfs(node.left, freq)
                dfs(node.right, freq)

            # remove the node from the current path
            freq[node.val] -= 1


        dfs(root, freq_map)
        return palindromic_counter


    def solution_with_dfs_and_bitmask(self, root: TreeNode | None) -> int:
        def dfs(node, mask: int):
            if not node:
                return 0
            mask ^= (1 << node.val)

            if not node.left and not node.right:
                return 1 if mask & (mask -1) == 0 else 0

            return dfs(node.left, mask) + dfs(node.right, mask)

        return dfs(root, 0)

    def soltion_with_stack_and_mask(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        stack = [(root, 0)]
        counter = 0

        while len(stack) > 0:
            node, bit_mask_val = stack.pop()

            bit_mask_val ^= (1 << node.val)

            if not node.left and not node.right and bit_mask_val & (bit_mask_val - 1) == 0:
                counter += 1

            else:
                if node.left:
                    stack.append((node.left, bit_mask_val))
                if node.right:
                    stack.append((node.right, bit_mask_val))

        return counter