def solution(n):
    answer = 0 #누적합을 위한 answer변수 선언
    while(answer<=n): #누적합을 한것이 n값보다 작을시에만 돈다
        if(answer**2 == n): #누적합을 한 수의 제곱이 n과 같을 시
            return (answer + 1)**2 #누적합 + 1의 제곱을 반환
        answer += 1 #제곱근을 판별한 누적합
    return -1 #모두 아닐시 -1을 반환 한다