# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 20:23:38 2019

@author: clc87
"""

import random

suits = ['Hearts','Diamonds','Spades','Clubs']
ranks = ['Two', 'Three', 'Four','Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Quene', 'King', 'Ace']
values = {'Two':2, 'Three':3, 'Four':4,'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Quene':10, 'King':10,
          'Ace':11}
Playing = True

class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "Card is ---- {} : {}\n".format(self.suit, self.rank)

class Deck(object):
    global suits, ranks
    #create a new deck will also generate 52 cards in order
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank)
                self.deck.append(new_card)


    def __str__(self):
        string = '\n'.join(map(str, self.deck))
        return string

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

class Hand(object):
    global values
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces11 = 0
        self.aces0 = 0

    def add_card(self, card):
        self.cards.append(card)
        #check if card is Ace
        if(card.rank == 'Ace'):
            self.aces11 += 1

        #add to value
        value = values[card.rank]
        self.value += value

    def adjust_for_ace(self):
        if(self.aces11 == 0 and self.aces0 == 0):
            print( "I dont think you have a Ace in hand")
            return

        require_value = int(input("Wanna to change your Ace to 1 or 11?"))
        #adjust Ace to value 1
        if(require_value == 1 and self.aces11 != 0):
            self.value -= 10
            self.aces11 -= 1
            self.aces0 +=1
            print("You change one Ace to value 1, and value is {}".format(self.value))
        #adjust ace to 11
        elif(require_value == 11 and self.aces0 != 0):
            self.value += 10
            self.aces11 += 1
            self.aces0 -=1
            print("You change one Ace to value 11, and value is {}".format(self.value))
        else:
            print("All of your Ace is value {} now".format(require_value))


    def __str__(self):
        string = "You have cards:\n" + "".join(map(str, self.cards)) \
        + "Total value: {}\n".format(self.value)

        return string


class Chips(object):
    def __init__(self, account):
        self.account = account
        self.bet = 0;

    def win_bet(self):
        pass

    def lost_bet(self):
        pass
