# https://contest.yandex.ru/contest/28069/problems/A/
# Ниже представлено три способа добавления нового элемента в дерево, все рабочие:
# insert_recursive – рекурсивная вставка с вызовом функцией самой себя
# insert_with_loop – цикл вместо рекурсии
# insert_with_loop_optimized – цикл вместо рекурсии с сохранением родителя на каждой итерации
# Первый способ самый простой для понимания, третий самый быстрый.

# BST = Binary Search Tree
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

    # Используем цикл вместо рекурсии
    def insert_with_loop(self, key):
        if self.key is None:
            self.key = key
            return self

        current_node = self
        while True:
            if key == current_node.key:
                return current_node
            if key < current_node.key:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = BSTNode(key=key, level=current_node.level + 1)
                    return current_node.left
            else:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = BSTNode(key=key, level=current_node.level + 1)
                    return current_node.right

    # Используем цикл вместо рекурсии и храним родителя на каждом шаге итерации
    def insert_with_loop_optimized(self, key):
        if self.key is None:
            self.key = key
            return self

        current_node = self
        previous_node = None
        while current_node is not None:
            if key == current_node.key:
                return current_node

            previous_node = current_node
            if key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right

        new_node = BSTNode(key=key, level=previous_node.level + 1)

        if key < previous_node.key:
            previous_node.left = new_node
        else:
            previous_node.right = new_node
        return new_node

    def __iter__(self):
        if self.left:
            for node in self.left:
                yield node
        yield self
        if self.right:
            for node in self.right:
                yield node

    def __str__(self):
        return f'({self.key} l={self.left}, r={self.right})'


def tree_height(keys):
    bst = BSTNode()
    max_level = 0
    for key in keys:
        new_node = bst.insert_with_loop_optimized(key)
        if new_node.level > max_level:
            max_level = new_node.level

    return max_level


assert tree_height([7, 3, 2, 1, 9, 5, 4, 6, 8]) == 4
assert tree_height([7, 3, 3, 3, 2, 1, 9, 5, 4, 6, 8]) == 4
assert tree_height([9, 4, 2, 1]) == 4
assert tree_height([1, 6, 8, 2]) == 3
assert tree_height([1, 7]) == 2
assert tree_height([7, 1]) == 2
assert tree_height([3, 1, 2]) == 3
assert tree_height([3, 1, 2, 0]) == 3
assert tree_height([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == 11
assert tree_height([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == 11
assert tree_height([4, 2, 4, 6, 2, 4, 1, 6, 2, 4, 3, 1, 6, 2, 4, 5, 3, 1, 6, 2, 4, 7, 5, 3, 1, 6, 2, 4]) == 3
assert tree_height([7, 3, 2, 1, 9, 5, 7, 3, 2, 1, 5, 7, 2, 3, 1, 5, 4, 6, 8]) == 4


def main():
    keys = list(map(int, input().split()))[:-1]
    print(tree_height(keys))


if __name__ == '__main__':
    main()
