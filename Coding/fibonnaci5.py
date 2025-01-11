# def fibonnaci(n):
#     k = 0
#     j = 1
#     for i in range(0,n):
#         print(f'term: {i} / number: {k}')
#         c = k + j
#         k = j
#         j = c

# # fibonnaci(10)

# def reverse_fibonnaci(n):
#     a = [0] * n
#     a[0] = 0
#     a[1] = 1
#     for i in range(2,n):
#         a[i] = a[i-2] + a[i-1]
#         print(f"[+]{a[i]}")
#     for i in range(n-1,-1,-1):
#         print(a[i], end=" ")

# reverse_fibonnaci(10)

def reverse_fibonnaci(n):
    a = [0] * n
    a[0] = 0
    a[1] = 1
    for i in range(2, n):
        a[i] = a[i-2] + a[i-1]
    for i in range(n-1,-1,-1):
        print(f"{a[i]}", end=" ") 

reverse_fibonnaci(10)

def factorial(n):
    if n ==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))