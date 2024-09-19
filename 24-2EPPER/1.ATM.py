# BOJ 111399
def calculate(t_list):
    t_list.sort()
    tot = 0
    for i in range(1, N+1):
        tot += sum(t_list[:i])
    return tot

if __name__ == '__main__':
    N = int(input())
    T = list(map(int, input().split()))
    print(calculate(T))