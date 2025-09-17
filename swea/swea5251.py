from heapq import heappush, heappop


def dijkstra(start_node):
    pq = [(0, start_node)]
    dists = [INF] * (V + 1)
    dists[start_node] = 0

    while pq:
        dist, node = heappop(pq)

        if dists[node] < dist:
            continue

        for next_dist, next_node in graph[node]:
            new_dist = next_dist + dist

            if dists[next_node] <= new_dist:
                continue

            dists[next_node] = new_dist
            heappush(pq, (new_dist, next_node))

    return dists


INF = int(21e8)

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    start_node = 0
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))

    result = dijkstra(start_node)
    print(f"#{tc} {result[V]}")
