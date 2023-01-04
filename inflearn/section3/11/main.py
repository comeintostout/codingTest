from concurrent.futures import process
import sys
sys.stdin = open("in3.txt","rt")

board = []
for row in range(0,7):
    board.append(list(map(int,input().strip().split(' '))))


def checkPalindrum(list):
    if(list[0] == list[4] and list[1] == list[3]):
        return 1
    return 0

count = 0
for row in range(0,7):
    for col in range(0,7):
        if(row < 3):
            count += checkPalindrum([board[k][col] for k in range(row,5+row)])
        if(col < 3):
            count += checkPalindrum([board[row][k] for k in range(col,5+col)])

print(count)