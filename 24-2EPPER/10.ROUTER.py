import sys

n, c = map(int, sys.stdin.readline().rstrip().split())
houses = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

houses.sort()
start = 1
end = houses[-1] - houses[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    left = houses[0]
    valid = 1
    for i in range(1, n):
        if houses[i] >= left + mid:
            valid += 1
            left = houses[i]

    if valid >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
출처: https://coding-harry.tistory.com/28 [코딩해-리:티스토리]