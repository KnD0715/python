import sys

num = int(sys.stdin.readline())

for i in range(1000000):
    result = i
    num_list = list(str(i))

    for n in num_list:
        result += int(n)

    if result == num:
        print(i)
        break

else:
    print(0)