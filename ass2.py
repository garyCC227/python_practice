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
        return " - {} : {}".format(self.suit, self.rank)

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

    def haveAce(self):
        if(self.aces11 == 0 and self.aces0 == 0):
            return False
        return True

    def adjust_for_ace(self):
        if(haveAce() == False):
            print( "\n I dont think you have a Ace in hand")
            return

        require_value = int(input("\n Wanna to change your Ace to 1 or 11?"))
        #adjust Ace to value 1
        if(require_value == 1 and self.aces11 != 0):
            self.value -= 10
            self.aces11 -= 1
            self.aces0 +=1
            print("\n Ace changed to 1, total value: {}".format(self.value))
        #adjust ace to 11
        elif(require_value == 11 and self.aces0 != 0):
            self.value += 10
            self.aces11 += 1
            self.aces0 -=1
            print("\n Ace changed to 11, total value: {}".format(self.value))
        else:
            print("\n All of your Ace is value {} now".format(require_value))


    def __str__(self):
        string = "You have cards:\n" + "".join(map(str, self.cards)) \
        + "\n Total value: {}\n".format(self.value)

        return string


class Chips(object):
    def __init__(self, account):
        self.account = account
        self.bet = 0;

    def win_bet(self):
        self.account += self.bet

    def lose_bet(self):
        self.account -= self.bet

    def take_bet(self):
        while True:
            try:
                self.bet = int(input("\n How much chips would you like to bet??"))
            except ValueError:
                print("\n Must be a integer!!")
            else:
                if(self.bet > self.account):
                    print("\n Insufficient money in account, try again!")
                else:
                    break


def hit(deck, hand):
    card = deck.deal()
    hand.add_card(card)
    while hand.haveAce():
        print("************************************************************************************************")
        print(hand)
        if(input("\n Change Ace? y/n??").startswith('n')):
            break
        hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global Playing

    while True:
        s = input("\n Would you like to hit or stand? Enter h or s?? ")
        if(s.startswith('h')):
            hit(deck, hand)
        elif(s.startswith('s')):
            print("*********************************************************************************************** " \
            + "*************************************************************************************************")
            print("\n Player stand, now is dealer's turn")
            Playing = False
        else:
            print("\n You maynot enter h or s, pls try again")
            continue
        break

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" - <card hidden>")
    print('',dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and Player tie! It's a push.")

#playing game
def main():
    chip = Chips(100)
    global Playing
    while True:
        print("Welcome to this game, wanna become rich? play now and no end")
        print("\n You are giving 100 dollars to play")

        # Create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()
        player = Hand()
        dealer = Hand()
        for i in range(2):
            player.add_card(deck.deal())
            dealer.add_card(deck.deal())

        show_some(player, dealer)


        # Prompt the Player for their bet
        chip.take_bet()

        while Playing:

            # Prompt for Player to Hit or Stand
            hit_or_stand(deck, player)

            # Show cards (but keep one dealer card hidden)
            show_some(player, dealer)

            # If player's hand exceeds 21, run player_busts() and break out of loop
            if(player.value > 21):
                player_busts(player, dealer, chip)
                break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if(player.value <= 21):
            while (dealer.value < 17):
                hit(deck, dealer)
            #  Show all cards
            show_all(player, dealer)
            # Run different winning scenarios
            if dealer.value > 21:
                dealer_busts(player, dealer, chip)

            elif dealer.value > player.value:
                dealer_wins(player,dealer,chip)

            elif dealer.value < player.value:
                player_wins(player,dealer,chip)

            else:
                push(player,dealer)

        # Inform Player of their chips total
        print("\n You have {} money in your account!".format(chip.account))
        # Ask to play again
        new_game = input("Would you like to keep playing? y/n?? ")
        if(new_game.startswith('y')):
            Playing = True
            continue
        else:
            print("Thanks for playing")
            break


if __name__ == '__main__':
    main()
