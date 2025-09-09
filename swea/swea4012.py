import sys

sys.stdin = open('input_4012.txt')

from collections import deque


def arr(num):
    if len(path) == N // 2:
        combination.append(path[:])
        return

    for i in range(num, N + 1):
        if i not in path:
            path.append(i)
            arr(i + 1)
            path.pop()


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cook_synergy = [list(map(int, input().split())) for _ in range(N)]

    path = []
    combination = deque()
    arr(1)

    result = []

    while combination:
        synergy_1 = combination.popleft()
        synergy_2 = combination.pop()

        cook_1 = 0
        cook_2 = 0

        for i in synergy_1:
            for j in synergy_1:
                if cook_synergy[i - 1][j - 1] == 0:
                    continue
                else:
                    cook_1 += cook_synergy[i - 1][j - 1]

        for i in synergy_2:
            for j in synergy_2:
                if cook_synergy[i - 1][j - 1] == 0:
                    continue
                else:
                    cook_2 += cook_synergy[i - 1][j - 1]

        result.append(abs(cook_1 - cook_2))

    print(f"#{tc} {min(result)}")
