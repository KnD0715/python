from collections import deque
import sys

q = deque()
N = int(sys.stdin.readline())
for _ in range(N):
    command_list = list(map(int, sys.stdin.readline().split()))

    if command_list[0] == 1:
        q.appendleft(command_list[1])
    elif command_list[0] == 2:
        q.append(command_list[1])
    elif command_list[0] == 3:
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif command_list[0] == 4:
        if q:
            print(q.pop())
        else:
            print(-1)
    elif command_list[0] == 5:
        print(len(q))
    elif command_list[0] == 6:
        if not q:
            print(1)
        else:
            print(0)
    elif command_list[0] == 7:
        if q:
            print(q[0])
        else:
            print(-1)
    elif command_list[0] == 8:
        if q:
            print(q[-1])
        else:
            print(-1)