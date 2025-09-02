# import sys
# sys.stdin = open('input_4408.txt')

T = int(input())
for tc in range(1, T + 1):
    enter = [0] * 201
    N = int(input())
    room = []

    for _ in range(N):
        start, end = map(int, input().split())
        s = (start - 1) // 2
        e = (end - 1) // 2

        if s > e:
            s, e = e, s

        room.append((s, e))

        while room:
            s, e = room.pop()
            for i in range(s, e + 1):
                enter[i] += 1

        count = max(enter)

    print(f"#{tc} {count}")
