import sys

num = int(sys.stdin.readline())
result = 1
zero_count = 0
for i in range (1, num + 1):
    result *= i

num_list = list(map(int, str(result)))
reversed_list = reversed(num_list)

for count in reversed_list:
    if count == 0:
        zero_count += 1
    elif count != 0:
        break

print (zero_count)
