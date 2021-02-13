import random as r
import nom3

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

def makgora():



def melee():
    ## 플레이어 생성
    a = PlayerA
    b = PlayerB
    c = PlayerC

    player = [a, b, c]

    if r.randrange(1,2) > 1:
        a.shot(b)
    else:
        a.shot(c)
    
    if r.randrange(1,2) > 1:
        b.shot(c)
    else:
        b.shot(a)

    if r.randrange(1,2) > 1:
        c.shot(a)
    else:
        c.shot(b)