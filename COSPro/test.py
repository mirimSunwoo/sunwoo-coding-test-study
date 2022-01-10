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

def min_list(scores):
    min = max(scores)
    for x in scores:
        if x<min:
            min = x
    return min
#인터넷 따라해보기(왜 0이 나올까)
def min_list_2(scores):
    min = 0
    for x in scores:
        if x == 0 or x < min:
            min = x
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
    return [0]*number

# 1. 숫자가 들어있는 리스트의 합계
scores = [10, 3, 20, 50]
print(sum_list(scores))   #83
# 2. 최댓값
print(max_list(scores))   #50
# 3. 최솟값
print(min_list(scores))   #3
print(min_list_2(scores))
# 4. 평균
print(avg_list(scores))   #20.75
# 5. 짝수인 것만 세기
print(count_even(scores))   #3
# 6. N개의 0을 가진 리스트 만들기
print(make_list(6))   #[0, 0, 0, 0, 0, 0]

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