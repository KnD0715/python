import sys

result = 1
num_count = [0] * 10
for _ in range(3):
    num = int(sys.stdin.readline())
    result *= num

for i in str(result):
    num_count[int(i)] += 1

for count in num_count:
    print(count)