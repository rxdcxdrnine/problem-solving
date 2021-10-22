from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if root1 is None and root2 is None:
            return None

        def dfs(root, root1, root2):

            if root1 is not None and root2 is None:
                root.val = root1.val
                root.left = root1.left
                root.right = root1.right
            elif root1 is None and root2 is not None:
                root.val = root2.val
                root.left = root2.left
                root.right = root2.right
            else:
                root.val = root1.val + root2.val

                if root1.left is not None or root2.left is not None:
                    root.left = TreeNode()
                    dfs(root.left, root1.left, root2.left)

                if root1.right is not None or root2.right is not None:
                    root.right = TreeNode()
                    dfs(root.right, root1.right, root2.right)

        root = TreeNode(0)
        dfs(root, root1, root2)

        return root
