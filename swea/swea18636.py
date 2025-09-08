import sys

sys.stdin = open('input_18636.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    time = []
    count = 0

    for _ in range(N):
        start, end = map(int, input().split())
        time.append((start, end))

    sorted_time = sorted(time, key=lambda x: x[1])

    now = 0

    for i in range(N):
        start = sorted_time[i][0]
        end = sorted_time[i][1]

        if now <= start:
            count += 1
            now = end

    print(f"#{tc} {count}")
