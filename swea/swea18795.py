import sys

sys.stdin = open('input_18795.txt')


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
    num_list = list(map(int, input().split()))

    print(f"#{tc}", *quick_sort(num_list))
