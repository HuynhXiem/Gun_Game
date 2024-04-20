import socket
import sys
import pickle
import time
from models.player import Player
from _thread import *

#192.168.1.119
HOST = "192.168.2.6" #loopback
SERVER_PORT = 20000 
FORMAT = "utf-8"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

try:
   s.bind((HOST, SERVER_PORT))

except socket.error as e:
   str(e)

s.listen(2)

print("Waiting for client connection")

pos = [(300,400), (500,400)]
players = [Player(pos[0], False, 500) , Player(pos[1], False, 300)]


def threaded_client(conn, player) :
   conn.send(pickle.dumps(players[player]))
   reply = ""
   counter = 0

   while True:
      if counter == 50:
         try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
               print("Disconnected")
               break
            else:
               if player == 1:
                  reply = players[0]
               else:
                  reply = players[1]
                  # print("Received ", player,": ", data.print())
                  # print("Sending ", player, ": ", reply.print())
               
            conn.sendall(pickle.dumps(reply))
         except:
            break
         counter = 0

      counter +=1
      # time.sleep(0.05)


currentPlayer = 0
while True:
   conn, addr = s.accept()
   print("Connected to: ", addr)

   start_new_thread(threaded_client, (conn, currentPlayer % 2))
   currentPlayer += 1

   print(currentPlayer)