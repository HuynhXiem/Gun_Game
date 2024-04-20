class Player:
   def __init__(self, pos, isShot, startEnemyPos = 0, hp = 0):
      self.pos = pos
      self.hp = hp
      self.startEnemyPos = startEnemyPos
      self.isShot = isShot

   def print(self):
      print("Pos: ", self.pos, " isShot: ", self.isShot)

   def toString(self):
      return "Pos: " +  self.pos + " isShot: " + self.isShot