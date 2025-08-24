import sys

num_list = []
N, M = map(int, sys.stdin.readline().split())

for i in range (1 , N + 1):
    num_list += [i]


for i in range(M):
    num1, num2 = map(int, sys.stdin.readline().split())
    
    num1 = num1 - 1
    num_list[num1:num2] = reversed(num_list[num1:num2])
print(*num_list)
