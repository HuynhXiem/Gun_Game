import socket
from _thread import *
import sys

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

def read_pos(str):
   str = str.split(",")
   return int(str[0]), int(str[1])

def make_pos(tup):
   return str(tup[0]) + "," + str(tup[1])

pos = [(500,350), (300,350)]


def threaded_client(conn, player) :
   startPos = (300,500)
   if player % 2 != 0:
      startPos = (startPos[1], startPos[0])
   conn.send(str.encode(make_pos(startPos)))
   reply = ""
   counter = 0

   while True:
      try:
         data = read_pos(conn.recv(2048).decode())
         pos[player] = data

         if not data:
            print("Disconnected")
            break
         else:
            if player == 1:
               reply = pos[0]
            else:
               reply = pos[1]

            if counter == 100:
               print("Received ", player,": ", data)
               print("Sending ", player, ": ", reply)
               counter = 0
            
            counter += 1

         conn.sendall(str.encode(make_pos(reply)))
      except:
         break


currentPlayer = 0
while True:
   conn, addr = s.accept()
   print("Connected to: ", addr)

   start_new_thread(threaded_client, (conn, currentPlayer % 2))
   currentPlayer += 1

   print(currentPlayer)