import collections
from typing import Optional, List, Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mergeTrees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

    def dfs(node: TreeNode, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> None:
        if not node:
            return

        left: int = 0
        left += node1.left.val if node1 and node1.left else 0
        left += node2.left.val if node2 and node2.left else 0

        right: int = 0
        right += node1.right.val if node1 and node1.right else 0
        right += node2.right.val if node2 and node2.right else 0

        if (node1 and node1.left) or (node2 and node2.left):
            node.left = TreeNode(left)
        if (node1 and node1.right) or (node2 and node2.right):
            node.right = TreeNode(right)

        dfs(node.left, node1.left if node1 else None, node2.left if node2 else None)
        dfs(node.right, node1.right if node1 else None, node2.right if node2 else None)
        return

    val: int = 0
    val += root1.val if root1 else 0
    val += root2.val if root2 else 0

    if root1 or root2:
        root = TreeNode(val)
        dfs(root, root1, root2)
        return root

    return None
