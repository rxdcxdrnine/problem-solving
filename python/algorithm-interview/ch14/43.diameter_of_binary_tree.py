import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    longest = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left + right)
            return max(left, right) + 1

        dfs(root)
        return self.longest


if __name__ == "__main__":
    root = [1,2,3,4,None,None,5]
    root_node = TreeNode(root.pop(0))
    queue = collections.deque([root_node])
    values = collections.deque(root)

    while values:
        node = queue.popleft()
        node.left = TreeNode(values.popleft())
        node.right = TreeNode(values.popleft())

        if node.left.val:
            queue.append(node.left)
        if node.right.val:
            queue.append(node.right)

    solution = Solution()
    print(solution.diameterOfBinaryTree(root_node))

