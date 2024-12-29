import random

class Deck():
    def __init__(self, players):
        self.cards = []
        self.discard = []

        self.players = players

        self.BuildDeck()
        self.ShuffleDeck()
    
    def BuildDeck(self): 
        numberofcards = [0, 0, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4]

        for cardvalue in range(len(numberofcards)):
            for number in range(numberofcards[cardvalue]):
                self.cards.append(Card(cardvalue))

    def AddExtras(self):
        explodingkittens = self.players - 1
        for explodingkitten in range(explodingkittens):
            self.cards.append(Card(0))
        
        defuses = 2 if self.players == 2 else 6 - self.players
        for defuse in range(defuses):
            self.cards.append(Card(1))

    def ShuffleDeck(self):
        random.shuffle(self.cards)

    def DrawCard(self):
        return self.cards.pop(0)

    def ShowDeck(self):
        for card in self.cards:
            card.ShowCard()

    def ShowDiscard(self):
        for card in self.discard:
            card.ShowCard()

    def SeeTheFuture(self):
        for card in range(3):
            self.cards[card].ShowCard()
    
    def Discard(self, card):
        self.discard.append(card)


class Card():
    def __init__(self, value):
        self.value = value

        self.AssignName()

    def AssignName(self):
        cards = {
            0 : 'Exploding Kitten',
            1 : 'Defuse',
            2 : 'Nope',
            3 : 'See the Future',
            4 : 'Attack',
            5 : 'Skip',
            6 : 'Favor',
            7 : 'Shuffle',
            8 : 'Tacocat',
            9 : 'Beard Cat',
            10 : 'Rainbow Cat',
            11 : 'Cattermelon',
            12 : 'Hairy Potato Cat'
        }

        self.name = cards[self.value]
    
    def ShowCard(self):
        print(self.name)
