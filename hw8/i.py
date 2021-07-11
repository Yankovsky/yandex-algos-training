# https://contest.yandex.ru/contest/28069/problems/I/
import sys

sys.setrecursionlimit(100000)


class GenealogicalTreeNode:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.descendants = 0

    def update_descendants(self, increment):
        self.descendants += increment
        if self.parent:
            self.parent.update_descendants(increment)


def descendants_count(descendant_parent_pairs):
    nodes = {}
    for (descendant, parent) in descendant_parent_pairs:
        if parent not in nodes:
            nodes[parent] = GenealogicalTreeNode(parent)
        if descendant not in nodes:
            nodes[descendant] = GenealogicalTreeNode(descendant)

        nodes[descendant].parent = nodes[parent]
        nodes[parent].update_descendants(nodes[descendant].descendants + 1)

    return sorted((name, node.descendants) for name, node in nodes.items())


assert descendants_count([
    ('Alexei', 'Peter_I'),
    ('Anna', 'Peter_I'),
    ('Elizabeth', 'Peter_I'),
    ('Peter_II', 'Alexei'),
    ('Peter_III', 'Anna'),
    ('Paul_I', 'Peter_III'),
    ('Alexander_I', 'Paul_I'),
    ('Nicholaus_I', 'Paul_I'),
]) == [
    ('Alexander_I', 0),
    ('Alexei', 1),
    ('Anna', 4),
    ('Elizabeth', 0),
    ('Nicholaus_I', 0),
    ('Paul_I', 2),
    ('Peter_I', 8),
    ('Peter_II', 0),
    ('Peter_III', 3)
]
assert descendants_count([
    ('Peter_II', 'Alexei'),
    ('Peter_III', 'Anna'),
    ('Paul_I', 'Peter_III'),
    ('Alexander_I', 'Paul_I'),
    ('Nicholaus_I', 'Paul_I'),
    ('Alexei', 'Peter_I'),
    ('Anna', 'Peter_I'),
    ('Elizabeth', 'Peter_I'),
]) == [
    ('Alexander_I', 0),
    ('Alexei', 1),
    ('Anna', 4),
    ('Elizabeth', 0),
    ('Nicholaus_I', 0),
    ('Paul_I', 2),
    ('Peter_I', 8),
    ('Peter_II', 0),
    ('Peter_III', 3)
]
assert descendants_count([
    ('A', 'B'),
    ('C', 'D'),
    ('E', 'F'),
]) == [
    ('A', 0),
    ('B', 1),
    ('C', 0),
    ('D', 1),
    ('E', 0),
    ('F', 1),
]
assert descendants_count([
    ('A', 'B'),
    ('B', 'C'),
    ('C', 'D'),
]) == [
    ('A', 0),
    ('B', 1),
    ('C', 2),
    ('D', 3),
]
assert descendants_count([
    ('C', 'D'),
    ('B', 'C'),
    ('A', 'B'),
]) == [
    ('A', 0),
    ('B', 1),
    ('C', 2),
    ('D', 3),
]
assert descendants_count([
    ('A', 'X'),
    ('B', 'X'),
    ('C', 'X'),
]) == [
    ('A', 0),
    ('B', 0),
    ('C', 0),
    ('X', 3),
]
assert descendants_count([
    ('A', 'B'),
]) == [
    ('A', 0),
    ('B', 1),
]
assert descendants_count([
    ('A', 'X'),
    ('B', 'X'),
    ('C', 'Y'),
    ('D', 'Y'),
    ('Y', 'X'),
]) == [
    ('A', 0),
    ('B', 0),
    ('C', 0),
    ('D', 0),
    ('X', 5),
    ('Y', 2),
]
assert descendants_count([
    ('A', 'X'),
    ('B', 'X'),
    ('C', 'Y'),
    ('D', 'Y'),
    ('X', 'Z'),
    ('Y', 'Z'),
]) == [
    ('A', 0),
    ('B', 0),
    ('C', 0),
    ('D', 0),
    ('X', 2),
    ('Y', 2),
    ('Z', 6),
]
assert descendants_count([
    ('A', 'X'),
    ('B', 'X'),
    ('C', 'Y'),
    ('D', 'Y'),
    ('X', 'Z'),
    ('Y', 'B'),
]) == [
    ('A', 0),
    ('B', 3),
    ('C', 0),
    ('D', 0),
    ('X', 5),
    ('Y', 2),
    ('Z', 6),
]


def main():
    n = int(input())
    descendant_parent_pairs = [tuple(input().split()) for _ in range(n - 1)]
    results = descendants_count(descendant_parent_pairs)
    for name, descendants in results:
        print(name, descendants)


if __name__ == '__main__':
    main()
