import sys

sys.stdin = open('input_18530.txt')

T = int(input())
for tc in range(1, T + 1):
    number = float(input())

    result = []

    while number != 1 and len(result) <= 12:
        number *= 2
        if number > 1:
            result.append(1)
            number -= 1

        elif number == 1:
            result.append(1)
            break

        else:
            result.append(0)

    if len(result) > 12:
        print(f"#{tc} overflow")

    else:
        print(f"#{tc}", ''.join(map(str, result)))
