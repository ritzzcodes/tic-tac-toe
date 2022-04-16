import numpy as np
import random
from time import sleep

def create_board():
  return (np.array([[0,0,0],[0,0,0],[0,0,0]]))
  
def possibilities(board):
  l=[]
  for i in range(len(board)):
    for j in range(len(board)):
      if board[i][j]==0:
        l.append((i,j))
  return l
  
def randomp(board,player):
  select=possibilities(board)
  current=random.choice(select)
  board[current]=player
  return board
  
def row(board,player):
  for x in range(len(board)):
    win=True
    for y in range(len(board)):
      if board[x,y]!=player:
        win=False
        continue
    if win==True:
      return win
  return win
      
def column(board,player):
  for x in range(len(board)):
    win=True
    for y in range(len(board)):
      if board[y][x]!=player:
        win=False
        continue
    if win==True:
      return win
  return win
  
def diag(board,player):
  win=True
  y=0
  for x in range(len(board)):
    if board[x,x]!=player:
      win=False
  if win:
    return win
  win=True
  if win:
    for x in range(len(board)):
      y=len(board)-1-x
      if board[x,y]!=player:
        win=False
  return win
  
def evaluate(board):
  winner=0
  for player in [1,2]:
    if (row(board,player) or column(board,player) or diag(board,player)):
      winner=player
  if np.all(board!=0) and winner==0:
    winner=-1
  return winner
  
def play():
  board,winner,counter=create_board(),0,1
  print(board)
  sleep(2)

  while winner==0:
    for player in [1,2]:
      board=randomp(board,player)
      print("board after" +str(counter)+ "move")
      print(board)
      sleep(2)
      counter+=1
      winner=evaluate(board)
      if winner!=0:
        break
  return winner

print("winner is"+ str(play()))
