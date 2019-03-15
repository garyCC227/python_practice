

def word_len(phrase):
    list = phrase.split(" ")
    return list(map(len, list))

#word_len("How many word")
from functools import reduce

def digits_to_num(arg):
    return  reduce(lambda x, y:x*10+y, arg)
#([3,4,2,3]))
def match(letter):
    def match1(w):
        return w[0] == letter
    return match1

def filter_words(words, letter):
    filter14 = match(letter)
    return list(filter(filter14, words))

#l = ['hello','are','cat','dog','ham','hi','go','to','heart']
#print(filter_words(l, 'h'))

def concatenate(L1, L2, connector):
    return list((x+connector+y)for x,y in zip(L1,L2))

#print(concatenate(['A','B'],['a','b'],'-'))

def d_list(L):
    dict = {}
    for value,key in enumerate(L):
        dict[key] = value
    return dict

#print(d_list(['a','b','c']))

def count(L):
    counter = 0
    for value,key in enumerate(L):
        if(value == key):
            counter+=1

    return counter
b =count([0,2,2,1,5,5,6,10])
print(b)