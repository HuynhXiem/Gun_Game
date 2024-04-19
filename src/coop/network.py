import socket

HOST = "192.168.2.6"
SERVER_PORT = 20000
FORMAT = "utf-8"

class Network:
   def __init__(self):
      self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.server = HOST
      self.port = SERVER_PORT
      self.addr = (self.server,self.port)
      self.pos = self.connect()
      print(self.pos)

   def getPos(self):
      return self.pos

   def connect(self):
      try:
         self.client.connect(self.addr)
         return self.client.recv(2048).decode()
      except:
         pass
   
   def send(self, data):
      try:
         self.client.send(str.encode(data))
         return self.client.recv(2048).decode()
      except socket.error as e:
         print(e)

   def closeConnection(self):
      self.client.close()