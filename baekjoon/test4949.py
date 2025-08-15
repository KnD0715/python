while True:
    sentence = input()

    if sentence == '.':
        break

    stack = []
    for ch in sentence:
        if ch == '[' or ch == '(':
            stack.append(ch)
        elif ch == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(ch)
                break
        elif ch == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(ch)
                break

    if len(stack) == 0:
        print('yes')
    else:
        print('no')