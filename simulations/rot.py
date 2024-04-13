# 행렬 전체를 시계방향으로 90도 회전
import copy

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
N = len(arr) # 정사각형 회전이니 행 길이만 구함

rot = copy.deepcopy(arr)
for r in range(N):
    for c in range(N):
        rot[c][N-1-r] = arr[r][c]

# 정답 출력
for i in range(len(rot)):
    print(rot[i])

###########################################
# 같은 문제를 zip()을 사용해 풀 수도 있다.
# 장점은 직사각형에도 똑같이 적용할 수 있다는 점.
# 단점은 메모리나 시간복잡도 면에서 불리하다.
# 시계 방향 90 (== 반시계 방향 270)
arr_90 = list(map(list, zip(*arr[::-1])))
print(arr_90)

# 시계 방향 180 (== 반시계 방향 180)
arr_180 = [a[::-1] for a in arr[::-1]]
print(arr_180)

# 시계 방향 270 (== 반시계 방향 90)
arr_270 = [x[::-1] for x in list(map(list, zip(*arr[::-1])))[::-1]]
print(arr_270)