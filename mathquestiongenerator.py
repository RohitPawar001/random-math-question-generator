import random
import time

operator = ["+","-","/","*"]
min_no = 1
max_no = 100

def genrate():
    num1 = random.randint(min_no,max_no)
    num2 = random.randint(min_no,max_no)
    operation = random.choice(operator)
    
    equation = str(num1) +" "+ operation +" "+str(num2)
    answer = eval(equation)
    
    return equation, answer

score = 0
print("**********************")
start_time = time.time()
for i in range(10):
    equation,answer = genrate()
    ans =input(f"{i+1} your question is :  {equation}")
    if ans == str(answer):
        score += 1
end_time = time.time()
exe_time = end_time - start_time

print("*************************")
print(f"your score is {score} you take {round(exe_time)} sec. to answer")
    