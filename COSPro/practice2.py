'''
리듬체조 선수 영심 지난 1년간 대회 기록 정리중
각 대회에서 받은 점수 리스트
이 선수의 최고 점수와 최저 점수를 제외한 나머지 점수들의 합계를 구하려고 합니다
'''
def func_a(s):
    s.sort() #오름차순으로 정렬을 해준다
    return s[len(s)-1],s[0]
def func_b(s):
    ret = 0
    for i in s:
        ret += i
    return ret
def solution(scores):
    sum = func_b(scores) #합
    max, min = func_a(scores) #정렬한것에서 첫번째 min과 마지막값 max값을 구함
    return sum -max - min

scores = [100,50,30,40,60]
print(solution(scores)) #150