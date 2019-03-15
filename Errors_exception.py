'''
try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print('Type error raise bro')

'''
'''
#q2
try:
    x=5
    y=0
    z=x/y
except ZeroDivisionError:
    print('Cannot divide by zero')
finally:
    print('all done')
'''

#q3
import sys

def ask():
    int_ = int(input('Give me a integer'))
    print('input int is {}'.format(int_))
    return int_**2

while True:
    try:
        temp = ask()
    except:
         print("Unexpected error:") #sys.exc_info()[0])
    else:
        print('result is {}'.format(temp))
        break
