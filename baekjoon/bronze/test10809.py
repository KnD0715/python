import sys

word = sys.stdin.readline().rstrip()
for alpha in 'abcdefghijklmnopqrstuvwxyz':
    print(word.find(alpha), end=' ')