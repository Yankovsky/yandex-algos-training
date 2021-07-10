# https://contest.yandex.ru/contest/28069/problems/D/

class BSTNode:
    def __init__(self, key=None, level=1):
        self.key = key
        self.level = level
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
            self.left = BSTNode(key=key, level=self.level + 1)
            return self.left

        if self.right:
            return self.right.insert_recursive(key)
        self.right = BSTNode(key=key, level=self.level + 1)
        return self.right


def traversal(keys):
    bst = BSTNode()
    for key in keys:
        bst.insert_recursive(key)

    def traverse(node):
        subtree_keys = []
        if node.left:
            subtree_keys += traverse(node.left)
        subtree_keys.append(node.key)
        if node.right:
            subtree_keys += traverse(node.right)
        return subtree_keys

    return traverse(bst)


assert traversal([7, 3, 2, 1, 9, 5, 4, 6, 8]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert traversal([7, 3, 3, 3, 2, 1, 9, 5, 4, 6, 8]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert traversal([9, 4, 2, 1]) == [1, 2, 4, 9]
assert traversal([1, 6, 8, 2]) == [1, 2, 6, 8]
assert traversal([1, 7]) == [1, 7]
assert traversal([7, 1]) == [1, 7]
assert traversal([3, 1, 2]) == [1, 2, 3]
assert traversal([3, 1, 2, 0]) == [0, 1, 2, 3]
assert traversal([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
assert traversal([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
assert traversal([4, 2, 4, 6, 2, 4, 1, 6, 2, 4, 3, 1, 6, 2, 4, 5, 3, 1, 6, 2, 4, 7, 5, 3, 1, 6, 2, 4]) == \
       [1, 2, 3, 4, 5, 6, 7]


def main():
    keys = list(map(int, input().split()))[:-1]
    for key in traversal(keys):
        print(key)


if __name__ == '__main__':
    main()
