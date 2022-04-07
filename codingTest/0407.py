def solution(n):
    answer = ''
    even = '수박' #짝수일때 출력하는 두글자
    odd = '수' #홀수일때 더해줄 한글자
    if(n%2==0): #만약 짝수라면
        answer = even * (n//2)#짝수글자 * 나눈몫
    else: #짝수가 아닌 홀수라면
        answer = even * (n//2) + odd #짝수글자 * 나눈몫 + 홀수글자
    return answer

#다른사람의 풀이

#=>방법은 비슷하지만 한줄로 끝낸 간결한 코드
#  짝수는 몫값으로, 홀수는 나머지값으로 구해서 더한걸로 보인다
def water_melon(n):
    return "수박"*(n//2) + "수"*(n%2) 