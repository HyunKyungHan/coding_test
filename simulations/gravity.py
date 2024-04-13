# 주어진 행렬에서 1이 0보다 무겁다고 할 때, 중력이 작용하면 행렬이 어떻게 바뀔지 구하기
arr = [[0, 1, 0], [1, 0, 1], [0, 1, 0], [0, 0, 1], [0, 1, 0]]

# 중력이 작용하기 전 행렬 출력
print("=====before gravity=====")
for i in range(len(arr)):
    print(arr[i])

# 중력 작용 함수
def gravity(arr):
    N = len(arr) # 행의 수
    M = len(arr[0]) # 열의 수
    for i in range(N-1): # 맨 아래 행은 어떤 조치를 할 필요가 없음.
        for j in range(M): # 열은 모두 처리해야함.
            p = i 
            while p >= 0 and arr[p][j] == 1 and arr[p+1][j] == 0:
                arr[p][j], arr[p+1][j] = arr[p+1][j], arr[p][j] # 서로 값을 바꾸기
                p -= 1 # 그리고 그 위에서 또 내려올 거 없나 확인

gravity(arr)
# 중력이 작용한 후 행렬 출력
print("=====after gravity=====")
for i in range(len(arr)):
    print(arr[i])
