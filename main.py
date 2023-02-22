print("Welcome to a game of Tic Tac Toe\n")
print("Player 1 is X\nPlayer 2 is O\n\n")

# initial board
row1 = ["a", "b", "c"]
row2 = ["d", "e", "f"]
row3 = ["g", "h", "i"]
listoflists=[row1,row2,row3]

# prints initial board
print(row1)
print(row2)
print(row3)


# turns 1 to 8 while printing the board in between each turn



a=0
while a < 4:
  a=a+1
  turn1 = input("\n(Player 1)pick a spot: ")
  if (turn1 in row1[0]):
    row1[0]="X"
  elif (turn1 in row1[1]):
    row1[1]="X"
  elif (turn1 in row1[2]):
    row1[2]="X"
  elif (turn1 in row2[0]):
    row2[0]="X"
  elif (turn1 in row2[1]):
    row2[1]="X"
  elif (turn1 in row2[2]):
    row2[2]="X"
  elif (turn1 in row3[0]):
    row3[0]="X"
  elif (turn1 in row3[1]):
    row3[1]="X"
  else:
    row3[2]="X"
  print(row1)
  print(row2)
  print(row3)
  turn2 = input("\n(Player2)pick a spot: ")
  if (turn2 in row1[0]):
    row1[0]="O"
  elif (turn2 in row1[1]):
    row1[1]="O"
  elif (turn2 in row1[2]):
    row1[2]="O"
  elif (turn2 in row2[0]):
    row2[0]="O"
  elif (turn2 in row2[1]):
    row2[1]="O"
  elif (turn2 in row2[2]):
    row2[2]="O"
  elif (turn2 in row3[0]):
    row3[0]="O"
  elif (turn2 in row3[1]):
    row3[1]="O"
  else:
    row3[2]="O"
  print(row1)
  print(row2)
  print(row3)


# turn # 9(last turn in the game)
turn1 = input("\n(Player 1)pick a spot: ")
if (turn1 in row1[0]):
  row1[0]="X"
elif (turn1 in row1[1]):
  row1[1]="X"
elif (turn1 in row1[2]):
  row1[2]="X"
elif (turn1 in row2[0]):
  row2[0]="X"
elif (turn1 in row2[1]):
  row2[1]="X"
elif (turn1 in row2[2]):
  row2[2]="X"
elif (turn1 in row3[0]):
  row3[0]="X"
elif (turn1 in row3[1]):
  row3[1]="X"
else:
  row3[2]="X"
print(row1)
print(row2)
print(row3)

# The board has been filled. The game is over.
print("\nThe board has been filled. The game is over. Thanks for playing\n")
print(row1)
print(row2)
print(row3)





if (turn1==turn1==turn2==turn2):
  print("\nThat spot is already taken. Please try again")
  turn1=input("\n(Player2)pick a spot: ")
else: 
  turn1=input("\n(Player1)pick a spot: ")
