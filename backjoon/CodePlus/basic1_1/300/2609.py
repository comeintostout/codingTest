[A, B] = map(int,input().rstrip().split())

minAB = min(A,B)
maxAB = max(A,B)

commonSmall = 1
for i in range(minAB,0,-1):
    if A%i == 0 and B % i ==0:
        commonSmall = i
        break
print(commonSmall)

commonBig = minAB
while True:
    if commonBig%A ==0 and commonBig%B == 0 and commonBig >= maxAB:
        break
    commonBig += minAB
print(commonBig)