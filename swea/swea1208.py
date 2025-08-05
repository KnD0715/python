for i in range(1, 11):  # 10개 테스트 케이스
    flatten_count = int(input())  # 덤프 횟수 입력
    my_list = list(map(int, input().split()))  # 상자
    max_number = 0  # 최대값 초기 설정
    min_number = 100  # 최소값 초기 설정 (상자 높이 100 이하)
    for _ in range(flatten_count):  # 덤프 횟수만큼 반복문
        max_num = 0  # 상자 최대값 인덱스 초기화
        min_num = 0  # 상자 최소값 인덱스 초기화

        for num in range(len(my_list)):  # 최대값 찾기
            if my_list[max_num] < my_list[num]:
                max_num = num

        for num in range(len(my_list)):  # 최소값 찾기
            if my_list[min_num] > my_list[num]:
                min_num = num

        my_list[max_num] -= 1  # 최대값 -1
        my_list[min_num] += 1  # 최소값 +1

    for number in my_list:  # 평탄화 된 상자 리스트 최대값 찾기
        if number > max_number:
            max_number = number

    for number in my_list:  # 평탄화 된 상자 리스트 최소값 찾기
       if number < min_number:
            min_number = number

    print(f"#{i} {max_number - min_number}")
