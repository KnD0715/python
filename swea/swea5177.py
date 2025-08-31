def min_heap(arr):
    global last
    for i in range(len(arr)):
        last += 1
        heap[last] = num_list[i]
        child = last
        parent = last // 2

        while parent and heap[parent] > heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]
            child = parent
            parent = child // 2


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))

    heap = [0] * (N + 1)
    last = 0

    min_heap(num_list)

    result = 0

    while N > 0:
        result += heap[N // 2]
        N //= 2

    print(f"#{tc} {result}")
