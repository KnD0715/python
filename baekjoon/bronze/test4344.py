import sys

T = int(sys.stdin.readline())
for _ in range(T):
    num_list = list(map(int, sys.stdin.readline().split()))

    score = sum(num_list[1:])
    average = score / num_list[0]

    count = 0
    for i in range(1, num_list[0] + 1):
        if num_list[i] > average:
            count += 1

    print(f"{count / num_list[0] * 100:.3f}%")