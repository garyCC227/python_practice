#!/usr/bin/python
'''
numbers exersice in url: 'https://github.com/jmportilla/Complete-Python-Bootcamp/blob/master/Final%20Capstone%20Projects/Projects-Solutions/Solution%20Links.md'
'''

import math

## exersice: Find PI to the Nth Digit
def find_nth_pi(N):

    pi = math.pi;
    pi = str(pi);
    non_decimal_couter = 2;
    return (pi[:N + non_decimal_couter]);


#get nth fibonacci number
def fibonacci(N):
    if (N == 0):
        return 0;
    elif(N == 1):
        return 1;
    else:
        i = 2;
        curr = 1; # set curr == F1 first, and curr is F(N-1)
        prev = 0; #prev = F(n-2)
        while (i <= N):
            F = curr + prev; #F is F(N), and set the following value for next loop
            prev = curr;    #prev = F(N-1)
            curr = F;       #curr = F(N)
            i+=1;
        return "{}th Fibonacci number is {}".format(N, F);

'''
return a to the power of b in OlogN
'''
def pow(a, b):
    """
    Return a to the power of b
    """
    if(b == 0):
        return 1
    else:
        temp = pow(a, math.floor(b / 2))
        if(b % 2 == 0):
            return temp * temp
        else:
            return temp * temp * a

if __name__ == '__main__':
    while True:
        try:
            a= int(input("how many decimal numbers you want to print??\n"));
            b= int(input("how many decimal numbers you want to print??\n"));
        except:
            print("Please Enter a integer");
            continue;
        else:
            #print(fibonacci(N))
            print(pow(a,math.floor(b)))
            break;
