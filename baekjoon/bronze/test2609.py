import sys

def GCD(num1, num2):
    min_num = min(num1, num2)
    for i in range(min_num, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i

def LCM(num1, num2):
    num_list = []
    i = 1
    while True:
        pow_num1 = num1 * i
        pow_num2 = num2 * i

        if pow_num1 not in num_list:
            num_list.append(pow_num1)
        else:
            return pow_num1

        if pow_num2 not in num_list:
            num_list.append(pow_num2)

        else:
            return pow_num2

        i += 1


num1, num2 = map(int, sys.stdin.readline().split())
GCD_num = GCD(num1, num2)
LCM_num = LCM(num1, num2)

print(GCD_num)
print(LCM_num)
