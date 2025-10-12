import sys

word = list(sys.stdin.readline().strip())

word_count = [0] * 26

for ch in word:
    word_count[ord(ch.upper()) - 65] += 1

max_count = max(word_count)

if word_count.count(max_count) >= 2:
    print('?')

else:
    idx = word_count.index(max_count)
    print(chr(idx + 65))
