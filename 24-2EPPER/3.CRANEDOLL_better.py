def get_doll(board, moves):
    stacklist = []
    answer = 0
    
    for i in moves: # 크레인 좌표들을 하나씩 iterate
        for j in range(len(board)): # 행의 수
            if board[j][i-1] != 0: # 열을 고정, 행을 하나씩 아래로 움직이면서 탐색
                stacklist.append(board[j][i-1]) # 비어있지 않다면 stacklist에 추가
                board[j][i-1] = 0
                
                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2
                break
    return answer

def solution(board, moves):
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]
    ans = 0
    ans = get_doll(board, moves)
    return ans