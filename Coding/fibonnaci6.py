def fibonnaci(n):
    j = 0
    k = 1
    for i in range(0,n):
        print(j, end=" ")
        sum = j + k
        j = k
        k = sum
    
fibonnaci(10)
print("\n")
def reverse_fibonnaci(n):
    a = [0] * n
    a[0] = 0
    a[1] = 1
    for i in range(2,n):
        a[i] = a[i-2] + a[i-1]
    
    for j in range(n-1,-1,-1):
        print(a[j], end=" ")
    
reverse_fibonnaci(10)
print("\n")
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))