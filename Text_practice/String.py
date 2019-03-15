'''
Auther: Linchen Chen
date: 15/3/2019

String class that has plenty functionlities
'''
class Mystring():
    def __init__(self, str):
        self.str = str
    #reverse a stirng
    @property
    def reverse(self):
        return self.str[::-1]

    #cout vowels
    @property
    def vowel(self):
        vowels = "aeiouAEIOU"
        for i in iter(self.str):
            if i in vowels:
                yield i

    @property
    def is_palindrome(self):
        return self.str == self.str[::-1]

    #count words, or count a specific word in a string or a file
    def count_word(self, word=None, file=None, string = None):
        '''
        1st arg = specific word
        2nd arg = file name
        3rd arg = string
        '''
        count = 0
        if string:
            str = (string.split(' '))
            if word:
                 for e in str:
                     if e.lower() == word.lower():
                        count+=1
            else:
                count = len(str)
        elif file:
            if word:
                with open(file) as f:
                    for e in (f.read().split()):
                        if e.lower() == word.lower():
                           count+=1
            else:
                with open(file) as f:
                    count = len(f.read().split())
        return count

if __name__ == '__main__':
    str = "You will see how handsome you are"
    x = Mystring(str)
    #print(*x.vowel)
    #print(x.reverse)
    #print(x.is_palindrome)
    print(x.count_word('if','fizzBuzz.py',None))
