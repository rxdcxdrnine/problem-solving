import collections
import sys
from typing import Optional, List, Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Integer:
    def __init__(self, val=0):
        self.val = val


def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:

    longest: Integer = Integer(0)

    def dfs(node: Optional[TreeNode]):
        if not node:
            return -1

        left: int = dfs(node.left)
        right: int = dfs(node.right)

        longest.val = max(longest.val, left + right + 2)
        return max(left, right) + 1

    dfs(root)
    return longest.val


if __name__ == "__main__":
    nums: List[int] = [1, 2]
    vals: Deque[int] = collections.deque(nums)

    root: TreeNode = TreeNode(vals.popleft())
    nodes: Deque[TreeNode] = collections.deque([root])

    while vals:
        node: TreeNode = nodes.popleft()
        if vals:
            node.left = TreeNode(vals.popleft())
        if vals:
            node.right = TreeNode(vals.popleft())

        nodes.append(node.left)
        nodes.append(node.right)

    print(diameterOfBinaryTree(root))
