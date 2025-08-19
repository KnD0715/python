import sys

N, idx = map(int, sys.stdin.readline().split())

if N == 1:
    pascal = [[1]]
else:
    pascal = [[1], [1, 1]]
    for i in range(2, N):
        temp = [1]
        for j in range(1, i):
            temp.append(pascal[i - 1][j - 1] + pascal[i - 1][j])

        temp.append(1)
        pascal.append(temp)

print(pascal[N - 1][idx - 1])
