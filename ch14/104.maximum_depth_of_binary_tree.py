# leetcode 104

import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth_A(root):
    if root is None:
        return 0

    queue = collections.deque([root])
    depth = 0

    while queue:
        depth += 1
        for _ in range(len(queue)):
            cur_root = queue.popleft()
            if cur_root.left:
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)

    return depth


if __name__ == "__main__":
    val_list = [3, 9, 20, None, None, 15, 7]
    node_list = []

    node_list.append(TreeNode(val_list[0]))
    ind = left_ind = right_ind = 0

    while True:
        left_ind = 2 * ind + 1
        right_ind = 2 * ind + 2

        if val_list[left_ind]:
            node_list[ind].left = TreeNode(val_list[left_ind])
            node_list.append(node_list[ind].left)
        if val_list[right_ind]:
            node_list[ind].right = TreeNode(val_list[right_ind])
            node_list.append(node_list[ind].right)

        ind += 1

        if 2 * ind + 3 > len(val_list):
            break

    root = node_list[0]
    print(maxDepth_A(root))