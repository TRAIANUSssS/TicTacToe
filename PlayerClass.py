class Player:

    def __init__(self, name, move):
        self.name = name
        self.move = move

    def changeMove(self):
        if(self.move):
            self.move = False
        else:
            self.move = True