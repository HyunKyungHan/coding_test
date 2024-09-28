def dp(n, m, board):
    dp = [[0]*(m+1) for _ in range(n+1)]
    ans = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if board[i-1][j-1]: # board 값이 1인 경우만 탐색하면 됨.
                dp[i][j] = min(min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]) + 1 # 핵심 점화식. 왼, 위, 대각선 위 좌표들이 만드는 사각형 크기 중 가장 작은 것을 선택. 1 더해주는 것 잊지 말기!!
            ans = max(ans, dp[i][j])
    return ans

def solution(board):
    r = 0
    n = len(board)
    m = len(board[0])
    r = dp(n, m, board) # 정사각형 한 변의 길이를 저장함.
    answer = r*r
    return answer