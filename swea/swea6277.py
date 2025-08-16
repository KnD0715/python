num_list = []

for _ in range(5):
    num = int(input())
    num_list.append(num)

avg = sum(num_list) / 5

print(f"입력된 값 {num_list}의 평균은 {avg}입니다.")