ranks = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]
class Warrior():
    def __init__(self):
        self.level = 1
        self.experience = 100
        self.rank = 'Pushover'
        self.achievements  = []
        
        
    def training(self, encounter):
        if self.level >= encounter[2]:
            self.achievements.append(encounter[0])
            self.experience += encounter[1]
            
            if self.experience> 10000:
                self.experience = 10000
            
            self.level = self.experience//100
            self.rank = ranks[self.level//10]
        
            return encounter[0]
        else:
            return "Not strong enough"
        
    def battle(self, level):
        if level>100 or level<1:
            return "Invalid level"
        if ranks.index(self.rank) + 1 <= level//10 and self.level + 5 <= level:
            return "You've been defeated"

        diff  = self.level - level
        
        if diff == 1:
            self.experience += 5
        elif diff == 0:
            self.experience += 10
        elif diff > 1:
            self.experience += 0
        else:
            self.experience += 20*diff*diff
    
        if self.experience> 10000:
            self.experience = 10000

        self.level = self.experience//100
        self.rank = ranks[self.level//10]
            
        if diff == 0 or diff == 1:
            return "A good fight"
        elif diff>=2:
            return "Easy fight"
        else:
            return "An intense fight"