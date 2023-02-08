import sys
input = sys.stdin.readline


def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

T = int(input())
for _ in range(T):
    total = 0
    numberList = list(map(int,input().rstrip().split()))
    for i in range(1,len(numberList) - 1):
        for j in range(i+1,len(numberList)):
            total+= gcd(numberList[i], numberList[j])
    print(total)
