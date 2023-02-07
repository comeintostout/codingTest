import math

[A, B] = map(int,input().rstrip().split())
sosus = [True] * (B+1)
sosus[0] = sosus[1] = False
    
def getNextKey(prevKey):
    for i in range(prevKey+1,B+1):
        if sosus[i] == True:
            return i
    return -1
prevKey = 1
while True:
    key = getNextKey(prevKey)
    if key == -1:
        break
    prevKey = key
    key += key
    while key <= B:
        sosus[key] = False
        key += prevKey

for i in range(A,B+1):
    if sosus[i] == True:
        print(i)