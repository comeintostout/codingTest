import sys

FILE_NAME = "5.txt"
sys.stdin = open("in"+FILE_NAME,"rt")

def DFS(Nums, i, currSum , total):
    if currSum == total:
        return 1
    if currSum > total:
        return 0
    else:
        if i < len(Nums)-1:
            return DFS(Nums, i+1, currSum + Nums[i], total) + DFS(Nums, i+1,currSum, total)
        else:
            return 0

if __name__ == "__main__":
    n = int(input())
    Nums = list(map(int,input().split()))
    total = sum(Nums)
    if total%2 == 1:
        print("NO")
    else:
        if DFS(Nums,0, 0, total//2) > 0:
            print("YES")
        else:
            print("NO")