import sys

people = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split()))

sorted_line = sorted(line)

count = 0
result = 0
for i in range(people):
    count += sorted_line[i]
    result += count

print(result)