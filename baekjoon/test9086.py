import sys

T = int(sys.stdin.readline())

for i in range(T):
    word = list(sys.stdin.readline().strip())
    print(f"{word[0]}{word[-1]}")