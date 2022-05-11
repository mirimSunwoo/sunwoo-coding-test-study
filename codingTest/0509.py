a, b = map(int, input().strip().split(' '))
count = 0
for x in range(0,a*b):
    print('*',end='')
    count += 1
    if count==a:
        count = 0
        print()

#다른사람의 풀이
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)