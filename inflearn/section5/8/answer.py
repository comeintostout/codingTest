import sys

FILE_NAME = "5.txt"

sys.stdin = open("out"+FILE_NAME,"rt")
realAnswer = input()

sys.stdin = open("in"+FILE_NAME,"rt")

N = int(input())
words= dict()

for i in range(N):
    words[input()] = 0

for i in range(N-1):
    words[input()] = 1

for key in words:
    if words[key] == 0:
        print(key)
        myAnswer = key
        break

print(myAnswer == realAnswer)