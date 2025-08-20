import sys

sys.stdin = open('input_18400.txt')

T = int(input())

for tc in range(1, T + 1):
    length, rotation = map(int, input().split())
    q = list(map(int, input().split()))

    for i in range(rotation):
        q.append(q.pop(0))

    print(f"#{tc} {q[0]}")
