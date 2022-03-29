def solution(x, n):
    answer = [] #리스트를 선언한다
    up = x #up이라는 변수에 x부터 시작하기 위해 x를 초기값으로 선언한다
    # count = 0 #loop를 몇번 도는지 체크하는 변수
    for _ in range(n): #n만큼 loop를 돌린다
        # count += 1
        answer.append(up) #anwer리스트에 up의 값을 추가해준다
        up += x #x를 누적한 값을 넣기 위해 up변수에 x를 누적해준다
    return answer # answer리스트를 반환해준다