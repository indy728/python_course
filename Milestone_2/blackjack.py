import random
import os
from operator import attrgetter
from sys import stdout

write = stdout.write

suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', \
'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, \
'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

def strcmp_nocase(s1,s2):
    if s1.lower() == s2.lower():
        return True
    return False

class Card:

    def __init__(self,suit,rank,value):
        self.suit = suit
        self.rank = rank
        self.value = value
        self.hidden = False
    
    def __str__(self):
        if self.hidden:
            return "XXXXXXXXXXXXXX"
        return f"{self.rank} of {self.suit}"

    def visualize(self):
        return(f"|  {self.__str__()}  |")

class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank, values[rank]))
    
    def __str__(self):
        deck_to_str = ""
        for card in self.deck:
            deck_to_str += f"{card.rank} of {card.suit}\n"
        return deck_to_str

    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        return self.deck.pop()

class Hand:

    def __init__(self, deck):
        self.deck = deck
        self.cards = []
        self.value = 0
        self.aces = 0
        self.playing = True
    
    def hit(self):
        card = self.deck.deal()
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'Ace':
            self.aces += 1
        return card

    def show(self):
        for card in self.cards:
            write(card.visualize())
        print()

class Chips:

    def __init__(self):
        self.bank = 50
        self.bet = 0
    
    def win_bet(self):
        self.bank += self.bet
        self.bet = 0

    def lose_bet(self):
        self.bank -= self.bet
        self.bet = 0

    def push_bet(self):
        self.bet = 0
    
def take_bet(chips):

    while True:
        try:
            chips.bet = int(input(f'Your bank is at {chips.bank}. How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be in the form of an integer!')
        else:
            if chips.bet > chips.bank:
                print(f"Sorry, your bet cannot exceed {chips.bank}")
            else:
                break

def hit_or_stay(dealer, player):
    while True:
        os.system("clear")

        game_board(dealer, player)

        response = input("Would you like to hit or stay?: ")
        if strcmp_nocase("hit", response):
            card = player.hit()
            print(card.visualize())
            input("Press enter to continue...")
            os.system("clear")
            # game_board(dealer, player)
            if player.value == 21:
                print(f"Player has 21!")
                break
            elif player.value > 21:
                if player.aces > 0:
                    player.value -= 10
                    player.aces -= 1
                else:
                    print(f"Bust! Player has {player.value}!")
                    break
        else:
            print(f"Player opts to stay with a value of {player.value}")
            break
    dealer.cards[0].hidden = False    
    input("Press enter to continue...")

def game_board(dealer, player):
    print("Dealer:")
    print("\n\n\n")
    dealer.show()
    print("\n\n\n")
    print("Player:")
    print("\n\n\n")
    player.show()
    print("\n\n\n")

def blackjack(playing = True):
    deck = Deck()
    deck.shuffle()

    dealer = Hand(deck)
    player = Hand(deck)

    x = 0
    while x < 2:
        player.hit()
        dealer.hit()
        x += 1

    dealer.cards[0].hidden = True

    hit_or_stay(dealer, player)
    
    if player.value <= 21:
        while dealer.playing:
            if dealer.value > 16:
                if dealer.aces > 0:
                    dealer.value -= 10
                    dealer.aces -= 1
                if dealer.value > 16:
                    dealer.playing = False
            else:
                os.system("clear")
                game_board(dealer, player)
                input("Press enter to continue...")
                card = dealer.hit()
                print(card.visualize())
    
        os.system("clear")
        game_board(dealer,player)
        if dealer.value < player.value or dealer.value > 21:
            winner = "Player wins!"
            chips.win_bet()
        elif dealer.value > player.value:
            winner = "Dealer wins!"
            chips.lose_bet()
        else:
            winner = "Push"
            chips.push_bet()
        print(f"\n\n{winner}")
    else:
        chips.lose_bet()

    if chips.bank == 0:
        print("Sorry, you are out of chips to bet!")
        playing = False
    else:
        while True:
            play_again = input("Would you like to play again? (y) or (n)")
            if strcmp_nocase("n", play_again):
                print(f"Thank you for playing. Please see the cashier to change out your {chips.bank} chips for cash. Please come again!")
                playing = False
                break
            elif strcmp_nocase("y", play_again):
                break
            else:
                print("Invalid response.")
    return playing
    

if __name__ == "__main__":
    
    chips = Chips()
    while True:
        os.system("clear")
        take_bet(chips)
        if blackjack() == False:
            break