import sys
sys.stdin = open('input_1486.txt')

def arr(num, total):
    global result
    if total >= tower:
        result.append(total)
        return

    for i in range(num, N):
        arr(i + 1, total + height[i])


T = int(input())
for tc in range(1, T + 1):
    N, tower = map(int, input().split())
    height = list(map(int, input().split()))

    result = []
    arr(0, 0)

    print(f"#{tc} {min(result) - tower}")
