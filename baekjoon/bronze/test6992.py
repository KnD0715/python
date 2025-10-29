import sys

N = int(sys.stdin.readline())

for _ in range(N):
    num_list = list(map(int, sys.stdin.readline().split()))
    num_list.pop(0)

    diff = num_list[1] - num_list[0]

    for i in range(1, len(num_list)):
        if num_list[i] - num_list[i - 1] != diff:
            print(f"The sequence {num_list} is not an arithmetic sequence.")
            break

    else:
        result = []
        for i in range(1, 6):
            result.append(num_list[-1] + (diff * i))

        print(f"The next 5 numbers after {num_list} are: {result}")
