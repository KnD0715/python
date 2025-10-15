from collections import deque

import sys

N = int(sys.stdin.readline())
count = 0
for _ in range(N):
    result = True
    alphabet = [0] * 26
    word = list(sys.stdin.readline().strip())
    q = deque(word)

    while q:
        ch = q.popleft()
        if alphabet[ord(ch) - 97] == 0:
            while q:
                if q[0] == ch:
                    q.popleft()

                else:
                    break

            alphabet[ord(ch) - 97] += 1

        else:
            result = False

    if result:
        count += 1

print(count)