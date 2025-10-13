import sys

N = int(sys.stdin.readline())
coordinates = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    coordinates.append((x, y))

coordinates.sort()

for px, py in coordinates:
    print(f"{px} {py}")