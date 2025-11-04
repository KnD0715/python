import sys

N = int(sys.stdin.readline())
word_list = []
for _ in range(N):
    word = sys.stdin.readline().strip()
    if word in word_list:
        continue
    else:
        word_list.append(word)

word_list.sort(key=lambda x:(len(x), x))

for word in word_list:
    print(word)