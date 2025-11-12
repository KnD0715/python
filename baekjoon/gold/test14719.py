import sys

H, W = map(int, sys.stdin.readline().split())
ground = list(map(int, sys.stdin.readline().split()))
count = 0

for i in range(1, W - 1):
    left_max = max(ground[:i])
    right_max = max(ground[i + 1:])

    compare = min(left_max, right_max)

    if ground[i] < compare:
        count += compare - ground[i]

print(count)