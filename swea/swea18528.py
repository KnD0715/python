import sys

sys.stdin = open('input_18528.txt')


def pre_order(T):
    global result
    if T:
        result += value[T]
        pre_order(left[T])
        pre_order(right[T])

    return result


T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())

    result = 0

    left = [0] * (N + 1)
    right = [0] * (N + 1)
    parent = [0] * (N + 1)
    value = [0] * (N + 1)

    for i in range(2, N + 1):
        if i % 2 == 0:
            left[i // 2] = i
            parent[i] = i // 2
        else:
            right[i // 2] = i
            parent[i] = i // 2

    for _ in range(M):
        node, values = map(int, input().split())
        value[node] = values

    print(f"#{tc} {pre_order(L)}")
