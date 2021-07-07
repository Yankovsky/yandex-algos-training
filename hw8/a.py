# https://contest.yandex.ru/contest/28069/problems/A/

class BinarySearchTreeNode:
    def __init__(self, key, level, left=None, right=None):
        self.key = key
        self.level = level
        self.left = left
        self.right = right

    def __str__(self):
        return f'({self.key} l={self.left}, r={self.right})'


def tree_height(keys):
    max_level = 0
    root_node = None
    for key in keys:
        if not root_node:
            root_node = BinarySearchTreeNode(key, 1)
            max_level = 1
        else:
            current_node = root_node
            while True:
                if key == current_node.key:
                    break
                elif key < current_node.key:
                    if current_node.left:
                        current_node = current_node.left
                    else:
                        new_level = current_node.level + 1
                        current_node.left = BinarySearchTreeNode(key, current_node.level + 1)
                        if new_level > max_level:
                            max_level = new_level
                        break
                else:
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        new_level = current_node.level + 1
                        current_node.right = BinarySearchTreeNode(key, current_node.level + 1)
                        if new_level > max_level:
                            max_level = new_level
                        break

    return max_level


assert tree_height([7, 3, 2, 1, 9, 5, 4, 6, 8]) == 4
assert tree_height([7, 3, 2, 1, 9, 5, 7, 3, 2, 1, 5, 7, 2, 3, 1, 5, 4, 6, 8]) == 4


def main():
    keys = list(map(int, input().split()))[:-1]
    print(tree_height(keys))


if __name__ == '__main__':
    main()
