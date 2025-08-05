T = int(input())    # 테스트 케이스 수 입력

for i in range(1, T + 1):
    N = int(input())    # 양수 개수 입력
    num_list = list(map(int, input().split()))

    max_num = num_list[0]   # 최대값 초기 설정
    min_num = num_list[0]   # 최소값 초기 설정

    for num in num_list:
        if max_num < num:
            max_num = num

    for num in num_list:
        if min_num > num:
            min_num = num

    result = max_num - min_num

    print(f"#{i} {result}")
