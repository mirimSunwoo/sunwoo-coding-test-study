def solution(arr):
    answer = 0 #반환할 변수, 연산에 사용할 변수를 0으로 초기화 해준다
    for x in arr: #arr배열의 값을 하나하나 x에 넣어준다
        answer += x #answer반환 변수에 x(arr의 value)를 누적합 해준다
    return answer / len(arr) #반환을 할 참에 arr배열의 길이만큼 나눠서 값을 return한다