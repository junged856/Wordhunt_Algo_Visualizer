# this file is used to filter words from linux dictionary to only include lowercase and non-hyphenated words

f = open('linuxwords.txt')
f2 = open('wordbank.txt', "x")

words = f.readlines()

for word in words:
    word = word.strip()
    if len(word) >= 3 and len(word) <= 16:
        print(word.islower() and word.isalpha())
        if word.islower() and word.isalpha():
            f2.write(word + "\n")