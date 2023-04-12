import sys

FILE_NAME = "1.txt"
sys.stdin = open("in"+FILE_NAME,"rt")

number, m = input().split()
m = int(m)

sys.stdin = open("out"+FILE_NAME,"rt")
realAnswer = input()

def getBiggestNumber(number, m):
    if m == 0:
        return number
    if len(number) == m:
        return ""
    pickableIdx = m

    largestNumber = largestNumberIdx = -1

    for i in range(pickableIdx+1):
        if largestNumber < int(number[i]):
            largestNumber = int(number[i])
            largestNumberIdx = i

    return str(largestNumber) + getBiggestNumber(number[largestNumberIdx+1:],m - largestNumberIdx)

myAnswer = getBiggestNumber(number,m)

print(myAnswer == realAnswer)

