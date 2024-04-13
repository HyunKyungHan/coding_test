# 행렬의 일부만을 시계방향으로 90도 회전하기
import copy
arr = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
rot = copy.deepcopy(arr)
sx, sy = 1, 1 # 회전할 부분행렬의 lt 좌표
length = 3 # 회전할 부분행렬의 크기 (정사각형 행렬이라고 가정함.)

def parital_rot(arr, rot, sx, sy, length):
    for r in range(sx, sx + length):
        for c in range(sy, sy + length):
            # STEP 1. 좌표를 원점(0,0) 기준으로 이동한다.
            mr = r - sx # mr = moved r
            mc = c - sy
            # STEP 2. 시계방향으로 90도 회전했을 때의 '좌표'를 구한다.
            rr = mc
            rc = length - 1 - mr
            # STEP 3. 다시 sx, sy를 더한 위치에 간 후 행렬 값을 입력받음.
            rot[rr+sx][rc+sy] = arr[r][c]

    # 이제 원래 배열에 회전한 부분배열 값을 적용해줌.
    for r in range(sx, sx + length):
        for c in range(sy, sy + length):
            arr[r][c] = rot[r][c]


# 결과 출력
parital_rot(arr, rot, sx, sy, length)
for i in range(len(arr)):
    print(arr[i])
