import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    number_list = []
    result = 'YES'
    for i in range(N):
        number = sys.stdin.readline().strip()
        number_list.append(number)
    number_list.sort()

    for i in range(N - 1):
        if number_list[i] == number_list[i + 1][:len(number_list[i])]:
            result = 'NO'

    print(result)