import sys

sys.stdin = open('input_18524.txt')


def pre_order(T):
    global count
    if T:
        count += 1
        pre_order(left[T])
        pre_order(right[T])

    return count


T = int(input())
for tc in range(1, T + 1):
    count = 0
    route_num, root = map(int, input().split())
    route_list = list(map(int, input().split()))

    left = [0] * (route_num + 2)
    right = [0] * (route_num + 2)
    parent = [0] * (route_num + 2)

    for i in range(route_num):
        p, c = route_list[i * 2], route_list[i * 2 + 1]
        parent[c] = p

        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    print(f"#{tc} {pre_order(root)}")
