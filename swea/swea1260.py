T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    chemistry = [list(map(int, input().split())) for _ in range(N)]

    container = []

    for i in range(N):
        for j in range(N):
            if chemistry[i][j]:
                w = j + 1
                while w < N and chemistry[i][w]:
                    w += 1

                width = w - j

                h = i + 1
                while h < N and chemistry[h][j]:
                    h += 1

                height = h - i

                container.append((height, width))

                zero_i, zero_j = i, j

                for m in range(i, h):
                    for n in range(j, w):
                        chemistry[m][n] = 0

    rows = {r for r, c in container}
    cols = {c for r, c in container}
    nxt = {r: c for r, c in container}

    start = (rows - cols).pop()
    dims = [start]
    while dims[-1] in nxt:
        dims.append(nxt[dims[-1]])


    k = len(dims) - 1
    if k <= 1:
        result = 0
    else:
        m = [[0] * (k + 1) for _ in range(k + 1)]
        for L in range(2, k + 1):
            for i in range(1, k - L + 2):
                j = i + L - 1
                m[i][j] = min(
                    m[i][t] + m[t + 1][j] + dims[i - 1] * dims[t] * dims[j]
                    for t in range(i, j)
                )
        result = m[1][k]

    print(f"#{tc} {result}")