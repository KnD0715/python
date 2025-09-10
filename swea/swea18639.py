import sys

sys.stdin = open('input_18639.txt')


def merge_sort(arr):
    global count
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_ = merge_sort(left)
    right_ = merge_sort(right)

    if left_[-1] > right_[-1]:
        count += 1

    return merge(left_, right_)


def merge(left, right):
    i, j = 0, 0
    sorted_list = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1

        else:
            sorted_list.append(right[j])
            j += 1

    while i < len(left):
        sorted_list.append(left[i])
        i += 1

    while j < len(right):
        sorted_list.append(right[j])
        j += 1

    return sorted_list


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))
    count = 0
    result = merge_sort(num_list)

    print(f"#{tc} {result[N // 2]} {count}")
