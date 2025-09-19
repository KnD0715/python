import sys

N = int(sys.stdin.readline())
mod = 1000000
cycle = (mod // 10) * 15
fibo = [0, 1]

for i in range(2, cycle):
    fibo.append((fibo[i - 1] + fibo[i - 2]) % mod)

print(fibo[N % cycle])
