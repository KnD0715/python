import sys

sys.stdin = open('input_20551.txt')

T = int(input())
for tc in range(1, T + 1):
    A, B, C = map(int, input().split())
    count = 0

    while B >= C and B > 1:
        B -= 1
        count += 1

    while A >= B and A > 1:
        A -= 1
        count += 1

    if A == B or B == C:
        count = -1

    print(f"#{tc} {count}")
