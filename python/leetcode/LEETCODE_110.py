from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Boolean:
    def __init__(self, val=False):
        self.val = val


def isBalanced(root: Optional[TreeNode]) -> bool:
    balanced: Boolean = Boolean(True)

    def dfs(node: Optional[TreeNode]):
        if not node:
            return 0

        left: int = dfs(node.left)
        right: int = dfs(node.right)

        if abs(left - right) > 1:
            balanced.val = False

        return max(left, right) + 1

    dfs(root)
    return balanced.val
