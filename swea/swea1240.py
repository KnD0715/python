import sys

sys.stdin = open('input_1240.txt')


def check_password(num):
    password = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111',
                '0001011']

    return password.index(num)

def pass_code(num):
    return ((num[0] + num[2] + num[4] + num[6]) * 3) + (num[1] + num[3] + num[5] + num[7])

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    password = [list(map(int, input().strip())) for _ in range(N)]

    for row in range(N):
        if 1 in password[row]:
            check_row = row
            break

    result = []
    check_list = ''
    count = 0

    for i in reversed(password[check_row]):
        if i == 0:
            password[check_row].pop()

        else:
            break

    for i in reversed(password[check_row]):
        check_list += str(i)
        count += 1

        if count == 7:
            result.append(''.join(reversed(check_list)))
            check_list = ''
            count = 0

    if check_list:
        result.append(''.join(reversed(check_list)))

    result.reverse()

    num_list = []
    for pw in result:
        check = 0
        if '1' not in pw:
            continue
        else:
            check = check_password(pw)
            num_list.append(check)

    code = pass_code(num_list)

    if code % 10 != 0:
        print(f"#{tc} 0")

    else:
        print(f"#{tc} {sum(num_list)}")
