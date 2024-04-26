class Player:
   def __init__(self, pos, isShot, player = 0, startEnemyPos = 0):
      self.pos = pos
      self.player = player
      self.startEnemyPos = startEnemyPos
      self.isShot = isShot

   def print(self):
      print("Pos: ", self.pos, " isShot: ", self.isShot, "  player: ", self.player)

   def toString(self):
      return "isShot: " + self.isShot