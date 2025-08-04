import sys

word = sys.stdin.readline().strip()
reversed_word = word[::-1]

if word == reversed_word:
    print (1)
else:
    print (0)