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
