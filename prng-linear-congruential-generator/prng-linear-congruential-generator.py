import math
class LCG(object):
  a = 2
  c = 3
  m = 10
  def __init__(self, seed):
      self.seed = seed
  def random(self):
      self.seed = (self.a*self.seed+self.c)%self.m
      return self.seed/10 