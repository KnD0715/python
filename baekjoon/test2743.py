import sys

word = list(map(str, sys.stdin.readline()))
word.pop(-1)

count = 0
for i in word:
    count += 1

print(count)