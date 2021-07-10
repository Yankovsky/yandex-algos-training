# https://contest.yandex.ru/contest/28069/problems/H/

class BSTNode:
    def __init__(self, key=None):
        self.key = key
        self.left_subtree_depth = 0
        self.right_subtree_depth = 0
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
                result = self.left.insert_recursive(key)
                self.left_subtree_depth = max(self.left.left_subtree_depth, self.left.right_subtree_depth) + 1
                return result
            self.left_subtree_depth = 1
            self.left = BSTNode(key)
            return self.left

        if self.right:
            result = self.right.insert_recursive(key)
            self.right_subtree_depth = max(self.right.left_subtree_depth, self.right.right_subtree_depth) + 1
            return result
        self.right_subtree_depth = 1
        self.right = BSTNode(key)
        return self.right

    def __iter__(self):
        if self.left:
            for node in self.left:
                yield node
        yield self
        if self.right:
            for node in self.right:
                yield node


def is_avl_tree(keys):
    bst = BSTNode()
    for key in keys:
        bst.insert_recursive(key)

    is_avl = True

    for node in bst:
        is_avl = is_avl and (abs(node.left_subtree_depth - node.right_subtree_depth) <= 1)

    return 'YES' if is_avl else 'NO'


assert is_avl_tree([7, 3, 2, 1, 9, 5, 4, 6, 8]) == 'YES'
assert is_avl_tree([7, 3, 3, 3, 2, 1, 9, 5, 4, 6, 8]) == 'YES'
assert is_avl_tree([9, 4, 2, 1]) == 'NO'
assert is_avl_tree([1, 6, 8, 2]) == 'NO'
assert is_avl_tree([1, 7]) == 'YES'
assert is_avl_tree([7, 1]) == 'YES'
assert is_avl_tree([3, 1, 2]) == 'NO'
assert is_avl_tree([3, 1, 2, 0]) == 'NO'
assert is_avl_tree([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == 'NO'
assert is_avl_tree([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == 'NO'
assert is_avl_tree([4, 2, 4, 6, 2, 4, 1, 6, 2, 4, 3, 1, 6, 2, 4, 5, 3, 1, 6, 2, 4, 7, 5, 3, 1, 6, 2, 4]) == 'YES'
assert is_avl_tree([3, 2, 1, 0, 4, 5, 6]) == 'NO'
assert is_avl_tree([6, 2, 1, 8]) == 'YES'


def main():
    keys = list(map(int, input().split()))[:-1]
    print(is_avl_tree(keys))


if __name__ == '__main__':
    main()
