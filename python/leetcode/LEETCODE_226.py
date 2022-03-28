import collections
from typing import Optional, List, Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:

    def dfs(node: Optional[TreeNode]):
        if not node:
            return

        dfs(node.left)
        dfs(node.right)

        node.left, node.right = node.right, node.left
        return

    dfs(root)
    return root
