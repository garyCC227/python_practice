'''
Auther: Linchen Chen
date: 15/3/2019

simple calculator
'''

class Calculator(object):
    @property
    def run(self):
        while True:
            firstnum = input()
            op = input()
            secnum = input()
