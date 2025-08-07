import sys

sys.stdin = open('input_1966.txt')


def sorted_arr(arr):    # 버블 정렬
    length = len(arr)   # 리스트의 길이 확인

    for i in range(length):
        for j in range(0, length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


T = int(input())
for i in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))

    sort_list = sorted_arr(num_list)    # 함수를 통해 리스트 정렬

    print(f"#{i}", *sort_list)
