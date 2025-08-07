import sys

sys.stdin = open('input_1210.txt')


def search(start):
    x = 99  # 아래부터 시작
    y = start  # 도착지점 인덱스부터 시작

    while x > 0:  # x가 0이 될 때까지 반복
        x -= 1

        if y > 0 and ladder[x][y - 1] == 1:  # 왼쪽이 1이라면
            while y > 0 and ladder[x][y - 1] == 1:  # 1이 끝날때까지 왼쪽으로 이동
                y -= 1
        elif y < 99 and ladder[x][y + 1] == 1:  # 오른쪽이 1이라면
            while y < 99 and ladder[x][y + 1] == 1:  # 1이 끝날때까지 오른쪽으로 이동
                y += 1
    return y


for test in range(1, 11):  # 10번 케이스 반복
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]  # 사다리 생성

    goal = 0  # 도착 지점 초기 설정

    for i in range(100):
        if ladder[99][i] == 2:  # 도착 부분 인덱스 값 찾기
            goal = i

    result = search(goal)  # x 위치 찾는 함수 호출
    print(f"#{test} {result}")
