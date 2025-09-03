import sys

sys.stdin = open('input_18613.txt')


def hex_to_bin(num):
    hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    hex_num = hex.index(num)

    bin = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100',
           '1101',
           '1110', '1111']

    return bin[hex_num]


def password_bit(num):
    bit_pattern = ['001101', '010011', '111011', '110001', '100011', '110111', '001011', '111101', '011001', '101111']
    return bit_pattern.index(num)


T = int(input())
for tc in range(1, T + 1):
    password = list(input().strip())

    code = ''
    for i in password:
        code += hex_to_bin(i)

    code = list(code)
    code.reverse()

    count = 0
    for i in range(len(code)):
        if code[i] == '0':
            count += 1

        else:
            break

    for i in range(count):
        code.pop(0)
        code.pop()

    code.reverse()

    code_word = 0
    check_password = ''
    result = []
    for i in range(len(code)):
        check_password += code[i]
        code_word += 1

        if code_word == 6:
            result.append(password_bit(check_password))
            code_word = 0
            check_password = ''

    print(f"#{tc}", *result)
