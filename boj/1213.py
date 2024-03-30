# (하) 팰린드롬 문제
from collections import Counter

def make_palindrome(text):
    part1 = "" # 반복되는 덩어리들
    part2 = "" # 중간 한자리(홀수 개 val이 존재하는 경우)

    text_dict = sorted(Counter(text).items())
    for key, val in text_dict:
        if val % 2 == 1: # 홀수 개의 알파벳이 있다면
            if len(part2) == 0:
                part2 += key
            else:
                return "I'm Sorry Hansoo"
        part1 += key * (val//2)
    name = part1 + part2 + part1[::-1]

    return name


if __name__ == "__main__":
    # 입력
    text = input()
    print(make_palindrome(text))