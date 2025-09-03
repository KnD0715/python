import sys

sys.stdin = open('input_18612.txt')


def hex_to_bin(num):
    hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    num_idx = hex.index(num)

    bin = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100',
           '1101',
           '1110', '1111']

    return bin[num_idx]


def bin_to_dec(num):
    num_list = list(num)
    dec_list = []
    pow = 6
    total = 0
    length = len(num_list)

    for i in num_list:
        if i == '1':
            total += 2 ** pow
        pow -= 1

        if pow == -1:
            dec_list.append(total)
            pow = 6
            total = 0
            length -= 7

            if length // 7 == 0:
                pow = length - 1

    return dec_list


T = int(input())
for tc in range(1, T + 1):
    bin_list = ''
    hex_num = list(input().strip())

    for i in hex_num:
        bin_num = hex_to_bin(i)
        bin_list += bin_num

    result = bin_to_dec(bin_list)

    print(f"#{tc}", *result)
