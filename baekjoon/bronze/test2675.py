import sys

T = int(sys.stdin.readline())
result = ""
for i in range(T):
    num, word = sys.stdin.readline().split()
    for opp in word:
        result += int(num) * opp    
    print(result)
    result = ""
