class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0
        

    def inc_progress(self, n):
        diff = 0
        if n >=9 or n<=-9 or n == 0:
            raise
        if self.rank < 8:
            if (n >= 1 and self.rank<=-1) or (n<=-1 and self.rank>=1):
                diff = abs(n-self.rank) -1
            else:
                diff = abs(n-self.rank)

            if n > self.rank:
                d = 0
                if n >= 1 and self.rank<=-1:
                    d = abs(self.rank - n) - 1
                else:
                    d = abs(self.rank - n)
                self.progress = self.progress + 10*d*d

            elif n == self.rank:
                self.progress = self.progress + 3
            elif diff >= 2:
                pass
            elif diff < 2:
                self.progress = self.progress + 1


            while self.progress >= 100:
                new_rank = self.rank + 1
                if new_rank == 0:
                    self.rank = new_rank + 1
                else:
                    self.rank = new_rank
                if self.rank>= 8:
                    self.progress = 0
                else:
                    self.progress = self.progress - 100