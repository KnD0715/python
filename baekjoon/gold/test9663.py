import sys


def dfs(row):
    global count

    if row == N:
        count += 1
        return

    for col in range(N):
        visited[row] = col
        if check(row):
            dfs(row + 1)


def check(new_row):
    for prev_row in range(new_row):
        if visited[new_row] == visited[prev_row] or new_row - prev_row == abs(visited[new_row] - visited[prev_row]):
            return False

    return True


N = int(sys.stdin.readline())

count = 0
visited = [0] * N
dfs(0)

print(count)
