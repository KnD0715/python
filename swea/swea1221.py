import sys

sys.stdin = open('input_1221.txt')


def sort_list(arr): # 버블 정렬 함수
    length = len(arr)

    for i in range(length - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


T = int(input())
for i in range(1, T + 1):
    ex = input().split()
    word_list = list(input().split())
    num_list = []   # 숫자를 넣을 빈 리스트 생성
    for word in word_list:
        if word == 'ZRO':
            num_list.append(0)
        elif word == 'ONE':
            num_list.append(1)
        elif word == 'TWO':
            num_list.append(2)
        elif word == 'THR':
            num_list.append(3)
        elif word == 'FOR':
            num_list.append(4)
        elif word == 'FIV':
            num_list.append(5)
        elif word == 'SIX':
            num_list.append(6)
        elif word == 'SVN':
            num_list.append(7)
        elif word == 'EGT':
            num_list.append(8)
        elif word == 'NIN':
            num_list.append(9)

    result_list = []    # 결과값을 넣을 빈 리스트 생성

    for num in sort_list(num_list):
        if num == 0:
            result_list.append('ZRO')
        elif num == 1:
            result_list.append('ONE')
        elif num == 2:
            result_list.append('TWO')
        elif num == 3:
            result_list.append('THR')
        elif num == 4:
            result_list.append('FOR')
        elif num == 5:
            result_list.append('FIV')
        elif num == 6:
            result_list.append('SIX')
        elif num == 7:
            result_list.append('SVN')
        elif num == 8:
            result_list.append('EGT')
        elif num == 9:
            result_list.append('NIN')

    print(f"#{i}", *result_list)
