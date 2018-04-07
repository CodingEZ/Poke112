class TA():
    def __init__(self):
        self.type = 
        self.health = 
        self.attack = 
        self.defense =
        self.speed = 
        self.moveSet = {move1, move2, move3, move4}

    def attack(self, move, target):
        target.loseHealth(move.power)      # need to calculate damage

    def loseHealth(self, power):
        self.health -= power

class Eugene(TA):
    def __init__(self):
        super.__init__()
        self.moveSet.add(specialMove)
    
