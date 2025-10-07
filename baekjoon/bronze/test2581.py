import sys
start_num = int(sys.stdin.readline())
end_num = int(sys.stdin.readline())
arr = []

for num in range(start_num, end_num + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break

        else:
            arr.append(num)

if len(arr) == 0:
    print(-1)

else:
    print(sum(arr))
    print(min(arr))