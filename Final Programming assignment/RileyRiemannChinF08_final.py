import random 
from libdw import sm

class Card:
    def __init__(self,suit,val):
        self.suit = suit
        self.value = val

    def __str__(self):
        return "{} of {}".format(self.value,self.suit)

class Deck:
    def __init__(self): #initializes the deck when it is called
        self.cards = []
        self.create_deck()
        self.shuffle()

    def create_deck(self): #creates a deck of cards in a specific order
        card_list=["Clubs","Diamonds","Hearts","Spades"]
        for suit in card_list:
            for value in range(1,14):
                if value <= 10:
                    if value == 1:
                        self.cards.append(Card(suit,"Ace"))
                    else:
                        self.cards.append(Card(suit,value))
                else:
                    if value == 11: 
                        self.cards.append(Card(suit,"Jack"))
                    if value == 12:
                        self.cards.append(Card(suit,"Queen"))
                    if value == 13:
                        self.cards.append(Card(suit,"King"))
    def show(self):
        print(len(self.cards))
        for card in self.cards:
            print(card)


    def shuffle(self):
        shuffled = []
        for i in range(len(self.cards)):
            shuffled.insert(random.randint(0,i),self.cards[i])
        self.cards = shuffled
    
    def drawCard(self):
        return self.cards.pop()

class Player:
    def __init__(self,name):
        self._name = name
        self._points = 500

    def get_points(self):
        return self._points
    
    def set_points(self,value):
        self._points = value

    def __str__(self):
        return self._name

    points = property(get_points,set_points)

class Game(sm.SM):
    def __init__(self):
        self.state = 0
        self.pot = 500 #equivalent of 10 chips, 1 chip is 50 points
        self.player = None

    def get_next_values(self,state,inp):
        next_state = state
        self.player.points += inp
        self.pot -= inp

        if inp <0:
            if self.player.points <=0:
                self.player.points = 0
                next_state = 0
                output = "You lost all your points! Better luck next time!"
            else:
                if self.high == self.low+1:
                    next_state = 1
                    output = "Unlucky! You currently have {} points! Pot is now {} points".format(self.player.points,self.pot)
                else:
                    next_state = 1
                    output = "It was not in between! You currently have {} points! Pot is now {} points".format(self.player.points,self.pot)
        elif inp > 0:
            if self.pot <=0:
                self.pot = 0
                next_state = 0
                output = "Congratulations! You won the pot!"
            else:
                if self.high == self.low:
                    next_state = 1
                    output = "You got lucky! You currently have {} points! Pot is now {} points".format(self.player.points,self.pot)
                else:
                    next_state = 1
                    output = "You won! You currently have {} points! Pot is now {} points ".format(self.player.points,self.pot)
            
        return (next_state,output)
    
    def main(self):
        print("-----------Welcome to in-between!-----------") #Step 1, player creates name and starts with 500 points
        name = input("Please input your player name: ")
        self.player = Player(name)
        print("Your name is {}, each player starts with 500 points\n".format(self.player))
        self.state = 1 #game has started
        round_counter = 1
        deck = Deck() #create a deck and draw the first 2 cards
        while self.state == 1:
            print("----------Round {}---------- ".format(round_counter))
            value_dictionary = {'Ace':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Jack':11,'Queen':12,'King':13}
            first_card = str(deck.drawCard())
            second_card = str(deck.drawCard())
            between_card = str(deck.drawCard())#check if the third card is in between and main conditions of the game

            for value in value_dictionary: #give value to cards
                if value in first_card:
                    v1 = value_dictionary[value]
                if value in second_card:
                    v2 = value_dictionary[value]
                if value in between_card:
                    v3 = value_dictionary[value]

            if v1 >v2: #see which is high and low
                self.high = v1
                self.low = v2
            else:
                self.high = v2
                self.low = v1
            
            need_bet = True#check if need to bet
            print('\n{:20.20s} {:20.20s}'.format(first_card,second_card)) #show the 2 cards and ask if want bet
            
            if self.high == self.low:
                results = self.step(100)
                print(results)
                need_bet = False
            elif self.high == self.low +1:
                results = self.step(-100)
                print(results)
                need_bet = False
            else:
                while need_bet == True: #check the bet amount
                    try:
                        bet = int(input("Please enter a bet amount: "))
                        if bet > self.player.points:
                            print("You can only bet up to a maximum of: {} points".format(self.player.points))
                        elif bet<=0:
                            print("You cannot bet less than or equal to 0 points")
                        elif bet > 0 and bet<50:
                            print("You must bet a minimum of 50 points")
                        else:
                            break
                    except:
                        print("Please enter an integer")

                print('\n{:20.20s} {:20.20s} {:20.20s}'.format(first_card,between_card,second_card))
                if self.low < v3 and v3 < self.high:
                    results = self.step(bet)
                    print(results)
                elif v3 == self.low or v3 == self.high:
                    results = self.step(-2*bet)
                    print(results)
                else:
                    results = self.step(-1*bet)
                    print(results)
            round_counter+= 1

if __name__ == "__main__":
    game = Game()
    game.start()
    game.main()
    Deck().show()
