from concurrent.futures import process
import sys
sys.stdin = open("in5.txt","rt")

def check(songs,cap,m):
    count = 0
    localCap = 0

    for i in range(len(songs)):
        if localCap + songs[i] > cap:
            count += 1
            localCap = songs[i]
            if count >= m:
                return False
        else:
            localCap += songs[i]

    return True


[N,M] = list(map(int,input().strip().split(' ')))
songs = list(map(int,input().strip().split(' ')))

left = 0
right = ans = sum(songs)

while left < right:
    mid = (left + right) // 2
    if(check(songs,mid,M)):
        ans = mid
        right = mid
    else:
        left = mid + 1

print(ans)