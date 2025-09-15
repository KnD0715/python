import sys

pay = int(sys.stdin.readline())
count = 0
change = 1000 - pay
while change > 0:
    if change >= 500:
        change -= 500
        count += 1

    elif 100 <= change < 500:
        while change >= 100:
            change -= 100
            count += 1

    elif 50 <= change < 100:
        while change >= 50:
            change -= 50
            count += 1

    elif 10 <= change < 50:
        while change >= 10:
            change -= 10
            count += 1

    elif 5 <= change < 10:
        while change >= 5:
            change -= 5
            count += 1

    else:
        while change > 0:
            change -= 1
            count += 1

print(count)