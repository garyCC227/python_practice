'''
Auther: Linchen Chen
date: 15/3/2019

A boring game:
print a series of number 1 to N, but fizz instead of 3, buzz instead of 5,
fizzbuzz instead of number % 3 == 0 && number % 5 == 0
'''

def myPrinter(num):
    for i in range(1,num+1):
        if i % 15 == 0:
            yield "FizzBuzz"
        elif i % 5 == 0:
            yield "Buzz"
        elif i % 3 == 0:
            yield "Fizz"
        else:
            yield i

if __name__ == "__main__":
    printer = myPrinter(15)
    while True:
        print(next(printer))
