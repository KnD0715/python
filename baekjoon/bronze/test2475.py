import sys

my_list = list(map(int, sys.stdin.readline().split()))
pow_list = list(map(lambda x : x ** 2, my_list))
veri_num = sum(pow_list) % 10

print (veri_num)