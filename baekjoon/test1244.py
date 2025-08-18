import sys

def change(num):
    if num == 1:
        return 0
    else:
        return 1

length = int(sys.stdin.readline())
switch = list(map(int, sys.stdin.readline().split()))
T = int(sys.stdin.readline())
for _ in range(T):
    sex, number = map(int, sys.stdin.readline().split())

    if sex == 1:
        for i in range(number - 1, length, number):
            switch[i] = change(switch[i])

    else:
        center = number - 1
        switch[center] = change(switch[center])

        i = 1
        while 0 <= center - i < length and 0 <= center + i < length:
            if switch[center - i] == switch[center + i]:
                switch[center - i] = change(switch[center - i])
                switch[center + i] = change(switch[center + i])
                i += 1

            else:
                break

for i in range(length):
    print(switch[i], end=' ')
    if (i + 1) % 20 == 0:
        print()