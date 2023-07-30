import sys
sys.stdin = open("in5.txt","rt")

def init():
    global N,M,weights
    N = int(input())
    weights =list(map(int,input().split()))

def DFS(index, w):
    global N, vaildWeights, weights
    
    if index >= N:
        if w > 0:
            vaildWeights.add(w)
        return
    
    DFS(index+1, w + weights[index])
    DFS(index+1, w)
    DFS(index+1, w - weights[index])


if __name__ == "__main__":
    N = 0
    weights = []
    vaildWeights = set()
    init()

    DFS(0,0)

    print(sum(weights) - len(vaildWeights))


    