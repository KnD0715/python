import sys

sys.stdin = open('input_18640.txt')


def binary_search(num):
    global count
    start = 0
    end = N - 1
    direct = 0

    while start <= end:
        mid = (start + end) // 2

        if find_list[mid] == num:
            return True

        elif find_list[mid] > num:
            if direct == -1:
                return False
            else:
                end = mid - 1
                direct = -1

        else:
            if direct == 1:
                return False
            else:
                start = mid + 1
                direct = 1

    return False


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    find_list = list(map(int, input().split()))
    num_list = list(map(int, input().split()))
    count = 0
    find_list.sort()

    for i in num_list:
        if binary_search(i):
            count += 1

    print(f"#{tc} {count}")
