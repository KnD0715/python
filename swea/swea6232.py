word = input()
reverse_word = word[::-1]

print(word)
if word == reverse_word:
    print("입력하신 단어는 회문(Palindrome)입니다.")