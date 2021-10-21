from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    max_val = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if node.left:
                if node.val == node.left.val:
                    left += 1
                else:
                    left = 0

            if node.right:
                if node.val == node.right.val:
                    right += 1
                else:
                    right = 0

            self.max_val = max(self.max_val, left + right)
            return max(left, right)

        dfs(root)
        return self.max_val
