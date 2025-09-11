import sys

sys.stdin = open('input_18641.txt')


def bus(location, count):
    global result

    if count >= result:
        return

    if location >= N - 1:
        if count <= result:
            result = count
        return

    for i in range(station[location]):
        bus(location + i + 1, count + 1)


T = int(input())
for tc in range(1, T + 1):
    station = list(map(int, input().split()))
    N = station.pop(0)
    result = float('inf')
    bus(0, -1)

    print(f"#{tc} {result}")
