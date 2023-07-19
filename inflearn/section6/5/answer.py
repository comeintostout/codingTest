import sys

FILE_NAME = "4.txt"
sys.stdin = open("in"+FILE_NAME,"rt")

def DFS(accSum, idx):
    if accSum > limit:
        return 0
    elif idx == len(weights):
        return accSum
    else:
        return max(accSum, DFS(accSum + weights[idx],idx+1), DFS(accSum,idx+1))


if __name__ == "__main__":
    limit,n = map(int,input().split())
    weights = []
    for i in range(n):
        weights.append(int(input()))

    if sum(weights) <= limit:
        print(sum(weights))
    else:
        print(DFS(0, 0))