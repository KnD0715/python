T = int(input())  # 테스트 케이스 입력

for i in range(1, T + 1):  # 테스트 케이스 수만큼 반복
    N = int(input())  # 배열 개수 입력
    num_list = list(map(int, input().split()))  # 숫자 입력

    max_num = 0  # 최대값 인덱스 초기 설정
    min_num = 0  # 최소값 인덱스 초기 설정
    count = 0  # 카운트 초기 설정

    for num in range(len(num_list)):  # 최대값 인덱스 찾기
        if num_list[num] >= num_list[max_num]:
            max_num = num

    for num in range(len(num_list)):  # 최소값 인덱스 찾기
        if num_list[num] < num_list[min_num]:
            min_num = num

    if max_num > min_num:  # 최대값 인덱스가 최소값 인덱스보다 클 때
        for cnt in range(min_num, max_num):
            count += 1
    elif min_num > max_num:  # 그 반대
        for cnt in range(max_num, min_num):
            count += 1

    print(f"#{i} {count}")
