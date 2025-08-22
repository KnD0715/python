import sys

sys.stdin = open('input_1231.txt')


def in_order(T):
    global result
    if T:
        in_order(left[T])
        result += alphabet[T]
        in_order(right[T])

    return result


for tc in range(1, 11):
    N = int(input())

    left = [0] * (N + 1)
    right = [0] * (N + 1)
    parent = [0] * (N + 1)
    alphabet = [''] * (N + 1)

    for _ in range(N):
        tree_list = input().split()

        p = int(tree_list[0])
        alphabet[p] = tree_list[1]

        if len(tree_list) >= 3:
            c = int(tree_list[2])
            left[p] = c
            parent[c] = p

        if len(tree_list) >= 4:
            c = int(tree_list[3])
            right[p] = c
            parent[c] = p

    result = ''

    print(f"#{tc} {in_order(1)}")
