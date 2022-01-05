import sys
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    val = sys.maxsize
    prev = -sys.maxsize

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root:
            self.minDiffInBST(root.left)
            self.val = min(self.val, root.val - self.prev)
            self.prev = root.val
            self.minDiffInBST(root.right)

        return self.val
        