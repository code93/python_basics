# Enter your code here. Read input from STDIN. Print output to STDOUT

# duplicated string to find kth unique string

 # if no of unique string < k display empty string

def sort_unique(N_no,N,k):
  sort_list = N.copy()
  for n in range(0,len(N)):
    name1 = N[n]
    for n2 in range(n+1,len(N)):
      name2 = N[n2]
      if name1 == name2:
        sort_list = [l for l in sort_list if l!=name1]
  if len(sort_list) < k:
    return ""
  else:
    return sort_list[k-1]

inp = int(input())
nu_list = []
for inp2 in range(0,inp):
  inp2 = input()
  nu_list.append(inp2)
inp3 = int(input())

print(sort_unique(inp, nu_list,inp3))