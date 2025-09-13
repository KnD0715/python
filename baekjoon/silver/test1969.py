import sys

N, M = map(int, sys.stdin.readline().split())
DNA = []
for _ in range(N):
    DNA.append(list(sys.stdin.readline().strip()))

count = 0
result = ''
for c in range(M):
    A, C, G, T = 0, 0, 0, 0
    for r in range(N):
        if DNA[r][c] == 'A':
            A += 1
        elif DNA[r][c] == 'C':
            C += 1
        elif DNA[r][c] == 'G':
            G += 1
        elif DNA[r][c] == 'T':
            T += 1

    if max(A, C, G, T) == A:
        result += 'A'
        count += C + G + T
    elif max(A, C, G, T) == C:
        result += 'C'
        count += A + G + T
    elif max(A, C, G, T) == G:
        result += 'G'
        count += A + C + T
    elif max(A, C, G, T) == T:
        result += 'T'
        count += A + C + G

print(result)
print(count)