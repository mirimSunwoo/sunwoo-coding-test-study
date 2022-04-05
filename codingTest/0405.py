def solution(n):
    answer = 0 #정답을 return할 변수를 초기화 시켜준다
    for x in range(n,1,-1): #n부터 1까지 1씩 빼면서 반복한다
        if n%x == 1: #그중 n을 나누었을때 나머지가 1인 것을
            answer = x #answer에 대입시킨다(만약 답이 2개가 나와도 나중에 나온 답을 최종적으로 저장한다)
    return answer