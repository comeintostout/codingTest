import sys

FILE_NAME = "5.txt"
sys.stdin = open("in"+FILE_NAME,"rt")

def getWeightArray(N):
    result = [1]*N
    for i in range(N):
        for j in range(i):
            result[i] *= (N-j-1)
        for j in range(i):
            result[i] /= (j+1)
        result[i] = int(result[i])
    return result

def DFS(L, total):
    global N,F, array, isFinished, weightArray, checkBits
    if isFinished:
        return
    if L == N:
        if total == F:
            print(" ".join(list(map(str,array))))
            isFinished = True
        return
    
    for i in range(1,N+1):
        if checkBits[i] == 0:
            checkBits[i] = 1
            array[L] = i
            DFS(L+1,total + (array[L] * weightArray[L]))
            checkBits[i] = 0
    
if __name__ == "__main__":
    isFinished = False
    N, F = map(int,input().split())
    weightArray = getWeightArray(N)

    array = [0]*(N)
    checkBits = [0]*(N+1) 

    DFS(0,0)
