# https://contest.yandex.ru/contest/28069/problems/B/

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
            return None

        if key < self.key:
            if self.left:
                return self.left.insert_recursive(key)
            self.left = BSTNode(key=key, level=self.level + 1)
            return self.left

        if self.right:
            return self.right.insert_recursive(key)
        self.right = BSTNode(key=key, level=self.level + 1)
        return self.right


def nodes_levels(keys):
    bst = BSTNode()
    results = []
    for key in keys:
        new_node = bst.insert_recursive(key)
        if new_node:
            results.append(new_node.level)

    return results


assert nodes_levels([7, 3, 2, 1, 9, 5, 4, 6, 8]) == [1, 2, 3, 4, 2, 3, 4, 4, 3]
assert nodes_levels([7, 3, 3, 3, 2, 1, 9, 5, 4, 6, 8]) == [1, 2, 3, 4, 2, 3, 4, 4, 3]
assert nodes_levels([9, 4, 2, 1]) == [1, 2, 3, 4]
assert nodes_levels([1, 6, 8, 2]) == [1, 2, 3, 3]
assert nodes_levels([1, 7]) == [1, 2]
assert nodes_levels([7, 1]) == [1, 2]
assert nodes_levels([3, 1, 2]) == [1, 2, 3]
assert nodes_levels([3, 1, 2, 0]) == [1, 2, 3, 3]
assert nodes_levels([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
assert nodes_levels([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
assert nodes_levels([4, 2, 4, 6, 2, 4, 1, 6, 2, 4, 3, 1, 6, 2, 4, 5, 3, 1, 6, 2, 4, 7, 5, 3, 1, 6, 2, 4]) == \
       [1, 2, 2, 3, 3, 3, 3]


def main():
    keys = list(map(int, input().split()))[:-1]
    print(*nodes_levels(keys))


if __name__ == '__main__':
    main()
