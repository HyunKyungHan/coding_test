# BOJ 19941
# 어떤 사람의 위치로부터 절댓값 K만큼 차이나는 곳에 햄버거가 위치하는지 확인하면 된다.
# 처음에 절댓값 크기가 큰 순서(예를들어 -2, +2 -> -1, +1)대로 탐색을 해야할 것이라고 생각했는데, 
# 그러면 + 방향 쪽의 다른 사람이 먹을 수도 있는 햄버거를 선점해버리는 오류가 생김.
# 결론적으로 그냥 왼쪽부터 오른쪽 방향으로 1씩 키워가며 탐색하면 된다.

def check_hamburger(idx, i_list, N, K):
    for k in range(idx - K, idx + K + 1):
        if k < 0 or k >= N:
            continue
        else:
            if i_list[k] == 'H':
                i_list[k] = 'X'  # Hamburger eaten
                return 1
    return 0

if __name__ == '__main__':
    N, K = map(int, input().split())
    i_list = list(input())
    cnt = 0
    for i in range(len(i_list)):
        if i_list[i] == 'P':
            cnt += check_hamburger(i, i_list, N, K)
    print(cnt)