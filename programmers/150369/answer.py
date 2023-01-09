def solution(cap, n, deliveries, pickups):
    answer = 0

    delHit = pickHit = -1 
    for i in range(len(deliveries)-1,-1, -1):
        if deliveries[i] > 0:
            delHit = i
            break
    for i in range(len(pickups)-1,-1, -1):
        if pickups[i] > 0:
            pickHit = i
            break
        
    while delHit >= 0 or pickHit >= 0:
        answer += 2*(max(delHit,pickHit)+1)
        delCap = pickCap = cap

        while delHit >= 0 and delCap > 0:
            if deliveries[delHit] > delCap:
                deliveries[delHit] -= delCap
                delCap = 0
            elif deliveries[delHit] == delCap:
                deliveries[delHit] -= delCap
                delCap = 0
                delHit -= 1
            else:
                delCap -= deliveries[delHit]
                delHit -= 1
        while delHit >= 0 and deliveries[delHit] == 0:
            delHit -= 1

        while pickHit >= 0 and pickCap > 0:
            if pickups[pickHit] > pickCap:
                pickups[pickHit] -= pickCap
                pickCap = 0
            elif pickups[pickHit] == pickCap:
                pickups[pickHit] -= pickCap
                pickCap = 0
                pickHit -= 1
            else:
                pickCap -= pickups[pickHit]
                pickHit -= 1
        while pickHit >= 0 and pickups[pickHit] == 0:
            pickHit -= 1

    return answer

print(solution(	2, 2, [0, 0], [0, 0]))
