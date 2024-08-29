# Define a PrimeGenerator class
class PrimeGenerator:
    # You may modify the __init__() method if necessary, but you don't need to change its arguments
    def __init__(self, stop):
        self.stop = stop    # stop defines the range (exclusive upper bound) in which we search for the primes
        self.number = 2
    def __next__(self):
        stop = self.stop
        for n in range(self.number, stop):
            for x in range(2,n):
                if n % x == 0:
                    break
            else:
                self.number = n + 1
                return n
        raise StopIteration()
prime_obj = PrimeGenerator(10)
print(next(prime_obj))
print(next(prime_obj))
print(next(prime_obj))
print(next(prime_obj))
print(next(prime_obj))
print(next(prime_obj))