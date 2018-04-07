class Move(pygame.sprite.Sprite):

    def damage(self, attacker, defender):
        attackerType = attacker.type
        defenderType = defender.type
        attack = attacker.attack
        defense = defender.defense
        movePower = self.power
        moveType = self.type
        STAB = 1
        typeAdv = self.typeAdvCalc(attackerType, defenderType)
        if attackerType == moveType:
            STAB = 1.5
        damage = .44 * movePower * (attack/defense) * typeAdv * STAB
        return damage
            
    def typeAdvCalc(self, defenderType):
        moveType = self.type
        if moveType == "water" and defenderType == "water":
            typeAdv = .5
        elif moveType == "water" and defenderType == "grass":
            typeAdv = .5
        elif moveType == "water" and defenderType == "fire":
            typeAdv = 2
        elif moveType == "grass" and defenderType == "water":
            typeAdv = 2
        elif moveType == "grass" and defenderType == "grass":
            typeAdv = .5
        elif moveType == "grass" and defenderType == "fire":
            typeAdv = .5
        elif moveType == "fire" and defenderType == "water":
            typeAdv = .5
        elif moveType == "fire" and defenderType == "grass":
            typeAdv = 2
        elif moveType == "fire" and defenderType == "fire":
            typeAdv = .5
        else:
            typeAdv = 1
        return typeAdv
            
### STUDENT MOVES ###
            
class RegradeReq(Move):
    def __init__(self):
        self.power = 42
        self.type = "water"
        self.animation = regradeAnimate()
        
    @staticmethod
    def regradeAnimate():
        def init(data):
            data.hands = pygame.image.load('prayemoji.png').convert()
            data.imgW = 100
            data.imgH = 100
            data.rect = data.hands.get_rect()
            data.counter = 0
        
        def draw(data):
            while data.counter < 3:
                data.x = random.randint(0, width/2-data.imgW)
                data.y = random.randint(0, height/2-data.imgH)
                data.rect.center = (data.x, data.y)
                gameDisplay.blit(data.hands, (data.x, data.y))
                pygame.display.flip()
                time.sleep(.25)
                data.counter +=1
            data.counter = 0
    
        class Struct(object): pass
        data = Struct()
        init(data)
        draw(data)
        
class ThreeAMPiazza(Move):
    def __init__(self):
        self.power = 60
        self.type = 'water'
        
class Sleep(Move):
    def __init__(self):
        self.power = 0
        attacker.health += 30
        self.type = "grass"
        self.animation = sleepAnimate()
        
    @staticmethod
    def sleepAnimate():
        def init(data):
            data.zs = pygame.image.load('zs.png')
            data.imgW = 100
            data.imgH = 100
            data.rect = data.zs.get_rect()
            data.y = height/2
            data.x = width/4
            data.vel = 10
            data.animSize = 50
            data.counter = 0
            
        def draw(data):
            while data.counter <= 1:
                pygame.draw.rect(gameDisplay, (0,0,255), (0,0,800,600))
                gameDisplay.blit(data.zs, (data.x, data.y))
                pygame.display.flip()
                if data.x+data.vel < width/3:
                    data.x += data.vel
                    data.y -= data.vel
                else:
                    data.y = height/2
                    data.x = width/4
                time.sleep(.2)
                data.counter += .1
            data.counter = 0
        
        class Struct(object): pass
        data = Struct()
        init(data)
        draw(data)
        
class OHQueue(Move):
    def __init__(self, attacker):
        self.power = 0
        attacker.attack +=3
        self.type='grass'
        
### TA MOVES ###
        
class Style(Move):
    def __init__(self, defender):
        defender.health -= 2
        
class FixProjector(Move):
    def __init__(self):
        self.power = 30
        self.type = 'grass'
        
class VagueAnswers(Move):
    def __init__(self):
        attacker.defense += 3
        
class Clap(Move):
    def __init__(self):
        self.power = 42
        self.type = 'fire'
        
### PROFESSOR MOVES ###

class DebugInClass(Move):
    def __init__(self):
        self.power = 30
        self.type = 'grass'
        
class LongLecture(Move):
    def __init__(self, attacker):
        attacker.attack += 3
        
class Recursion(Move):
    def __init__(self):
        self.power = 60
        self.type = 'fire'
    
class BypassPiazza(Move):
    def __init__(self):
        self.power = 30
        self.type = 'grass'
        self.animation = bypassAnimate()
        
    @staticmethod
    def bypassAnimate():
        def init(data):
            data.imgW = 200
            data.imgH = 43
            data.notification = pygame.image.load('piazzasmall.png')
            data.rect = data.notification.get_rect()
            data.counter = 0
        def draw(data):
                while data.counter < 5:
                    data.x = random.randint((width*3/4)-100, width-data.imgW)
                    data.y = random.randint(height/4, height*3/4)
                    data.rect.center = (data.x, data.y)
                    gameDisplay.blit(data.notification, (data.x, data.y))
                    pygame.display.flip()
                    time.sleep(.2)
                    data.counter +=1
                data.counter = 0
            
        class Struct(object): pass
        data = Struct()
        init(data)

        draw(data)
