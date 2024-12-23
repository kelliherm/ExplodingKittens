import deck, player

class Game():
    def __init__(self, players=[], advanced=False):
        self.players = players
        self.numplayers = len(players)
        self.advanced = advanced
        self.deck = deck.Deck(self.numplayers)

        self.DealCards()
    
    def DealCards(self):
        for card in range(4):
            for player in self.players:
                player.DrawCard(self.deck.DrawCard())
        
        for player in self.players:
            player.DrawCard(deck.Card(1))
        
        self.deck.AddExtras()
        self.deck.ShuffleDeck()