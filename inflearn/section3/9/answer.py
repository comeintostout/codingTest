import sys
sys.stdin = open("in5.txt","rt")

n = int(input())

# O(n)
board = []
for row in range(n+2):
    if(row == 0 or row == n+1):
        board.append([0 for col in range(n+2)])
    else:
        boardRow = list(map(int,input().split()))
        boardRow.insert(0,0)
        boardRow.append(0)
        board.append(boardRow)

# O(n*n)
count = 0
for row in range(1,n+1):
    for col in range(1,n+1):
        if(board[row][col] > board[row-1][col] and board[row][col] > board[row+1][col] and board[row][col] > board[row][col-1] and board[row][col] > board[row][col+1]):
            count += 1

print(count)