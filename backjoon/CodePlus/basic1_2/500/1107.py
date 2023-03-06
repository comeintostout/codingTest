N = int(input())
M = int(input())
brokenButtons =[]
unBrokenButtons = []

def makeNumberList(numberList,unBrokenButtons ,digit):
    maxIdx = len(unBrokenButtons)
    
    idxList = [0] * digit
    while True:
        number = 0
        for i in idxList:
            number *= 10
            number += unBrokenButtons[i]
        numberList.append(number)
        idxList[-1] += 1
        for i in range(len(idxList)-1,0,-1):
            if idxList[i] >= maxIdx:
                idxList[i-1] += 1
                idxList[i] = 0
            else:
                break
        if idxList[0] == maxIdx:
            break

if M > 0:
    brokenButtons = list(map(int,input().rstrip().split())) 

if N == 100:
    print(0)
else:
    answer = len(str(N))
    if M == 0:
        print(min(answer, abs(N-100)))
    elif M >= 10:
        print(min(answer + abs(N - 100), abs(N - 100)))
    else:
        for i in range(10):
            if i not in brokenButtons:
                unBrokenButtons.append(i)
        numberList = []
        if answer > 1:
            makeNumberList(numberList, unBrokenButtons,answer-1)
        makeNumberList(numberList, unBrokenButtons,answer)
        makeNumberList(numberList, unBrokenButtons,answer+1)
        result = list(map(lambda x: abs(N-x),numberList))
        minRes = min(result)
        i = 0
        for i in range(len(result)):
            if minRes == result[i]:
                break

        print(min(min(result) + len(str(numberList[i])), abs(N - 100)))