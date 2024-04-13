# arr = [1, 2, 3, 4]
# visited = [0] * len(arr)  # visited도 전역으로 둬도 됨


# def permutations(n, new_arr):
#     global arr
#     # 순서 상관 0, 중복 X
#     if len(new_arr) == n:
#         print(new_arr)
#         return
#     for i in range(len(arr)):
#         if not visited[i]:
#             visited[i] = 1
#             permutations(n, new_arr + [arr[i]])
#             visited[i] = 0


# permutations(2, [])