class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives
  
    def guess(self,n):
        if self.lives < 1:
            raise MyError('Expect error: "Omae wa mo shindeiru"')
        elif n==self.number:
            return True
        else:
            self.lives -=1
            return False