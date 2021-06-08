import sys

m = int(input())
m_triplets = [tuple(map(int, input().split())) for _ in range(m)]

print(*m_triplets)

n, k = map(int, input().split())
n_words = [input() for _ in range(n)]
k_lists = [list(map(int, input().split())) for _ in range(k)]
print(*n_words)
print(*k_lists)

unknown_count_of_floats = map(float, sys.stdin.read().split())
print(*unknown_count_of_floats)
