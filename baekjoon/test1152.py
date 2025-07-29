import sys

sentence = list(sys.stdin.readline().split())

count = 0
for _ in sentence:
    count += 1

print (count)
