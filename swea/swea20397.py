T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    stones = list(map(int, input().split()))
    for num in range(M):
        i, j = map(int, input().split())
        for swap in range(1, j + 1):
            if 0 <= i - 1 - swap < N and 0 <= i - 1 + swap < N:
                if stones[i - 1 - swap] == stones[i - 1 + swap]:
                    if stones[i - 1 - swap] == 1:
                        stones[i - 1 - swap] = 0

                    else:
                        stones[i - 1 - swap] = 1

                    if stones[i - 1 + swap] == 1:
                        stones[i - 1 + swap] = 0

                    else:
                        stones[i - 1 + swap] = 1

    print(f"#{tc}", *stones)