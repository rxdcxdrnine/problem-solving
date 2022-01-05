# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''

        result = []
        queue = collections.deque([root])

        while queue:
            now = queue.popleft()
            if now:
                result.append(str(now.val))
                queue.append(now.left)
                queue.append(now.right)
            else:
                result.append("null")

        return " ".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []

        values = collections.deque(data.split(" "))
        root = TreeNode(values.popleft())
        queue = collections.deque([root])

        while values:
            now = queue.popleft()

            if values:
                now.left = TreeNode(values.popleft())
                queue.append(now.left)
            if values:
                now.right = TreeNode(values.popleft())
                queue.append(now.right)

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))