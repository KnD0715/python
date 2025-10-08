import sys

def check_height(idx, total):
    if total > 100:
        return

    if len(path) > 7:
        return

    if len(path) == 7:
        if total == 100:
            result.append(path[:])
            return

        else:
            return

    for i in range(idx, 9):
        path.append(height[i])
        check_height(i + 1, total + height[i])
        path.pop()

height = []
result = []
path = []
for _ in range(9):
    height.append(int(sys.stdin.readline()))

height.sort()

check_height(0, 0)

dwarfs = result.pop(0)

for dwarf in dwarfs:
    print(dwarf)