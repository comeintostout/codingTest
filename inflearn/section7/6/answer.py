import sys
sys.stdin = open("in5.txt","rt")

def init():
    global letters, decoder, maxLength
    letters = input().rstrip()
    alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in range(1,27):
        decoder[str(i)]= alphabets[i-1]
    maxLength = len(letters)

def DFS(index, result):
    global letters, decoder, maxLength, cnt
    if index >= maxLength:
        print(result)
        cnt+=1
        return
    if letters[index] == '0':
        return

    DFS(index+1, result + decoder[letters[index]])
    if index+1 < maxLength and int(letters[index:index+2]) <= 26:
        DFS(index+2, result + decoder[letters[index:index+2]])

if __name__ == "__main__":
    letters = ""
    decoder = {}
    maxLength = cnt = 0 
    init()

    DFS(0,"")
    print(cnt)
    