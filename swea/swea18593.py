import sys

sys.stdin = open('input_18593.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    binary_list = [list(map(int, input().strip())) for _ in range(N)]

    pow = 6
    result = []
    total = 0
    for i in range(N):
        for j in range(10):
            if binary_list[i][j] == 1:
                total += 2 ** pow
            pow -= 1

            if pow == -1:
                pow = 6
                result.append(total)
                total = 0

    print(f"#{tc}", *result)
