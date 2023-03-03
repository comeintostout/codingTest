[E,S,M] = map(int,input().rstrip().split())

COEF = [15,28,19]
NEXT = [15,28,19]
XYZ = [0,0,0]

while True:
    if (COEF[0]*XYZ[0] + E == COEF[1]*XYZ[1] + S) and (COEF[1]*XYZ[1] + S == COEF[2]*XYZ[2] + M):
        print(COEF[0]*XYZ[0] + E)
        break
    minVal = min(NEXT)
    idx=0
    for i in range(3):
        if NEXT[i] == minVal:
            idx = i
    XYZ[idx] += 1
    NEXT[idx] += COEF[idx]