from memory_profiler import memory_usage

print(memory_usage())
n = 1_000_000_00

arr = [0] * n

print(memory_usage())
