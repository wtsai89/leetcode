from cs50 import *

text = get_string("Text: ")

letters = 0
words = 0
sentences = 0
for i in range(len(text)):
    c = text[i]
    if c.isalpha():
        letters += 1
    if c != " " and (i == len(text)-1 or text[i+1] == " "):
        words += 1
    if (c == "." or c == "!" or c == "?") and (i == len(text)-1 or text[i+1] == " "):
        sentences += 1
index = 0.0588 * (letters/words*100) - 0.296 * (sentences/words*100) - 15.8
if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {round(index)}")