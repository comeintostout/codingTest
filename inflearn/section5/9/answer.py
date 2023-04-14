import sys
from collections import deque

FILE_NAME = "1.txt"

sys.stdin = open("out"+FILE_NAME,"rt")
realAnswer = input()

sys.stdin = open("in"+FILE_NAME,"rt")

str1 = input()
str2 = input()

alphabet = dict()
for i in str1:
    if i in alphabet:
        alphabet[i] += 1
    else:
        alphabet[i] = 1

myAnswer = "YES"

for j in str2:
    if j in alphabet:
        alphabet[j] -= 1
    else:
        myAnswer = "NO"
        break

if myAnswer == "YES":
    for i in alphabet:
        if alphabet[i] != 0:
            myAnswer = "NO"

print(myAnswer == realAnswer)