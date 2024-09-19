def get_doll(board, i_move):
    i_move -= 1 # list index와 일치시키기
    for i in range(N):
        if board[i][i_move] == 0:
            continue
        else:
            doll = board[i][i_move]
            board[i][i_move] = 0
            return doll
    return None

def solution(board, moves):
    answer = 0 # 터뜨려진 인형 수
    global N 
    N = len(board[0]) # 세로 줄의 크기
    global i_board
    i_board = board
    basket = [0]
    for move in moves: # moves 배열 안의 명령을 하나씩 실행
        this_doll = get_doll(i_board, move)
        if this_doll == None: # 크레인을 내린 자리에 아무 인형도 없는 경우
            continue
        else: # 크레인을 내린 자리에 인형이 있는 경우
            if this_doll == basket[-1]: # 어떤 인형인지 확인, basket의 인형과 일치하면 
                answer += 2 # answer 증가
                basket = basket[:-1]
            else:
                basket.append(this_doll) # 이번 인형을 basket값으로 업데이트
    return answer

if __name__ == '__main__':
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]
    print(solution(board, moves))