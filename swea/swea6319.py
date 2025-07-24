word = input()
word_list = []
for char in word:
    word_list += [char]

reversed_list = list(reversed(word_list))

if word_list == reversed_list:
    print (word)
    print("입력하신 단어는 회문(Palindrome)입니다.")