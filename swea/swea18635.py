import sys

sys.stdin = open('input_18635.txt')

T = int(input())
for tc in range(1, T + 1):
    result = 0
    container, truck = map(int, input().split())
    container_weight = list(map(int, input().split()))
    truck_weight = list(map(int, input().split()))

    container_weight.sort()
    container_weight.reverse()

    truck_weight.sort()
    truck_weight.reverse()

    for move_container in container_weight:
        for i in range(len(truck_weight)):
            if move_container <= truck_weight[i]:
                truck_weight.pop(i)
                result += move_container
                break

    print(f"#{tc} {result}")
