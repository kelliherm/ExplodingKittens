import deck, player

class Game():
    def __init__(self, players=[], advanced=False):
        self.players = players
        self.numplayers = len(players)
        self.advanced = advanced
        self.deck = deck.Deck(self.numplayers)

        self.gameover = False

        if self.numplayers < 2 or self.numplayers > 5:
            raise ValueError('The game may only be played with 2-5 players')

        self.DealCards()
    
    def DealCards(self):
        for card in range(4):  # Deals random cards to each player (no defuses)
            for player in self.players:
                player.DrawCard(self.deck.DrawCard())
        
        for player in self.players:  # Deals a defuse card to each player
            player.DrawCard(deck.Card(1))
        
        self.deck.AddExtras()  # Adds extra defuses and exploding kittens back into deck
        self.deck.ShuffleDeck()

    def PlayGame(self):
        pass

    def ExampleTurn(self): # Uses the player at index 0 in players list
        pass