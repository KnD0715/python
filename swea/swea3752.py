import sys

sys.stdin = open('input_3752.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))
    answer = [0]

    for score in num_list:
        answer = list(set(answer))
        for i in range(len(answer)):
            answer.append(answer[i] + score)

    print(f"#{tc} {len(set(answer))}")
