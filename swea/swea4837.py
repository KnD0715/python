import sys

sys.stdin = open('input_4837.txt')

T = int(input())
num_list = [i for i in range(1, 13)]

for test in range(1, T + 1):
    N, K = map(int, input().split())
    sub_set = []    # 부분 집합을 담을 리스트 생성

    for i in range(1 << len(num_list)): # 부분 집합
        middle_list = []
        for j in range(len(num_list)):
            if i & (1 << j):
                middle_list.append(num_list[j])

        sub_set.append(middle_list)

    count = 0

    for set in sub_set: # 부분 집합을 담을 리스트 반복
        total = 0   # 합계 값 초기 설정
        if len(set) == N:   # 만약 부분집합의 길이가 N으로 같으면
            for num in set: # 부분집합 부분 값을 더함
                total += num
            if total == K:  # 합계 값이 K랑 같으면
                count += 1  # 1 증가

    print(f"#{test} {count}")
