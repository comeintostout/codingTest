import sys
sys.stdin = open("in5.txt","rt")

def init():
    global N,M,problems
    N, M = map(int,input().split())
    for i in range(N):
        score,time = map(int,input().split())
        problems.append((score,time))

    problems.sort(key=lambda x:x[0]/x[1],reverse=True)

def DFS(index, score, time):
    global N, M, maxScore, problems
    
    if time > M:
        return
    if index == N or time == M:
        maxScore = max(maxScore, score)
        return
    
    DFS(index+1, score + problems[index][0],time + problems[index][1])
    DFS(index+1, score,time)


if __name__ == "__main__":
    N = M = maxScore = 0
    problems =[]
    init()

    DFS(0,0,0)
    print(maxScore)