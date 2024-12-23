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
        if self.value == 0:
            self.name = 'Exploding Kitten'
        elif self.value == 1:
            self.name = 'Defuse'
        elif self.value == 2:
            self.name = 'Nope'
        elif self.value == 3:
            self.name = 'See the Future'
        elif self.value == 4:
            self.name = 'Attack'
        elif self.value == 5:
            self.name = 'Skip'
        elif self.value == 6:
            self.name = 'Favor'
        elif self.value == 7:
            self.name = 'Shuffle'
        elif self.value == 8:
            self.name  = 'Tacocat'
        elif self.value == 9:
            self.name = 'Beard Cat'
        elif self.value == 10:
            self.name = 'Rainbow Cat'
        elif self.value == 11:
            self.name = 'Cattermelon'
        elif self.value == 12:
            self.name = 'Hairy Potato Cat'
    
    def ShowCard(self):
        print(self.name)
