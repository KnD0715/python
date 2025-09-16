from collections import deque

def calc():
    global result
    while q:
        num, check = q.popleft()
        if num == M:
            result = check
            return

        for i in range(4):
            if i == 0:
                if 1 <= num + 1 <= 1000000 and visited[num + 1] == False:
                    q.append((num + 1, check + 1))
                    visited[num + 1] = True

            elif i == 1:
                if 1 <= num - 1 <= 1000000 and visited[num - 1] == False:
                    q.append((num - 1, check + 1))
                    visited[num - 1] = True

            elif i == 2:
                if 1 <= num * 2 <= 1000000 and visited[num * 2] == False:
                    q.append((num * 2, check + 1))
                    visited[num * 2] = True

            elif i == 3:
                if 1 <= num - 10 <= 100000 and visited[num - 10] == False:
                    q.append((num - 10, check + 1))
                    visited[num - 10] = True

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [False] * 1000001
    q = deque()
    result = 0
    q.append((N, 0))
    calc()

    print(f"#{tc} {result}")