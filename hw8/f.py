# https://contest.yandex.ru/contest/28069/problems/D/

class BSTNode:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None

    def insert_recursive(self, key):
        if self.key is None:
            self.key = key
            return self

        if key == self.key:
            return self

        if key < self.key:
            if self.left:
                return self.left.insert_recursive(key)
            self.left = BSTNode(key)
            return self.left

        if self.right:
            return self.right.insert_recursive(key)
        self.right = BSTNode(key)
        return self.right

    def traverse(self, func):
        if self.left:
            self.left.traverse(func)
        func(self)
        if self.right:
            self.right.traverse(func)


def nodes_with_two_children(keys):
    bst = BSTNode()
    for key in keys:
        bst.insert_recursive(key)

    results = []

    def append_node_with_two_children(node):
        if node.left and node.right:
            results.append(node.key)

    bst.traverse(append_node_with_two_children)
    return results


assert nodes_with_two_children([7, 3, 2, 1, 9, 5, 4, 6, 8]) == [3, 5, 7]
assert nodes_with_two_children([7, 3, 3, 3, 2, 1, 9, 5, 4, 6, 8]) == [3, 5, 7]
assert nodes_with_two_children([9, 4, 2, 1]) == []
assert nodes_with_two_children([1, 6, 8, 2]) == [6]
assert nodes_with_two_children([1, 7]) == []
assert nodes_with_two_children([7, 1]) == []
assert nodes_with_two_children([3, 1, 2]) == []
assert nodes_with_two_children([3, 1, 2, 0]) == [1]
assert nodes_with_two_children([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == []
assert nodes_with_two_children([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == []
assert nodes_with_two_children([4, 2, 4, 6, 2, 4, 1, 6, 2, 4, 3, 1, 6, 2, 4, 5, 3, 1, 6, 2, 4, 7, 5, 3, 1, 6, 2, 4]) == \
       [2, 4, 6]


def main():
    keys = list(map(int, input().split()))[:-1]
    for key in nodes_with_two_children(keys):
        print(key)


if __name__ == '__main__':
    main()
