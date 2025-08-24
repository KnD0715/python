import sys

total = 0
total_list = []
for _ in range(10):
    score = int(sys.stdin.readline())
    total_list.append(score)

my_list = [0]
for num in total_list:
    total += num

    if total >= 100:
        prev_num = my_list.pop()
        plus_num = total - 100
        minus_num = 100 - prev_num

        if plus_num == minus_num:
            print(total)
            break

        elif plus_num > minus_num:
            print(prev_num)
            break

        elif plus_num < minus_num:
            print(total)
            break

    else:
        my_list.append(total)

else:
    print(my_list[-1])
