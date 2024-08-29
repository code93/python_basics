from collections import namedtuple

account = ('checking', 1850.90)

Account = namedtuple('Account',['name','balance'])

account = Account('checking', 1850.90)

print(account.name)