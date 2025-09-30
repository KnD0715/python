import sys

N = int(sys.stdin.readline())
room = list(map(int, input().split()))

count = 0

avg = sum(room) // N

prefix = 0
min_prefix = 0
sum_prefix = 0

for mem in room:
    prefix += mem - avg
    sum_prefix += prefix
    if prefix < min_prefix:
        min_prefix = prefix

count = sum_prefix - N * min_prefix

print(count)