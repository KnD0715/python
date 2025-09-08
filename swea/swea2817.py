import sys

sys.stdin = open('input_2817.txt')


def part_sum(num, total):
    global count
    if total == M:
        count += 1
        return

    for i in range(num, N):
        part_sum(i + 1, total + num_list[i])


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    count = 0

    part_sum(0, 0)

    print(f"#{tc} {count}")
