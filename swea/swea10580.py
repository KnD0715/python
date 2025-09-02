import sys

sys.stdin = open('input_10580.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    line = []

    count = 0
    for _ in range(N):
        line.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(i + 1, N):

            if (line[i][0] - line[j][0]) * (line[i][1] - line[j][1]) < 0:
                count += 1

    print(f"#{tc} {count}")
