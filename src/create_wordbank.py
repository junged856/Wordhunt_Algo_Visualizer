# this file is used to filter words from linux dictionary to only include lowercase and non-hyphenated words

f = open('vocabulary/collins_scrabble_words_2019.txt')
f2 = open('vocabulary/scrabble_wordbank_2019.txt', "x")

words = f.readlines()

for word in words:
    word = word.strip()
    if len(word) >= 3 and len(word) <= 16:
        f2.write(word + "\n")