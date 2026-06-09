#make array of misspelt and another array of correctly spelt words and have the words have corresponding index value
import random

with open("words.txt", "r", encoding="utf-8") as file:
    words = [line.split() for line in file if line.strip()]

print (words [random.randint(0,2)][random.randint(0,1)])
print(len(words))

