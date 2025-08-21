from collections import deque
import sys

sys.stdin = open('input_18402.txt')


def bfs(start, end):
    Q.append(start)
    visited[start] = 1
    while Q:
        v = Q.popleft()
        for w in adj_list[v]:
            if not visited[w]:
                visited[w] = 1
                distance[w] = distance[v] + 1
                Q.append(w)

                if w == end:
                    return distance[w]

    return 0


T = int(input())
for tc in range(1, T + 1):
    node_num, route_num = map(int, input().split())  # 마지막 정점, 간선 수

    route_list = []
    adj_list = [[] for _ in range(node_num + 1)]

    for _ in range(route_num):
        start_node, end_node = map(int, input().split())  # start-end 노선
        route_list.append(start_node)
        route_list.append(end_node)

    for i in range(route_num):
        v1, v2 = route_list[i * 2], route_list[i * 2 + 1]
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)

    start, end = map(int, input().split())

    visited = [0] * (node_num + 1)
    distance = [0] * (node_num + 1)

    Q = deque()

    print(f"#{tc} {bfs(start, end)}")
