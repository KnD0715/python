import sys

sys.stdin = open('input_4843.txt')


def sorted_arr(arr):    # 버블정렬
    length = len(arr)   # 리스트의 길이 확인

    for i in range(length):
        for j in range(0, length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


T = int(input())
for i in range(1, T + 1):
    num = int(input())
    arr = list(map(int, input().split()))
    sort_arr = sorted_arr(arr)  # 함수를 통해 리스트 정렬
    new_arr = []    # 새로운 빈 리스트 생성
    for number in range(len(arr)): # 기존 리스트의 길이만큼 반복
        num = 0 # 값을 넣을 숫자 초기 설정
        if number % 2 == 0: # 짝수번일 때는 리스트의 큰 부분을 맨 앞으로 이동시키기 때문에
            num = arr.pop() # 뒤에 부분 pop pop pop
            new_arr.append(num) # 빈 리스트에다가 추가
        else:
            num = arr.pop(0)    # 홀수번일 때는 리스트의 작은 부분
            new_arr.append(num) # 앞에 부분 soda pop pop pop

    print(f"#{i}", *new_arr[:10]) # 10개 출력
