import sys
sys.stdin = open("in5.txt","rt")

def init():
    global N,M,Councils
    N = int(input())
    for i in range(N):
        time,pay = map(int,input().split())
        Councils.append((time,pay))

def DFS(index, pay):
    global N, maxPay, Councils
    
    if index >= N or index + Councils[index][0] > N:
        maxPay = max(maxPay, pay)
        return
    
    DFS(index+Councils[index][0],pay + Councils[index][1])
    DFS(index+1, pay)


if __name__ == "__main__":
    N = maxPay = 0
    Councils =[]
    init()
    
    DFS(0,0)
    print(maxPay)