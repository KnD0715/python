import sys

N = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))
Max_scores = scores[0]
for i in scores:
    if i > Max_scores:
        Max_scores = i

for i in range(N):
    scores[i] = scores[i]/Max_scores * 100

sum_score = 0
for i in scores:
    sum_score += i

print (sum_score/N)