import sys

sys.stdin = open('input_5215.txt')

def sequence(num, score, total):
    global max_score
    if total <= L:
        if max_score < score:
            max_score = score

    if total >= L:
        return

    for i in range(num, N):
        sequence(i + 1, score + material[i][0], total + material[i][1])


T = int(input())
for tc in range(1, T + 1):
    N, L = map(int, input().split())
    material = []
    for _ in range(N):
        material_score, calorie = map(int, input().split())
        material.append([material_score, calorie])

    max_score = 0
    sequence(0, 0, 0)

    print(f"#{tc} {max_score}")
