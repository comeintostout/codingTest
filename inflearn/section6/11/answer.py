import sys
sys.stdin = open("in5.txt","rt")

def DFS(depth,total):
    global N,M, K,array,numbers, cnt

    if depth == K:
        if total % M ==0:
            cnt+= 1
        return

    st = 0 if depth == 0 else int(array[-1]) + 1
    for i in range(st,N):
        array.append(i)
        DFS(depth+1,total+numbers[i])
        array.pop()


if __name__ == "__main__":
    N, K = map(int,input().split())
    numbers = list(map(int,input().split()))
    numbers.sort()
    M = int(input())

    array = []
    cnt = 0
    DFS(0,0)
    print(cnt)
