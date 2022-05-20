def solution(s):
    answer = '' #결과값을 넣을 변수를 만들어준다
    index = int(len(s)//2) #s배열의 길이를 정수형으로 바꿔 2로 나눈다
    if len(s)%2 == 1: #s배열의 길이가 2로 나누었을때 1 ==> 홀수일때
        answer = s[index] #5/2 = 2.5 즉 정수로 바꾸면 2가 된다. 가운데 값을 찾을 수 있다
    else:
        answer = s[index-1:index+1] #5/2 = 2.5 정수로는 2 [1:3] index1,index2의값 두개출력
    return answer #결과값 반