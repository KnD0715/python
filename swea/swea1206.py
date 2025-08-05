T = 10  # 테스트 케이스 입력

for i in range(1, 11):
    N = int(input())
    building = list(map(int, input().split()))  # 빌딩 높이 입력

    result = 0
    for j in range(N):

        if j == 0 or j == 1:    # j가 0이나 1이면 -2, -1할 시 음수가 나와 계산이 안되므로 넘기기
            continue

        if j + 1 >= len(building) or j + 2 >= len(building):    # j가 빌딩 리스트의 인덱스 값을 넘기면 인덱스 에러가 나기 때문에 넘기기 전 반복문 종료
            break
        for k in building[j - 2: j + 3]:
            my_list = [k - building[j - 2], k - building[j - 1], k, k - building[j + 1], k - building[j + 2]]   # k 값을 중앙으로 두고 좌우 2칸 계산
            for number in my_list:  # k의 값이 최댓값이어야 조경권 확보
                if number < 0:  # 리스트 내에 음수가 있다면 k가 최댓값이 아님
                    break   # 리스트 내에 음수가 있다면 바로 반복문 종료
            else:
                min_num = my_list[0]    # 최소값 초기 설정
                for num in my_list:
                    if num < 0:
                        continue
                    elif num < min_num:
                        min_num = num

                result += min_num   # 최소값 확정 후 결과 값 더하기

    print(f"#{i} {result}")
