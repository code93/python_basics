n = 10
num1 = 0
num2 = 1
count = 0
next_number = num2

while count <= n: #0<n
    count = count+1  # 1 2
    print(next_number, end=" ")
    num1,num2 = num2, next_number  #num1 = 1,num2 =1 #num1 = 1, num2 = 2, #num1=2,num2=3 
    next_number = num1 + num2 #1+1 #1+2 #2+3=5

