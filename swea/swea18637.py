import sys

sys.stdin = open('input_18637.txt')

T = int(input())
for tc in range(1, T + 1):
    player_1 = [0] * 10
    player_2 = [0] * 10

    result = 0
    achieve_1 = 0
    achieve_2 = 0
    num_list = list(map(int, input().split()))

    for i in range(6):
        player_1[num_list[i * 2]] += 1

        achieve_1 = 0
        for check_triplet_1 in range(10):
            if player_1[check_triplet_1] >= 3:
                achieve_1 = 1
                break
        if not achieve_1:
            for check_run_1 in range(8):
                if player_1[check_run_1] and player_1[check_run_1 + 1] and player_1[check_run_1 + 2]:
                    achieve_1 = 1
                    break

        if achieve_1:
            result = 1
            break

        player_2[num_list[i * 2 + 1]] += 1

        achieve_2 = 0
        for check_triplet_2 in range(10):
            if player_2[check_triplet_2] >= 3:
                achieve_2 = 1
                break
        if not achieve_2:
            for check_run_2 in range(8):
                if player_2[check_run_2] and player_2[check_run_2 + 1] and player_2[check_run_2 + 2]:
                    achieve_2 = 1
                    break

        if achieve_2:
            result = 2
            break

    print(f"#{tc} {result}")
