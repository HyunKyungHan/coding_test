# 15686. 치킨배달
from itertools import combinations

def chicken_dist(c_coord, h_coord): # 치킨집과 집의 좌표를 받았을 때 치킨거리를 계산.
    dist = abs(c_coord[0] - h_coord[0]) + abs(c_coord[1] - h_coord[1])
    return dist 

def solution():
    home_place = [(i, j) for i in range(N) for j in range(N) if city[i][j] == '1']     
    answer = [] # 각 combination에 대한 도시의 치킨거리
    for comb in combinations(chicken_place, M): # combinations라는 좋은 것이 있다...
        whole = 0
        for h in home_place:
            one = 9999 # 충분히 큰 값으로 초기화
            for chicken in comb:  # 하나의 집을 기준으로 구하는 치킨거리
                temp = chicken_dist(chicken,h)
                one = min(temp, one)
            whole += one # 하나의 치킨집에 대한 모든 집의 치킨거리의 합
        answer.append(whole) # combination 별 도시의 치킨거리 비교를 위해 answer 리스트에 추가
    return(min(answer))


if __name__ == '__main__':
    N, M= map(int, input().split())
    city = [0*N for _ in range(N)] # NxN matrix
    for i in range(N):
        city[i] = list(input().split())
    chicken_place = [(i, j) for i in range(N) for j in range(N) if city[i][j] == '2']
    print(solution())
    