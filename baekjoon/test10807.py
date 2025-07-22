import sys

N = int(sys.stdin.readline())

my_list = list(map(int, sys.stdin.readline().split()))

V = int(sys.stdin.readline())

print (my_list.count(V))