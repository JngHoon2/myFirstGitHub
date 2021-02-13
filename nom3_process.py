import random as r

class Player:

    #life
    state = True
    accuracy = 0

    def shot(self):

        percentage = r.random()
        
        if percentage < self.accuracy or percentage == self.accuracy:
            self.state = False
        else:
            pass
        

class PlayerA(Player):
    
    __identity = 'A'
    accuracy = 0.3
    
class PlayerB(Player):
    
    __identity = 'B'
    accuracy = 0.5

class PlayerC(Player):
    
    __identity = 'C'
    accuracy = 0.5


a = PlayerA
b = PlayerB

a.shot(b)

print(b.state)