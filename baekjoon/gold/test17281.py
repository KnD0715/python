from itertools import permutations
import sys

def play_game(player_order):
    score = 0
    p = 0

    for i in range(N):
        out = 0
        one = 0
        two = 0
        three = 0

        while out < 3:
            if inning[i][player_order[p]] == 0:
                out += 1

            elif inning[i][player_order[p]] == 1:
                score += three
                three = two
                two = one
                one = 1

            elif inning[i][player_order[p]] == 2:
                score += three + two
                three = one
                two = 1
                one = 0

            elif inning[i][player_order[p]] == 3:
                score += three + two + one
                three = 1
                two = 0
                one = 0

            elif inning[i][player_order[p]] == 4:
                score += 1 + three + two + one
                three, two, one = 0, 0, 0

            p = (p + 1) % 9

    return score

N = int(sys.stdin.readline())
inning = []
max_score = 0

for _ in range(N):
    inning.append(list(map(int, sys.stdin.readline().split())))

for player in permutations(range(1, 9), 8):
    order = list(player[:3]) + [0] + list(player[3:])
    max_score = max(max_score, play_game(order))

print(max_score)