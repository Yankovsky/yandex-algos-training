# https://contest.yandex.ru/contest/28069/problems/I/
import sys

sys.setrecursionlimit(100000)


class GenealogicalTreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.depth = 0

    def update_depth(self, increment):
        self.depth += increment
        for child in self.children:
            child.update_depth(increment)


def nodes_depth(descendant_parent_pairs):
    nodes = {}
    for (descendant, parent) in descendant_parent_pairs:
        if parent not in nodes:
            nodes[parent] = GenealogicalTreeNode(parent)
        if descendant not in nodes:
            nodes[descendant] = GenealogicalTreeNode(descendant)

        nodes[parent].children.append(nodes[descendant])
        nodes[descendant].update_depth(nodes[parent].depth + 1)

    return sorted((name, node.depth) for name, node in nodes.items())


assert nodes_depth([
    ('Alexei', 'Peter_I'),
    ('Anna', 'Peter_I'),
    ('Elizabeth', 'Peter_I'),
    ('Peter_II', 'Alexei'),
    ('Peter_III', 'Anna'),
    ('Paul_I', 'Peter_III'),
    ('Alexander_I', 'Paul_I'),
    ('Nicholaus_I', 'Paul_I'),
]) == [
    ('Alexander_I', 4),
    ('Alexei', 1),
    ('Anna', 1),
    ('Elizabeth', 1),
    ('Nicholaus_I', 4),
    ('Paul_I', 3),
    ('Peter_I', 0),
    ('Peter_II', 2),
    ('Peter_III', 2)
]
assert nodes_depth([
    ('Peter_II', 'Alexei'),
    ('Peter_III', 'Anna'),
    ('Paul_I', 'Peter_III'),
    ('Alexander_I', 'Paul_I'),
    ('Nicholaus_I', 'Paul_I'),
    ('Alexei', 'Peter_I'),
    ('Anna', 'Peter_I'),
    ('Elizabeth', 'Peter_I'),
]) == [
    ('Alexander_I', 4),
    ('Alexei', 1),
    ('Anna', 1),
    ('Elizabeth', 1),
    ('Nicholaus_I', 4),
    ('Paul_I', 3),
    ('Peter_I', 0),
    ('Peter_II', 2),
    ('Peter_III', 2)
]
assert nodes_depth([
    ('A', 'B'),
    ('C', 'D'),
    ('E', 'F'),
]) == [
    ('A', 1),
    ('B', 0),
    ('C', 1),
    ('D', 0),
    ('E', 1),
    ('F', 0),
]
assert nodes_depth([
    ('A', 'B'),
    ('B', 'C'),
    ('C', 'D'),
]) == [
    ('A', 3),
    ('B', 2),
    ('C', 1),
    ('D', 0),
]
assert nodes_depth([
    ('C', 'D'),
    ('B', 'C'),
    ('A', 'B'),
]) == [
    ('A', 3),
    ('B', 2),
    ('C', 1),
    ('D', 0),
]
assert nodes_depth([
    ('A', 'X'),
    ('B', 'X'),
    ('C', 'X'),
]) == [
    ('A', 1),
    ('B', 1),
    ('C', 1),
    ('X', 0),
]
assert nodes_depth([
    ('A', 'B'),
]) == [
    ('A', 1),
    ('B', 0),
]
assert nodes_depth([
    ('A', 'X'),
    ('B', 'X'),
    ('C', 'Y'),
    ('D', 'Y'),
    ('Y', 'X'),
]) == [
    ('A', 1),
    ('B', 1),
    ('C', 2),
    ('D', 2),
    ('X', 0),
    ('Y', 1),
]
assert nodes_depth([
    ('A', 'X'),
    ('B', 'X'),
    ('C', 'Y'),
    ('D', 'Y'),
    ('X', 'Z'),
    ('Y', 'Z'),
]) == [
    ('A', 2),
    ('B', 2),
    ('C', 2),
    ('D', 2),
    ('X', 1),
    ('Y', 1),
    ('Z', 0),
]
assert nodes_depth([
    ('A', 'X'),
    ('B', 'X'),
    ('C', 'Y'),
    ('D', 'Y'),
    ('X', 'Z'),
    ('Y', 'B'),
]) == [
    ('A', 2),
    ('B', 2),
    ('C', 4),
    ('D', 4),
    ('X', 1),
    ('Y', 3),
    ('Z', 0),
]
assert nodes_depth([
    ('AQHFYP', 'MKFXCLZBT'),
    ('AYKOTYQ', 'QIUKGHWCDC'),
    ('IWCGKHMFM', 'WPLHJL'),
    ('MJVAURUDN', 'QIUKGHWCDC'),
    ('MKFXCLZBT', 'IWCGKHMFM'),
    ('PUTRIPYHNQ', 'UQNGAXNP'),
    ('QIUKGHWCDC', 'WPLHJL'),
    ('UQNGAXNP', 'WPLHJL'),
    ('YURTPJNR', 'QIUKGHWCDC'),
]) == [
    ('AQHFYP', 3),
    ('AYKOTYQ', 2),
    ('IWCGKHMFM', 1),
    ('MJVAURUDN', 2),
    ('MKFXCLZBT', 2),
    ('PUTRIPYHNQ', 2),
    ('QIUKGHWCDC', 1),
    ('UQNGAXNP', 1),
    ('WPLHJL', 0),
    ('YURTPJNR', 2),
]
assert nodes_depth([
    ('BFNRMLH', 'CSZMPFXBZ'),
    ('CSZMPFXBZ', 'IHWBQDJ'),
    ('FMVQTU', 'FUXATQUGIG'),
    ('FUXATQUGIG', 'IRVAVMQKN'),
    ('GNVIZ', 'IQGIGUJZ'),
    ('IHWBQDJ', 'LACXYFQHSQ'),
    ('IQGIGUJZ', 'JMUPNYRQD'),
    ('IRVAVMQKN', 'GNVIZ'),
    ('JMUPNYRQD', 'BFNRMLH'),
]) == [
    ('BFNRMLH', 3),
    ('CSZMPFXBZ', 2),
    ('FMVQTU', 9),
    ('FUXATQUGIG', 8),
    ('GNVIZ', 6),
    ('IHWBQDJ', 1),
    ('IQGIGUJZ', 5),
    ('IRVAVMQKN', 7),
    ('JMUPNYRQD', 4),
    ('LACXYFQHSQ', 0),
]


def main():
    n = int(input())
    descendant_parent_pairs = [tuple(input().split()) for _ in range(n - 1)]
    results = nodes_depth(descendant_parent_pairs)
    for name, descendants in results:
        print(name, descendants)


if __name__ == '__main__':
    main()
