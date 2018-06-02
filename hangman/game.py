from .exceptions import *


class GuessAttempt(object):
    
    def __init__(self, chara, hit = None, miss = None):
        self.chara = chara
        self.hit =hit
        self.miss = miss
        
        if  hit is True and  miss is True:
            raise InvalidGuessAttempt()
    
    def is_hit(self):
        if self.hit == True:
            return True
        return False
        
        
        
    def is_miss(self):
        if self.miss == True:
            return True
        return False
        


class GuessWord(object):
    pass


class HangmanGame(object):
    pass
