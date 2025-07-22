N = int(input())

for i in range (1, N + 1):
    if (N % i == 0):
        print("%d(은)는 %d의 약수입니다." % (i, N))