import sys

sys.stdin = open('input_18529.txt')


def hex_to_bin(num):
    hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    hex_num = hex.index(num)

    bin = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100',
           '1101',
           '1110', '1111']

    return bin[hex_num]


T = int(input())
for tc in range(1, T + 1):
    my_list = list(map(str, input().split()))

    result = ''

    for i in my_list[1]:
        result += hex_to_bin(i)

    print(f"#{tc} {result}")
