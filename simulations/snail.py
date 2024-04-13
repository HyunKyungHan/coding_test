arr = [[0]*5 for _ in range(5)]

def tornado():
    d = [(-1, 0), (0, -1), (1, 0), (0, 1)] # 좌 하 우 상 순서로 이동
    d_idx = 0
    dist = 1
    num = 0
    move_count = 0 # (1,1,2,2,3,3,4,4,...) 크기로 이동하기 때문에 move_count == 2 이면 dist += 1 해야함.
    x = len(arr) // 2 # 시작 위치
    y = len(arr) // 2

    while True:
        for _ in range(dist): # 한 칸씩 움직이되, dist번 반복해서 움직임.
            dx, dy = d[d_idx] # x,y 좌표 변화량
            nx = x + dx
            ny = y + dy
            
            if (nx, ny) == (-1,0): # 좌표의 좌상단에 도착하면 종료하는 조건이라고 가정하자.
                return
            
            num += 1
            arr[y][x] = num
            x = nx
            y = ny # 좌표 업데이트
            
        move_count += 1 # 움직인 거리 업데이트
        d_idx = (d_idx + 1) % 4 # 회전 인덱스 업데이트

        if move_count == 2: # 이동거리를 바꿔야 할 시간!
            dist += 1
            move_count = 0
    
tornado()
for i in range(len(arr)):
    print(arr[i])