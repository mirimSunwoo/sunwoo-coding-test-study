#실험중인 코드(정제되지 않은 코드)
def solution(answers):
    answer = []
    supo_1 = [1, 2, 3, 4, 5]
    supo_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0, 0, 0]
    for index, x in enumerate(answers):
        if (x == supo_1[index]):
            count[0] += 1
        if (x == supo_2[index]):
            count[1] += 1
        if (x == supo_3[index]):
            count[2] += 1

    max = 0
    for x in range(0, len(count)):
        if (count[x] > max):
            max = count[x]
            maxindex = x + 1
            answer.append(maxindex)
    if(count[0] == count[1]) and (count[1]==count[2]):
        answer.append(1)
        answer.append(2)
        answer.append(3)
    return answer

#다른 분의 코드
def solution(answers):
   answer = []
   answer_temp = []
   count01 = 0
   count02 = 0
   count03 = 0
   supo_1 = [1, 2, 3, 4, 5]
   supo_2 = [2, 1, 2, 3, 2, 4, 2, 5]
   supo_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
   for i in range(len(answers)):
       if answers[i] == one[i%len(supo_1)]:
           count01 += 1
       if answers[i] == one[i%len(supo_2)]:
           count02 += 1
       if answers[i] == one[i % len(supo_3)]:
           count03 += 1
   answer_temp = [count01, count02, count03]
   for person, score in enumerate(answer_temp):
       if score == max(answer_temp):
           answer.append(person+1)
   return answer
