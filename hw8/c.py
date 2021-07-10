# https://contest.yandex.ru/contest/28069/problems/C/

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


def second_max(keys):
    bst = BSTNode()
    for key in keys:
        bst.insert_recursive(key)

    def find_second_max(node, previous_node=None, went_left_once=False):
        if node.right:
            return find_second_max(node.right, node, went_left_once)
        if node.left and not went_left_once:
            return find_second_max(node.left, node, True)
        return node.key if went_left_once else previous_node.key

    return find_second_max(bst)


assert second_max([7, 3, 2, 1, 9, 5, 4, 6, 8]) == 8
assert second_max([7, 3, 3, 3, 2, 1, 9, 5, 4, 6, 8]) == 8
assert second_max([9, 4, 2, 1]) == 4
assert second_max([1, 6, 8, 2]) == 6
assert second_max([1, 7]) == 1
assert second_max([7, 1]) == 1
assert second_max([3, 1, 2]) == 2
assert second_max([3, 1, 2, 0]) == 2
assert second_max([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == 4
assert second_max([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == 4
assert second_max([4, 2, 4, 6, 2, 4, 1, 6, 2, 4, 3, 1, 6, 2, 4, 5, 3, 1, 6, 2, 4, 7, 5, 3, 1, 6, 2, 4]) == 6


def main():
    keys = list(map(int, input().split()))[:-1]
    print(second_max(keys))


if __name__ == '__main__':
    main()
