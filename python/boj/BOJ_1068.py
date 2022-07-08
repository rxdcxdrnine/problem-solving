from typing import List, Optional


class Node:
    def __init__(self, ind: int, parent: int):
        self.ind = ind
        self.parent = parent
        self.children: List[int] = []

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        children: List[str] = [str(child) for child in self.children]
        return "Node(ind=" + str(self.ind) \
               + ", parent=" + str(self.parent) \
               + ", children=[" + ", ".join(children) + "])"


class Integer:
    def __init__(self, val: int = 0):
        self.val = val


def solution(nums: List[int], delete: int):
    nodes: List[Node] = [Node(ind, parent) for ind, parent in enumerate(nums)]
    leafs = Integer()

    for node in nodes:
        if node.parent == -1:
            continue
        nodes[node.parent].add_child(node.ind)

    def dfs(parent: Optional[int], ind: int):
        if ind == delete:
            if parent is not None \
                    and len(nodes[parent].children) == 1:
                leafs.val += 1
            return

        if not nodes[ind].children:
            leafs.val += 1

        for child in nodes[ind].children:
            dfs(ind, child)
        return

    root: Optional[int] = None
    for node in nodes:
        if node.parent == -1:
            root = node.ind

    dfs(None, root)
    return leafs.val


if __name__ == "__main__":
    N: int = int(input())
    nums: List[int] = list(map(int, input().split()))
    delete: int = int(input())

    print(solution(nums, delete))
