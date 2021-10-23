# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    flag = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        def dfs(node: Optional[TreeNode]):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if not abs(left - right) == 0 and not abs(left - right) == 1:
                self.flag = False

            return max(left, right) + 1

        dfs(root)
        return self.flag
