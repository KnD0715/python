import sys

sys.stdin = open('input_9367.txt')


def max_value(num):
    max_num = 0
    for i in num:
        if max_num < i:
            max_num = i

    return max_num


T = int(input())

for i in range(1, T + 1):
    num = int(input())
    carrots = list(map(int, input().split()))   # 힘들다면 당근을 흔들어주세요

    count = 0
    count_list = []
    carrot = 0  # 당근 셀 값 초기 설정
    for carrot_size in carrots: # 당근 리스트 반복
        if carrot < carrot_size:    # 당근 크기가 더 크면
            carrot = carrot_size    # 당근 크기 값을 재할당하고
            count += 1  # 1 증가

        else:
            count_list.append(count)    # 안 크면 지금까지 셌던 거 카운트 리스트에 넣고
            count = 1   # 카운트 초기화
            carrot = carrot_size    # 당근 크기도 재할당

    count_list.append(count)    # 남은 카운트 털어버리기~

    print(f"#{i} {max_value(count_list)}")
