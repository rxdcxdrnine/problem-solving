# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    max_depth = 0
    stack = [[root_node, 0]]    # [node, depth]
    while stack:
        now = stack.pop()

        depth = now[1] + 1
        if max_depth < depth:
            max_depth = depth

        if now[0].left:
            stack.append([now[0].left, depth])
        if now[0].right:
            stack.append([now[0].right, depth])

    return max_depth


if __name__ == "__main__":
    root = [3, 9, 20, None, None, 15, 7]

    root_node = TreeNode(root.pop(0))
    queue = collections.deque([root_node])
    values = collections.deque(root)

    while values:
        node = queue.popleft()
        node.left = TreeNode(values.popleft())
        node.right = TreeNode(values.popleft())

        queue.append(node.left)
        queue.append(node.right)

    print(maxDepth(root_node))
