T = int(input())

for _ in range(T):
    stack = []
    word = input()

    result = 'YES'

    for i in word:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                result = 'NO'
                break

    if len(stack) != 0:
        result = 'NO'

    print(result)