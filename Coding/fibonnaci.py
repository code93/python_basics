# n = 10
# num1 = 0
# num2 = 1
# next_number = num2
# count = 1

# while count <= n:
#     print(next_number, end=" ")
#     count += 1
#     num1, num2 = num2, next_number
#     next_number = num1 + num2

# def reverseFibonacci(n):
#     a= [0] * n
#     a[0] = 0
#     a[1] = 1

#     for i in range(2,n):
#         a[i] = a[i-2] + a[i-1]
#     for i in range(n-1,-1,-1):
#         print(a[i], end=" ")

# n= 5
# reverseFibonacci(n)


# n = 23
# fact =1

# for i in range(1, n+1):
#     fact = fact * i

# print("The factorial of 23 is :", end="")
# print(fact)

def factorial(n):
    if (n==1 or n==0):
        return 1
    else:
        return (n*factorial(n-1))

num = 5
print("number:", num)
print("Factorial :", factorial(num))