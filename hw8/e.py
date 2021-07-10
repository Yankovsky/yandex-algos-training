# https://contest.yandex.ru/contest/28069/problems/E/

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

    def __iter__(self):
        if self.left:
            for node in self.left:
                yield node
        yield self
        if self.right:
            for node in self.right:
                yield node


def leaves(keys):
    bst = BSTNode()
    for key in keys:
        bst.insert_recursive(key)

    results = []

    for node in bst:
        if not node.left and not node.right:
            results.append(node.key)

    return results


assert leaves([7, 3, 2, 1, 9, 5, 4, 6, 8]) == [1, 4, 6, 8]
assert leaves([7, 3, 3, 3, 2, 1, 9, 5, 4, 6, 8]) == [1, 4, 6, 8]
assert leaves([9, 4, 2, 1]) == [1]
assert leaves([1, 6, 8, 2]) == [2, 8]
assert leaves([1, 7]) == [7]
assert leaves([7, 1]) == [1]
assert leaves([3, 1, 2]) == [2]
assert leaves([3, 1, 2, 0]) == [0, 2]
assert leaves([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == [-5]
assert leaves([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == [5]
assert leaves([4, 2, 4, 6, 2, 4, 1, 6, 2, 4, 3, 1, 6, 2, 4, 5, 3, 1, 6, 2, 4, 7, 5, 3, 1, 6, 2, 4]) == \
       [1, 3, 5, 7]


def main():
    keys = list(map(int, input().split()))[:-1]
    for key in leaves(keys):
        print(key)


if __name__ == '__main__':
    main()
