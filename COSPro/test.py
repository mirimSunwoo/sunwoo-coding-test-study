def sum_list(scores):
    result = 0
    for x in scores:
        result += x
    return result

def max_list(scores):
    max = 0
    for x in scores:
        if x > max:
            max = x
    return max
#인터넷
def max_list(scores):
    max = scores[0]
    for x in scores:
        if max < x:
            max = x
    return max

def min_list(scores):
    min = max(scores)
    for x in scores:
        if x<min:
            min = x
    return min
#인터넷 따라해보기(왜 0이 나올까)
def min_list_2(scores):
    min = scores[0]
    for x in range(1,len(scores)):
        if x == 0 or min > scores[x]:
            min = scores[x]
    return min

def avg_list(scores):
    avg = 0
    sum = 0
    for x in scores:
        sum += x
    avg = sum/len(scores)
    return avg

def count_even(scores):
    count = 0
    for x in scores:
        if(x %2 ==0):
            count += 1
    return count

def make_list(number):
    list = [0 for _ in range(number)] #안써도 되지만 빈칸으로 하기 싫을 때 _을 씀
    return list

def count_even_upperten(scores):
    count  = 0
    for x in scores:
        if x>10 and x%2 == 0:
            count += 1
    return count

# 1. 숫자가 들어있는 리스트의 합계
scores = [10, 3, 20, 50]
print(f'리스트의 합계 : ',sum_list(scores))   #83
# 2. 최댓값
print(f'리스트의 최댓값 : ',max_list(scores))   #50
# 3. 최솟값
print(f'리스트의 최솟값_1 : ',min_list(scores))   #3
print(f'리스트의 최솟값_2 : ',min_list_2(scores))
# 4. 평균
print(f'리스트의 평균 : ',avg_list(scores))   #20.75
# 5. 짝수인 것만 세기
print(f'짝수의 개수 : ',count_even(scores))   #3
# 6. N개의 0을 가진 리스트 만들기
print(f'n만큼 0리스트 만들기 : ',make_list(6))   #[0, 0, 0, 0, 0, 0]
# 7. 짝수 이면서 10보다 큰 것 세기
print(f'짝수이면서 10보다 큰 것의 개수 : ',count_even_upperten(scores))
#출력
name = "이선우"
age = 19
print(f'name: {name}\tage: {age}')

a = 10
a = a + 1
a +=1

print(10**3) #10의 3제곱
print(10/3) #10을 3으로 나눈 값
print(10//3) #10을 3으로 몫
print(10%3) #10을 3으로 나누 나머지

'hello'[2] #'l'
a = [10,20,30]
print(a[2]) #30
'hello'[-1] #'0'
'hello'[-2] #'l'
'hello'[1:3] #'el' 문자열 자르는 슬라이싱
'hello'[:3] #'hel'
'hello'[1:] #'ello'
'hello'[:] #'hello'

print('hello'.count('l')) #없으면 0
print('hello'.find('l'))
print('hello'.find('z')) #없으면 -1
print('hello'.index('l'))
# print('hello'.index('z')) #없으면 에러
print('hello'+'world') #helloworld
a = 'hello world good lunch'
b = a.split(' ') #띄어쓰기로 잘라서 리스트에 넣는다
print(b)
c = '::'.join(b) #중간에 ::을 넣을때
print(c) #hello::world::good::lunch

print("-"*20)
print(3*2)
amtm = ['원슈타인','자이언티','소코도모']
amtm.append('계란썬')
print(amtm)

amtm2 = amtm.copy()
amtm2.append([1,2])
print(amtm2)
amtm2 = amtm2 + [1,2]
print(amtm2)

print(amtm2.count(2))
print(amtm2.index(2))
print(amtm2.remove(2))
print(amtm2)

amtm.sort() #원본이 바뀜
print(amtm)
amtm.reverse()
print(amtm)

amtm = sorted(amtm) #원본 안바뀌고 행위를 하는 것임
print(amtm)

for item in amtm: #직관적이고 파이썬스러운 코드임
    print(item)

for i in range(len(amtm)):
    print(amtm[i])

for i in range(0,4,1): #0부터 4까지 1씩 증가한다(for문과 비슷하게 만들 수있다)
    print(amtm[i])

for index,value in enumerate(amtm):
    print(f'{index+1}. {value}')

int("123") #내가 원하는 자료형을 호출하면 그렇게 됨
str(123)
a = list("123") #string을 한글자씩 꺼내서 리스트로 만든다
print(a)
