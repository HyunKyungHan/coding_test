# (하) 행운의 바퀴
def solution(n, record):
    wheel = ['?'] * n
    is_available = dict() # 같은 알파벳을 두 번 사용할 수 없음!!!
    
    ord_a = ord('A')
    for i in range(26):
        is_available[chr(i+ord_a)] = True

    idx = 0
    for i in range(len(record)):
        idx = (idx - int(record[i][0])) % n ##### wheel 범위 내의 인덱스로 조정 #####
        if wheel[idx] == record[i][1]:
            continue
        if wheel[idx] != '?' or not is_available[record[i][1]]:
                return "!"
        wheel[idx] = record[i][1]
        is_available[record[i][1]] = False
    return ''.join(wheel[idx:]+wheel[:idx])

n, k = map(int, input().split())
record = [input().split() for _ in range(k)]
    
print(solution(n, record))