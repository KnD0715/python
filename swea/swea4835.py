t = int(input())  # 테스트 케이스 입력

for i in range(1, t + 1):
    n, m = map(int, input().split())  # 정수의 개수와 구간의 개수 입력
    num_list = list(map(int, input().split()))  # 숫자 리스트 입력
    sum_list = []   # 구간합 리스트
    for j in range(n - m + 1):  # 배열 갯수와 구간 갯수만큼 반복
        result = 0
        for k in num_list[j:j + m]:
            if j + m > len(num_list):
                break
            result += k  # 구간만큼 k 출력 후 덧셈

        sum_list.append(result)  # 구간합 리스트에 추가

    max_num = sum_list[0]   # 구간합 리스트의 초기값 설정
    min_num = sum_list[0]   # 구간합 리스트의 초기값 설정

    for num in sum_list:
        if max_num < num:
            max_num = num   # 구간합 리스트의 최댓값 설정

    for num in sum_list:
        if min_num > num:
            min_num = num   # 구간합 리스트의 최소값 설정

    result = max_num - min_num

    print(f"#{i} {result}")
