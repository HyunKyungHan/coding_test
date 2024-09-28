def max_gift(friends, gifts):
    answer = 0
    friend_dict = dict()
    for i in range(len(friends)):
        friend_dict[friends[i]] = i
    
    gift_score = [[0]* len(friends) for _ in range(len(friends))] # 선물을 주고받은 내역
    gift_indices = [0]*len(friends) # 선물지수
    
    for i in gifts:
        a, b = i.split()
        sender, receiver = friend_dict[a], friend_dict[b]
        gift_score[sender][receiver] += 1
        gift_indices[sender] += 1
        gift_indices[receiver] -= 1
    
    next_gift = [0]*len(friends) # 다음 달에 받을 선물 계산
    for i in range(len(friends)):
        for j in range(len(friends)):
            if i == j:
                continue # 자기 자신을 고려할 필요 없음
            if gift_score[i][j] > gift_score[j][i]: # 준 게 더 많을 때
                next_gift[i] += 1
            elif gift_score[i][j] == gift_score[j][i]: # 주고 받은 개수가 똑같거나 한번도 안 주고받음
                if gift_indices[i] > gift_indices[j]:
                    next_gift[i] += 1
    
    answer = max(next_gift)
    return answer
            
def solution(friends, gifts):
    answer = max_gift(friends, gifts)
    return answer

if __name__ == '__main__':
    friends = ["muzi", "ryan", "frodo", "neo"]
    gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
    print(solution(friends, gifts))