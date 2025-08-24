import sys

T = int(sys.stdin.readline())

for _ in range(T):
    count = 0
    result = 0

    ox_sentence = sys.stdin.readline().strip()

    for ox in ox_sentence:
        if ox == 'O':
            count += 1
            result += count
        else:
            count = 0

    print(result)