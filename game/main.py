import player, game

player1 = player.Player()
player2 = player.Player()
player3 = player.Player()
player4 = player.Player()

players = [player1, player2, player3, player4]

myGame = game.Game(players)

for player in players:
    print(player)
    player.ShowHand()