import sys

N, M = map(int, sys.stdin.readline().split())
num_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
DP = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        DP[i][j] = num_list[i - 1][j - 1] + DP[i][j - 1] + DP[i - 1][j] - DP[i - 1][j - 1]

K = int(sys.stdin.readline())
for _ in range(K):
    i, j, x, y = map(int, sys.stdin.readline().split())
    print(DP[x][y] - DP[x][j - 1] - DP[i - 1][y] + DP[i - 1][j - 1])


