import socket
import pickle

HOST = "192.168.2.6"
SERVER_PORT = 20000
FORMAT = "utf-8"
TIMEOUT = 1

class Network:
   def __init__(self):
      self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.server = HOST
      self.port = SERVER_PORT
      self.addr = (self.server,self.port)
      self.player = self.connect()

   def getPlayer(self):
      return self.player

   def connect(self):
      try:
         self.client.connect(self.addr)
         return pickle.loads(self.client.recv(2048))
      except:
         pass

   def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            response = self.receive_with_timeout()
            if response:
                return pickle.loads(response)
            else:
                print("No response received.")
                return None
        except socket.error as e:
            print("Socket error:", e)

   def receive_with_timeout(self):
        self.client.settimeout(TIMEOUT)
        try:
            response = self.client.recv(2048)
            return response
        except socket.timeout:
            print("Timeout occurred while waiting for response.")
            return None

   def closeConnection(self):
      self.client.close()