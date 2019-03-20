'''
1 - List comprehensions
2 - iterator and generator
3. decorator
'''
####### List comprehensions
# Use [] make code shorter
print([i for i in range(10) if i%2 ==0])
seq = ['one','two','three']
print(["{}, {}".format(i,element) for i, element in enumerate(seq)])

########iterator and generator
##__iter__  this magic function take thing to iterator
i = iter('abc')
print(next(i))
print(next(i))

##generator by Yield

def myGenerator():
    for i in range(5):
        yield i

i = myGenerator()
print(next(i))
print(next(i))

#generator.send()
#send() can pass value to a yield expreesion, such a controll return
def hello():
    while True:
        answer = (yield)
        if answer == 'yes':
            yield "I love you"
        elif answer == 'no':
            yield "I hate you"
free = hello()
print(next(free))
print(free.send('yes'))
print(next(free))
print(free.send('no'))

#generator.close(), generator.throw()
'''
like in erro handling:
try:

except:
    #throw go here
finally:
    #close go here
'''

##generator shorter expression
## like list comprehensions, but use () to instead []
iter = (i for i in range(10) if i % 2 == 0)
print(iter)

##itertools
##islice
'''
useage: itertools.islice(iterator, start, end, step)
like list slice
'''
##groupby
'''
useage: itertools.groupby(data)
: similar to 'uniq' in linux = group dulicate element , as long as
they are adjacent.
'''
from itertools import *
def compress(data):
    return ((len(list(group)), name) for name, group in groupby(data))

print(list(compress('get uppppppppppp')))

######################################################
########### decorator
