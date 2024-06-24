# import random

# # This line creates a set with 6 random numbers
# lottery_numbers = set(random.sample(list(range(22)), 6))

# # Here are your players; find out who has the most numbers matching lottery_numbers!
# players = [
#     {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
#     {"name": "Charlie", "numbers": {2, 7, 9, 21, 10, 5}},
#     {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
#     {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}},
# ]
# earnings=[(len(set(player["numbers"]).intersection(lottery_numbers)),player["name"]) for player in players]

# winnings = [f'{name} won {10 ** earning}.' for earning,name in earnings]
# for i in range(len(winnings)):
#   print(winnings[i])
# # Then, print out a line such as "Jen won 1000.".
# # The winnings are calculated with the formula:
# # 100 ** len(numbers_matched)

# foo = [0,1,2,3,4]
# def add(foo=foo, sum= 0):
#   for f in foo:
#     sum = sum + f
#   return sum

# sum = add()
# print(sum)
# foo=[1,2,3,4,5]
# sum2 = add(foo=foo)
# print(sum2)

# def over_age(data, getter):
#   return getter(data) >= 18

# user = { 'username': 'rolf123', 'age': '35' }

# print(over_age(user, lambda x: int(x['age'])))

# movies = [{
#     "title": "Hello",
#     "director": "Hello",
#     "year": "2024"
#            }]

# def find(movies, title):
#   for movie in movies:
#       if title in movie["title"]:
#           print("Movie found")
#           return f"Movie title: {movie['title']} \n Movie diretor: {movie['director']} \n Movie year: {movie['year']}"

class Foo :

    @classmethod

    def hi(cls):

        print(cls.__name__)

my_object  = Foo()

my_object.hi()