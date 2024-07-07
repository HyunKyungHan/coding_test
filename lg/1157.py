if __name__ == '__main__':
    input = input().lower()
    alphabets = list(set(input))
    cnt = []
    for i in alphabets: # 단어에 등장하는 알파벳들을 중복 없이 셈.
        cnt.append(input.count(i)) # count()는 string에서 바로 사용 가능.
    if cnt.count(max(cnt)) >= 2:
        print("?")
    else:
        print(alphabets[cnt.index(max(cnt))].upper())