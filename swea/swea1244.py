import sys

sys.stdin = open('input_1244.txt')

def dfs(depth):
    global ans

    if depth == M:
        ans = max(ans, int(''.join(arr)))
        return

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]

            check = int(''.join(arr))
            if (depth, check) not in visited:
                visited.add((depth, check))
                dfs(depth + 1)

            arr[i], arr[j] = arr[j], arr[i]


result = []
T = int(input())
for case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(str(N))
    visited = set()
    ans = 0
    dfs(0)

    result.append(f"#{case} {ans}")

for _ in result:
    print(_)