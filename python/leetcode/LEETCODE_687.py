import collections
from typing import Optional, List, Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Integer:
    def __init__(self, val = 0):
        self.val = val


def longestUnivaluePath(root: Optional[TreeNode]) -> int:
    longest: Integer = Integer(0)

    def dfs(node: Optional[TreeNode], upper: Optional[int]):
        if not node:
            return 0

        left: int = dfs(node.left, node.val)
        right: int = dfs(node.right, node.val)

        longest.val = max(longest.val, left + right)

        result: int = 0
        if upper == node.val:
            result += max(left, right) + 1

        return result

    dfs(root, None)
    return longest.val


if __name__ == "__main__":
    nums: List[int] = [4, 4, 4, 4, 4, 4]
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

    print(longestUnivaluePath(root))
