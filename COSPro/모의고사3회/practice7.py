 #야구게임의 볼 판전 함수 수정하기

def solution(a,b):
     result = [0,0]
     for i in range(3):
         temp = b
         for k in range(3):
             if a % 10 == temp % 10:
                 if  i == k:
                     result[0] += 1
                     print(i,k)
                 else:
                     print(i,k)
                     result[1] += 1
             temp //= 10
         a //= 10
     return result

print(solution(123,345))