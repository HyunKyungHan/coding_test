def solution(s):
    answer = 0
    stack = []

    for i in range(len(s)):
        if s[i] == '(':
            stack.append("(")
        else: # 닫는 괄호인 경우
            stack.pop()

            if s[i-1] == '(': # 이전 괄호가 여는 것이면 레이저라는 뜻이므로
                answer += len(stack)

            else:
                answer += 1
    return answer

if __name__ == "__main__":
    s = input()
    answer = solution(s)
    print(answer)