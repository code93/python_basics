answers = []
score = 0
import re
with open('questions.txt', "r") as f:
    lines = f.readlines()
f.close()
questions = [re.split('=',line)[0].strip() + "=" for line in lines]
correct_ans = [re.split('=',line)[1].strip() for line in lines]
for i in range(len(questions)):
    print(questions[i])
    answer = input("Answer:")
    if int(answer) == int(correct_ans[i]):
        score = score + 1

with open('result.txt', "w") as g:
    g.write(f"Your final score is {score/len(correct_ans)}")