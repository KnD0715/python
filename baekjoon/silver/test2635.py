import sys
N = int(sys.stdin.readline())
ans = []

for i in range(1, N + 1):
    first = N
    second = i
    temp = [N, i]

    while True:
        next_num = first - second
        if next_num >= 0:
            temp.append(next_num)
            first = second
            second = next_num

        else:
            if len(temp) > len(ans):
                ans = temp

            break

print(len(ans))
print(*ans)

