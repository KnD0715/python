import sys

w, h = map(int, sys.stdin.readline().split())
n = int(input())

weight = [0, w]
height = [0, h]

for i in range(n):
    a, b = map(int, input().split())
    if a == 0:
        height.append(b)

    else:
        weight.append(b)

weight.sort()
height.sort()

check_weight = []
check_height = []

for i in range(1, len(weight)):
    check_weight.append(weight[i] - weight[i - 1])

for i in range(1, len(height)):
    check_height.append(height[i] - height[i - 1])

print(max(check_weight) * max(check_height))