def get_cnt(n):
    cnt = 0
    for x in range(1,n+1):
        if(n%x == 0):
            cnt +=1
    return cnt

def solution(left, right):
    add = 0 #변수를 저장할 add
    for x in range(left,right+1): #left부터 right + 1까지 더해준다(right까지 돌리기위해 1을 더함)
        if get_cnt(x)%2==0: #get_cnt라는 함수에서 약수의 개수를 추출하고, 짝수면
            add += x
            print("짝수",x,get_cnt(x))
        else:
            add -= x
            print("홀수",x,get_cnt(x))
    return add

print(solution(0,6))