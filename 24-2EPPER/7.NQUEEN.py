def backtracking(i, n, columns, diag_up, diag_down):
    if i == n:
        return 1
    
    answers = 0
    for col in range(n):
        if columns[col] or diag_up[i+col] or diag_down[i-col+n-1]:
            continue
            
        columns[col] = True
        diag_up[i+col] = True
        diag_down[i-col+n-1] = True
        
        answers += backtracking(i+1, n, columns, diag_up, diag_down)
        
        columns[col] = False
        diag_up[i+col] = False
        diag_down[i-col+n-1] = False
        
    return answers
        
def solution(n):
    columns = [False]*n
    diag_up = [False]*(2*n - 1)
    diag_down = [False]*(2*n - 1)
    answer = backtracking(0, n, columns, diag_up, diag_down)
    return answer