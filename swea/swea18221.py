import sys

sys.stdin = open('input_18221.txt')

T = int(input())
for i in range(1, T + 1):
    word1 = input()
    word2 = input()

    if word1 in word2:
        result = 1
    else:
        result = 0

    print(f"#{i} {result}")
