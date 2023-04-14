import sys

FILE_NAME = "5.txt"

sys.stdin = open("out"+FILE_NAME,"rt")
realAnswer = input()

sys.stdin = open("in"+FILE_NAME,"rt")



# print(myAnswer == realAnswer)