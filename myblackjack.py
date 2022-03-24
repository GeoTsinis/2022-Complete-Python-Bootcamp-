"""
Workflow: 1. Create a card object 2. Create a deck of 52 cards 3. Shuffle the deck 4. Create a chip stack 5. Ask the player for his bet 
  6. Make sure player's bet doesn't exceed his stack 7. Deal two cards to the player and two cards to the Dealer 8. Show only one card from the dealer's hand
  9. Ask the player if he wants to Hit = take another card OR Stand = go to dealer's turn 10. If player's hand value > 21 he is busted
  11. Dealer always hits until he reaches a hand value > 17 (or over the player's hand value for a more realistic game) 
  12. Determine the winner and adjust the player's chips accordingly 13. Ask the player if he wants to play again. 
"""
import random

#Global variables
suits = ["Hearts",'Diamonds','Spades','Clubs']
ranks = ['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,
          'Ace':11}
player_turn = True

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + ' of '+ self.suit
      
class Deck:
    
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
    
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop()
    
    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp
  
class Hand:
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'Ace':
            self.aces += 1
    
    #If our hand value is over 21 and we have an ace in hand then this ace's value becomes 1
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1   

 class Chips:
    
    def __init__(self):
        self.total = 100
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
        
    def lose_bet(self):
        self.total -= self.bet
        
def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input("Place your bets: "))
        except ValueError:
            print("Your input must be a number")
        else:
            if chips.total < chips.bet:
                print(f"Your bet can not be higher than {chips.total} chips")
            else:
                print("Successful Bet.")
                break
                
 def hit(deck,hand):
    
    hand.add_card(deck.deal_one())
    hand.adjust_for_ace()
    
 def hit_or_stand(deck,hand):
    
    global player_turn 
    
    while True:
        decision = input("Hit or Stand? ")
        if decision[0].upper() == 'H':
            hit(deck,hand)
        elif decision[0].upper() == 'S':
            print("Player Stands! Dealer's Turn.")
            player_turn = False
        else:
            print("Please answer with Hit or Stand")
            continue
        break

#Before the dealers turn the player sees only the first card of the dealer's hand      
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)  
    
#Chips result depending on who won
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
    
#main game starts here!!
player_chips = Chips()

while True:
    
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal_one())
    player_hand.add_card(deck.deal_one())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal_one())
    dealer_hand.add_card(deck.deal_one())
    
    print(f"Your current balance: {player_chips.total}")
    
    take_bet(player_chips)
    
    show_some(player_hand,dealer_hand)
    
    while player_turn:
        
        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)
        
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
    
    #Dealer's Turn
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
        
        show_all(player_hand,dealer_hand)
        
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
            
        elif dealer_hand.value == 21:
            dealer_wins(player_hand,dealer_hand,player_chips)
            
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
            
        elif player_hand.value > dealer_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
            
        else:
            push(player_hand,dealer_hand)
    
    # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        player_turn=True
        continue
    else:
        print("Thanks for playing!")
        break
