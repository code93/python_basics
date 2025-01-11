# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def reverse_k(n,k,string):
  reverse_string = ""
  for i in range(0,n):
    reverse_string = string[i] + reverse_string 
  if k <= len(string):
    return reverse_string[k]
  # if k > len(string):
  #   raise IndexError("value of k is greater than length of string")
  


no = re.split(" ",input())
n = no[0]
k = no[1]
string=input()
print(string)
print(reverse_k(n=n,k=k,string=string))