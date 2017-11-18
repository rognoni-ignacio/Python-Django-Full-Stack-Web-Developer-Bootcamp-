### WELCOME TO YOUR OOP PROJECT #####

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:

# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.

# The Play:

# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.

# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.


from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """

    def __init__(self):
        print("Creating New Ordered Deck")
        self.allcards = [(s,r) for s in SUITE for r in RANKS ]

    def shuffle(self):
        print("Shuffling Deck")
        shuffle(self.allcards)

    def split_cards(self):
        return (self.allcards[:26],self.allcards[26:])


class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''

    def __init__(self,cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add_card(self,card):
        self.cards.extend(card)

    def remove_card(self):
        return self.cards.pop()


class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name,drawn_card))
        print('\n')
        return drawn_card

    def play_war_card(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return war_cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards


    def still_has_cards(self):
        return len(self.hand.cards) > 0


#### GAME PLAY #######

print("Welcome to War, let's begin...")

deck = Deck()
deck.shuffle()
player_1_cards, player_2_cards = deck.split_cards()

player1 = Player("Player 1", Hand(player_1_cards))
player2 = Player("Player 2", Hand(player_2_cards))

print(player_1_cards)
print(player_2_cards)

total_rounds = 0
war_count = 0

while player1.still_has_cards() and player2.still_has_cards():
    total_rounds += 1
    print("New round")
    print("Standings: ")
    print(player1.name + " has: " + str(len(player1.hand.cards)) + " cards")
    print(player2.name + " has: " + str(len(player2.hand.cards)) + " cards")
    print('\n')

    table_cards = []

    player1_card = player1.play_card()
    player2_card = player2.play_card()

    table_cards.append(player1_card)
    table_cards.append(player2_card)

    if player1_card[1] == player2_card[1]:
        war_count += 1

        print("War!")

        table_cards.extend(player1.play_war_card())
        table_cards.extend(player2.play_war_card())

        if RANKS.index(player1_card[1]) < RANKS.index(player2_card[1]):
            player2.hand.add_card(table_cards)
        else:
            player1.hand.add_card(table_cards)
    
    else:
        if RANKS.index(player1_card[1]) < RANKS.index(player2_card[1]):
            player2.hand.add_card(table_cards)
        else:
            player1.hand.add_card(table_cards)

print("Game Over! Number of rounds: " + str(total_rounds) + " War happened " + str(war_count) + " times")
print("Player 1 has: " + str(len(player1.hand.cards)))
print("Player 2 has: " + str(len(player2.hand.cards)))