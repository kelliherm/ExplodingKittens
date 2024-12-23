class Player():
    def __init__(self):
        self.hand = []
    
    def DrawCard(self, card):
        self.hand.append(card)
    
    def ShowHand(self):
        for card in self.hand:
            card.ShowCard()