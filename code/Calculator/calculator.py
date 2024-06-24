from addition import Addition
# You don't need to change the import statement
# now you can use Addition.add() function from the addition module like this:
# res = Addition.add(100, 150)
# the Addition.add() function takes in two parameters `num1` and `num2` and return the sum of `num1` and `num2`


# Please create and implement a Calculator class, which makes use of the `addition` module.
# Your Calculator should achieve these goals:
# - It should implement `Addition.add()`, `subtract()`, `multiply()` and `divide()` methods.
# - It cannot use addition, subtraction, multiplication and division operators (`+`, `-`, `*` and `/`) directly.
#   Instead, it should be only based on the `Addition.add()` function from the `addition` module.
# - To simplify the problem, you may expect input for the multiply() and divide() methods are all non-integers,
#   and will always be valid, i.e. all non-negative integers and no 0 as divisor.

# the class definition and a sample class method `Addition.add()` is provided below
class Calculator:

    # a sample add() method in our calculator is shown below
    # you may learn from it and implement the other methods
    @classmethod
    def add(cls, num1, num2):
        return Addition.add(num1, num2)  # make use of add() from addition module

    # implement a class method `subtract()` that takes in num1 and num2 and return num1 - num2
    # your `subtract()` method cannot use the + - * / calculation operators, but can use - as a negative sign operator
    @classmethod
    def subtract(cls,num1, num2):
        return Addition.add(num1,-num2)
    # implement a class method `multiply()` that takes in num1 and num2 and return num1 * num2
    # your `multiply()` method cannot use the + - * / calculation operators, but can use - as a negative sign operator
    # you may assume num1 and num2 are always non-negative integers
    @classmethod
    def multiply(cls,num1,num2):
        sum = 0
        for i in range(num2):
            sum = Addition.add(sum,num1)
        return sum
    # implement a class method `divide()` that takes in num1 and num2 and return num1 // num2
    # your `divide()` method cannot use the + - * / calculation operators, but can use - as a negative sign operator
    # you may assume num1 is always a non-negative integer, and num2 is always a positive integer
    @classmethod
    def divide(cls,num1,num2):
        res = num1
        count = 0
        count2 = 0
        if num1 == 0:
            return 0
        while res > 0:
            res = Addition.add(res,-num2)
            count = Addition.add(count,1)
        if res!=0:
            res = Addition.add(res,num2)
        if res > 0:
            res2 = cls.multiply(res,100)
            while res2>0:
                res2 = Addition.add(res2,-num2)
                count2 = Addition.add(count2,1)
        if count2 != 0:
            final_sum = Addition.add(count-1,float(f'0.{count2}'))
        if count2 == 0:
            final_sum = count
        if res > 0:
            return count-1
        if res <= 0 :
            return count
    
print(Calculator.divide(144,12))


### SOLUTION BY THE TUTORIAL

    # from addition import Addition
     
    # class Calculator:
    #     @classmethod
    #     def add(cls, num1, num2):
    #         return Addition.add(num1, num2)  # make use of add() from Addition module
     
    #     @classmethod
    #     def subtract(cls, num1, num2):
    #         return cls.add(num1, -num2)     # turn subtraction to adding a negative num2
     
    #     @classmethod
    #     def multiply(cls, num1, num2):
    #         res = 0
    #         for x in range(0, num2):
    #             res = cls.add(res, num1)    # add num1 for num2 times
    #         return res
     
    #     @classmethod
    #     def divide(cls, num1, num2):
    #         res = 0
    #         while num1 >= num2:
    #             num1 = cls.subtract(num1, num2)  # subtract num2 from num1 until its remainder is smaller than num2
    #             res = cls.add(res, 1)   # count the times of subtraction as the result
    #         return res