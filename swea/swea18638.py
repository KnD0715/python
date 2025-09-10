import sys

sys.stdin = open('input_18638.txt')


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    left = [i for i in tail if i <= pivot]
    right = [i for i in tail if i > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))
    sorted_list = quick_sort(num_list)

    print(f"#{tc} {sorted_list[N // 2]}")
