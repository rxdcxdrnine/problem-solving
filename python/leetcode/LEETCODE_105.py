import collections
from typing import List, Optional, Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not inorder:
        return

    index: int = inorder.index(preorder.pop(0))

    node: TreeNode = TreeNode(inorder[index])
    node.left = buildTree(preorder, inorder[:index])
    node.right = buildTree(preorder, inorder[index + 1:])

    return node


if __name__ == "__main__":
    preorder: List[int] = [3, 9, 20, 15, 7]
    inorder: List[int] = [9, 3, 15, 20, 7]

    buildTree(preorder, inorder)
