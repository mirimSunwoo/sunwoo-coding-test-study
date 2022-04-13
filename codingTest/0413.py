def solution(x):
    answer = []
    digit = str(x)
    hasshad = 0
    hasshad = list(map(int,digit))
    if x%sum(hasshad) == 0:
        return True
    return False

#다른사람의 풀이
def Harshad(n):
    # n은 하샤드 수 인가요?
    return n % sum([int(c) for c in str(n)]) == 0