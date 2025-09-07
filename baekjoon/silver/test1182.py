import sys

def sequence(start, total):
    global count

    if start >= N:
        return

    total += num_list[start]

    if total == S:
        count += 1

    sequence(start + 1, total)
    sequence(start + 1, total - num_list[start])

N, S = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

count = 0

sequence(0, 0)

print(count)