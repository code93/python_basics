# Enter your code here. Read input from STDIN. Print output to STDOUT



def young(n,m,gifts):
  not_young = []
  young = [i for i in range(1,n+1)]
  members = []
  for gift in gifts:
    gift = gift.split(" ")
    gift[0] = int(gift[0])
    gift[1] = int(gift[1])
    if gift[0]:
      not_young.append(int(gift[0]))
      if gift[0] in young:
        young.remove(gift[0])
    # if gift[1] not in young and gift[1] not in not_young:
    #   young.append(gift[1])
    # if gift[0] not in members:
    #   members.append(gift[0])
    # if gift[1] not in members:
    #   members.append(gift[1])
  if len(young) == 1:
    return young[0]
  else:
    return -1



gifts = []
nm = input().split(" ")
n= int(nm[0])
m = int(nm[1])
for i in range(m):
  gift = input()
  gifts.append(gift)

print(young(n=n,m=m,gifts=gifts))


# # Enter your code here. Read input from STDIN. Print output to STDOUT

# def find_youngest_member(n, m, exchanges):

#     # Dictionary to count gifts received by each member

#     receivers_count = {i: 0 for i in range(1, n + 1)}

#     # Set to track members who have given gifts

#     givers_set = set()



#     for ai, bi in exchanges:

#         # Increment the count of gifts received by bi

#         receivers_count[bi] += 1

#         # Add ai to the set of givers

#         givers_set.add(ai)



#     # List to store potential youngest candidates

#     youngest_candidates = []



#     for member in range(1, n + 1):

#         # The member is a candidate if they have not given any gifts and received n-1 gifts

#         if member not in givers_set and receivers_count[member] == n - 1:

#             youngest_candidates.append(member)



#     # If exactly one candidate matches the criteria, return them

#     if len(youngest_candidates) == 1:

#         return youngest_candidates[0]

#     # Otherwise, return -1

#     return -1



# # Input handling

# if __name__ == "__main__":

#     # Read the first line for n (family members) and m (number of gifts)

#     n, m = map(int, input().strip().split())

    

#     # Read each exchange

#     exchanges = [tuple(map(int, input().strip().split())) for _ in range(m)]

    

#     # Call the function and print the result

#     print(find_youngest_member(n, m, exchanges))


# # Enter your code here. Read input from STDIN. Print output to STDOUT

# def find_youngest_member(n, m, gifts):

#   #create an array for receiced and for gifted

#     received_count = [0] * (n + 1)

#     given_count = [0] * (n + 1)

#     #increase recieved and gifted count according to number in the 

#     for giver, receiver in gifts:

#         given_count[giver] += 1

#         received_count[receiver] += 1

#     #checking whether gifted count is -1 and given count of parrticular number is n-1 and 0 respectively

#     for i in range(1, n + 1):

#         if received_count[i] == n - 1 and given_count[i] == 0:

#             return i

#     #if not found

#     return -1
