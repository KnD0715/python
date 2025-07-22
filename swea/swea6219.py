N = int(input())
my_list = []

for i in range (1, N + 1):
    if (N % i == 0):
        print ("%d(은)는 %d의 약수입니다." % (i, N))
        my_list += str(i)

if (len(my_list) == 2):
    print (f"{N}(은)는 {my_list[0]}과 {my_list[1]}로만 나눌 수 있는 소수입니다.")