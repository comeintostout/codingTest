from concurrent.futures import process
import sys
sys.stdin = open("in1.txt","rt")


board= []
# O(1)
for i in range(9):
    board.append(list(map(int,input().split())))
    checker = [0,0,0,0,0,0,0,0,0]
    for num in board[i]:
        checker[num-1] +=1 
    if(0 in checker):
        print("NO")
        sys.exit()

# O(1)
for i in range(9):
    checker = [0,0,0,0,0,0,0,0,0]
    for j in range(9):
        checker[board[j][i]-1] += 1
    if(0 in checker):
        print("NO")
        sys.exit()

# O(1)
for i in [0,3,6]:
    checker = [0,0,0,0,0,0,0,0,0]
    for j in [0,3,6]:
        checker[board[i][j]-1] += 1
        checker[board[i][j+1]-1] += 1
        checker[board[i][j+2]-1] += 1
        checker[board[i+1][j]-1-1] += 1
        checker[board[i+1][j+1]-1] += 1
        checker[board[i+1][j+2]-1] += 1
        checker[board[i+2][j]-1] += 1
        checker[board[i+2][j+1]-1] += 1
        checker[board[i+2][j+2]-1] += 1
    if(0 in checker):
        print("NO")
        sys.exit()
print("YES")