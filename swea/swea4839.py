import sys

sys.stdin = open('input_4839.txt')


def binary_search(page, search):
    start = 1  # 시작 페이지
    end = page  # 끝 페이지
    count = 0  # 카운트

    while start <= end:  # 찾을 시작 페이지와 끝 페이지가 같아질때까지반복
        mid = int((start + end) / 2)  # 중간 지점
        if mid == search:  # 중간 지점과 찾을 페이지가 같으면
            return count  # count return
        elif mid > search:  # 중간 지점이 찾을 페이지보다 크면
            end = mid  # 중간 부분을 끝 페이지로 설정
            count += 1  # 카운트 1 증가
        else:  # 중간 지점이 찾을 페이지보다 작으면
            start = mid  # 중간 부분을 처음 페이지로 설정
            count += 1  # 카운트 1 증가


T = int(input())
for i in range(1, T + 1):
    page, search_A, search_B = map(int, input().split())

    A_count = binary_search(page, search_A)
    B_count = binary_search(page, search_B)

    if A_count == B_count:
        result = 0
    elif A_count > B_count:
        result = 'B'
    elif A_count < B_count:
        result = 'A'

    print(f"#{i} {result}")
