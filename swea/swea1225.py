import sys

sys.stdin = open('input_1225.txt')

for tc in range(1, 11):
    N = int(input())
    q = list(map(int, input().split()))

    while q[-1] > 0:
        q[0] -= 1
        q.append(q.pop(0))
        if q[-1] <= 0:
            q[-1] = 0
            break
        q[0] -= 2
        q.append(q.pop(0))
        if q[-1] <= 0:
            q[-1] = 0
            break
        q[0] -= 3
        q.append(q.pop(0))
        if q[-1] <= 0:
            q[-1] = 0
            break
        q[0] -= 4
        q.append(q.pop(0))
        if q[-1] <= 0:
            q[-1] = 0
            break
        q[0] -= 5
        q.append(q.pop(0))
        if q[-1] <= 0:
            q[-1] = 0
            break

    print(f"#{tc}", *q)
