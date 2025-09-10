import sys

sys.stdin = open('input_2819.txt')


def dfs(idx, x, y, num):
    num += board[x][y]

    if idx == 6:
        result.append(num)
        return

    for row, column in circuit_list:
        if 0 <= row + x < 4 and 0 <= column + y < 4:
            dfs(idx + 1, row + x, column + y, num)


T = int(input())
for tc in range(1, T + 1):
    board = [list(map(str, input().split())) for _ in range(4)]
    circuit_list = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    result = []
    for row in range(4):
        for col in range(4):
            dfs(0, row, col, "")

    ans = set(result)

    print(f"#{tc} {len(ans)}")
