## I am changing my input data before start
## changed \n\r --> * to separate passports
answers = input().split('*')
group_answers = []
for i in range(0, len(answers)):
    group_answers.append(answers[i].split(' '))
print(group_answers)


# The first group contains one person who answered "yes" to 3 questions: a, b, and c.
# The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
# The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
# The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
# The last group contains one person who answered "yes" to only 1 question, b.

yes_sum = 0
for j in range(len(group_answers)):
    yes_answers = []
    for k in range(len(group_answers[j])):
        for l in range(len(group_answers[j][k])):
            if group_answers[j][k][l] not in yes_answers:
                yes_answers.append(group_answers[j][k][l])
                yes_sum += 1
    print(yes_answers)
print(yes_sum)

# Part Two

# In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
# In the second group, there is no question to which everyone answered "yes".
# In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
# In the fourth group, everyone answered yes to only 1 question, a.
# In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.

all_yes_sum = 0

for j in range(len(group_answers)):
    all_yes_answers = []
    answer = ''
    for k in range(len(group_answers[j])):
        if (group_answers[j][k] != ''):
            all_yes_answers.append(group_answers[j][k])
    answer = str(len(all_yes_answers))
    for t in range(len(all_yes_answers)):
        answer = answer + all_yes_answers[t]
    #print(answer)
        
    for m in range(1, len(answer)):
        if answer.count(answer[m]) == int(answer[0]) and answer[m] != '*':
            all_yes_sum += 1
            answer = answer.replace(answer[m],'*')
print(all_yes_sum)