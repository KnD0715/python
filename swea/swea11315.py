T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    omok = [list(input()) for _ in range(N)]

    result = 'NO'
    for row in range(N):
        count = 0
        for column in range(N):
            if omok[row][column] == 'o':
                count += 1
                if count >= 5:
                    result = 'YES'
                    break

            else:
                count = 0

        if result == 'YES':
            break

    if result == 'NO':
        for column in range(N):
            count = 0
            for row in range(N):
                if omok[row][column] == 'o':
                    count += 1
                    if count >= 5:
                        result = 'YES'
                        break

                else:
                    count = 0

            if result == 'YES':
                break

    if result == 'NO':
        for row in range(N):
            for column in range(N):
                count_diagonal = 0
                if omok[row][column] == 'o':
                    for num in range(5):
                        if 0 <= row + num < N and 0 <= column + num < N:
                            if omok[row + num][column + num] == 'o':
                                count_diagonal += 1

                            else:
                                break
                        if count_diagonal >= 5:
                            result = 'YES'
                            break
                    if result == 'YES':
                        break
    if result == 'NO':
        for row in range(N):
            for column in range(N):
                count_diagonal = 0
                if omok[row][column] == 'o':
                    for num in range(5):
                        if 0 <= row + num < N and 0 <= column - num < N:
                            if omok[row + num][column - num] == 'o':
                                count_diagonal += 1

                            else:
                                break
                        if count_diagonal >= 5:
                            result = 'YES'
                            break
                    if result == 'YES':
                        break

    print(f"#{tc} {result}")
