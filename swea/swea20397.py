T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 돌 개수 및 반복 횟수
    stones = list(map(int, input().split()))  # 돌 리스트
    for num in range(M):
        i, j = map(int, input().split())  # stones[i - 1] 돌을 기준으로 j개의 돌 뒤집기
        for swap in range(1, j + 1):  # 기준점에서 j개 반복
            if 0 <= i - 1 - swap < N and 0 <= i - 1 + swap < N:  # 인덱스 내에서 활용
                if stones[i - 1 - swap] == stones[i - 1 + swap]:  # 같은 색이면 뒤집기
                    if stones[i - 1 - swap] == 1:  # 기준점 앞
                        stones[i - 1 - swap] = 0

                    else:
                        stones[i - 1 - swap] = 1

                    if stones[i - 1 + swap] == 1:  # 기준점 뒤
                        stones[i - 1 + swap] = 0

                    else:
                        stones[i - 1 + swap] = 1

    print(f"#{tc}", *stones)
