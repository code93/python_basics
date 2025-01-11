n = 10
count = 0
num1 = 0
num2 = 1
next_number = num2

while count <= n:
    count =count + 1
    print(next_number, end=" ")
    num1 = num2
    num2 = next_number
    next_number = num1 + num2
