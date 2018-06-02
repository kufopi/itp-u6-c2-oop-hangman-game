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
    def __init__(self,word):
        
        if len(word) == 0:
            raise InvalidWordException()
        
        self.answer = word
        self.masked = '*' * len(self.answer)
        
        
    def discovery(self,  chara ):
       
        holder = ''
        for j in range(len(self.answer)):
            wordLetter = self.answer[j].lower()
            maskedLetter =self. masked[j]
    
            if maskedLetter != '*':
                holder += maskedLetter
            elif chara.lower() == wordLetter:
                holder += wordLetter
    
            else:
                holder += '*'
        return holder    
    
    
    
        
    def perform_attempt (self, chara):
        if len(chara)>1:
            raise InvalidGuessedLetterException()
            
        
            
        if chara.lower() in self.answer.lower():
            
            self.masked = self.discovery( chara)
            
            return GuessAttempt(chara, hit=True )
        else:
            return GuessAttempt(chara, miss=True )
        


class HangmanGame(object):
    pass
