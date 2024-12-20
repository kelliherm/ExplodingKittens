from card import Card
import random

class Deck():
    def __init__(self, players):
        self.cards = []
        self.discard = []

        self.players = players

        self.BuildDeck()
        self.ShuffleDeck()
    
    def BuildDeck(self):
        defuses = 6 - self.players
        if self.players == 2:
            defuses = 2        
        numberofcards = [self.players - 1, defuses, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4]

        for cardvalue in range(len(numberofcards)):
            for number in range(numberofcards[cardvalue]):
                self.cards.append(Card(cardvalue))
    
    def ShuffleDeck(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

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
