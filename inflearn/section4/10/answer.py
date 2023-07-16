import sys
sys.stdin = open("in5.txt","rt")

N = int(input())
reversedNumbers = list(map(int,input().split()))
Numbers = [0]*(N+1)

for num in range(1,N+1):
    biggerNumbers = reversedNumbers[num-1]
    idx = 1
    count = 0
    while count < biggerNumbers and idx <= N:
        if Numbers[idx] == 0 or Numbers[idx] > num:
            count+=1
        idx+=1
    while Numbers[idx] > 0 and idx <= N:
        idx+= 1
    Numbers[idx] = num
print(Numbers[1:])
