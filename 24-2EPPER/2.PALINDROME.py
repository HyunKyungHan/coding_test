# BOJ 1213
def check_failure(o_list):
    if len(o_list) > 1:
        return True
    else:
        return False

if __name__ =='__main__':
    name = input()
    count = dict()
    result = ''
    keys = sorted(list(set(name))) # set: 등장하는 알파벳을 추출, sorted: 알파벳 순서대로 정렬 => 얘네를 key로써 사용.
    odd = []
    for key in keys:
        cnt = name.count(key) # 입력받은 문자열에서 key의 개수를 세서 저장함. 
        count[key] = cnt # 이제 key-cnt 쌍을 가지게 됨.
        if cnt % 2:
            odd.append(key)

    if check_failure(odd):
        print("I'm Sorry Hansoo")
    else:
        for key in keys:
            result += key * (count[key] // 2)
        if odd: # odd 리스트에 하나라도 들어있으면
            result += odd[0] + result[::-1]
        else:
            result += result[::-1]

        print(result)