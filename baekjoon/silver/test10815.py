import sys

get_card_num = int(sys.stdin.readline())
get_card_list = list(map(int, sys.stdin.readline().split()))
check_card_num = int(sys.stdin.readline())
check_card_list = list(map(int, sys.stdin.readline().split()))

have = set(get_card_list)

print(' '.join('1' if x in have else '0' for x in check_card_list))
