# leetcode 687

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_tree(data, index):
    node = None
    if index < len(data):
        if not data[index]:
            return None
        else:
            node = TreeNode(data[index])
            node.left = create_tree(data, 2 * index + 1)
            node.right = create_tree(data, 2 * index + 2)
    return node


class Solution:
    longest = 0

    def longestUnivaluePath_A(self, root):

        def dfs(node):
            if not node:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left + right + 2)
            return max(left, right) + 1

        dfs(root)
        return self.longest
