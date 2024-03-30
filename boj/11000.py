# (중) 강의실 배정
import heapq as hq 

# 1. 내 시작 시간이 이전 애의 종료 시간 이후인가? -> 이러면 강의실을 새로 배정할 필요가 없음.
# 2. 강의실 수 == 동시에 진행되어야만 하는 강의의 수
def solution(lectures):
    lectures.sort() # 오름차순으로 정렬
    pq = [-1] # priority queue를 구현해둔 리스트의 첫 원소를 -1로 지정, 그래야 맨 처음 강의실을 배정할 수 있게 됨

    for start, end in lectures:
        if pq[0] <= start:
            hq.heappop(pq) # 강의실을 배정할 수 있으면 큐에서 뺸다.
        hq.heappush(pq, end) # 배정할 수 없으면 끝나는 시간을 큐에 넣는다. 알아서 min heap안에서 오름차순 정렬될거임.

    return len(pq)