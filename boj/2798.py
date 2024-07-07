n, m = map(int, input().split())
card = list(map(int, input().split()))

largest = 0
for i in range(len(card)):
    for j in range(i+1, len(card)):
        for k in range(j+1, len(card)):
            if m < card[i] + card[j] + card[k]: # 카드의 합이 m을 넘으면 못씀
                continue
            else: # m보다 작은 카드의 합 중 가장 큰 걸 찾고 싶은 것.
                largest = max(largest, card[i] + card[j] + card[k])
                
print(largest)
