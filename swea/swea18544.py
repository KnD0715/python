import sys

sys.stdin = open('input_18544.txt')

result = []
def pre_order(T):
    global result
    if T:
        result.append(T)
        pre_order(left[T])
        pre_order(right[T])

    return result


node_num = int(input())
route_list = list(map(int, input().split()))

left = [0] * (node_num + 1)
right = [0] * (node_num + 1)
parent = [0] * (node_num + 1)

for i in range(len(route_list) // 2):
    p, c = route_list[i * 2], route_list[i * 2 + 1]
    parent[c] = p

    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c

root = 1
for i in range(1, node_num + 1):
    if parent[i] == 0:
        root = i
        break

result = pre_order(root)

print(*result)
