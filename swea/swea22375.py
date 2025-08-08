T = int(input())
for i in range(1, T + 1):
    length = int(input())
    Init_state = list(map(int, input().split()))  # 초기 전등 상태 리스트
    Manipulate_state = list(map(int, input().split()))  # 만들 전등 상태 리스트

    count = 0
    for num in range(length):  # 전등 리스트 길이 만큼 반복
        if Init_state[num] != Manipulate_state[num]:  # 초기 전등 상태와 만들 전등 상태의 값이 다를 시
            for change in range(num, length):  # num부터 전등 길이까지 다 바꿈
                if Init_state[change] == 1:  # 초기 전등의 값이 1이면
                    Init_state[change] = 0  # 0으로 바꿈
                else:
                    Init_state[change] = 1  # 초기 전등의 값이 0이면 1로 바꿈

            count += 1  # if 문이 실행될 때마다 카운트 증가

        else:
            continue  # 아니면 다음 번호로 넘어감

    print(f"#{i} {count}")
