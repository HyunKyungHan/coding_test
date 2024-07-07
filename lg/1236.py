# IDEA) 행 기준으로 필요한 경호원의 수, 열 기준으로 필요한 경호원의 수를 각각 세면, 하나의 경호원만으로 1개의 행과 1개의 열을 보호할 수 있는 경우의 수 만큼을 중복하여 세게 된다.
# 중복하지 않고 세려면 어떻게 해야할까? 이 방법을 떠올리는 게 핵심이었을 것.
# ==> 행과 열 기준으로 counting 했을 때, 더 큰 값만큼만 취하면 된다.
if __name__ == '__main__':
    n, m = map(int, input().split())
    input = [list(input().rstrip()) for _ in range(n)]
    row = 0
    col = 0
    for i in range(n): # 행 기준
        if 'X' not in input[i]:
            row += 1

    for j in range(m): # 열 기준
        if "X" not in [input[i][j] for i in range(n)]:
            col += 1

    print(max(row, col))