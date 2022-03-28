import collections
from typing import Optional, List, Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:

    def dfs(node: Optional[TreeNode]):
        if not node:
            return 0

        left: int = dfs(node.left)
        right: int = dfs(node.right)

        return max(left, right) + 1

    return dfs(root)


if __name__ == "__main__":
    nums: List[int] = [3, 9, 20, None, None, 15, 7]
    vals: Deque[int] = collections.deque(nums)

    root: TreeNode = TreeNode(vals.popleft())
    nodes: Deque[TreeNode] = collections.deque([root])

    while vals:
        node: TreeNode = nodes.popleft()
        node.left = TreeNode(vals.popleft())
        node.right = TreeNode(vals.popleft())

        nodes.append(node.left)
        nodes.append(node.right)

    print(maxDepth(root))
