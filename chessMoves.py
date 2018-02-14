import argparse, json

chessBoard = [[1] * 8 for i in range(8)]
# print (chessBoard)

chess_map_from_alpha_to_index = {
  "a" : 0,
  "b" : 1,
  "c" : 2,
  "d" : 3,
  "e" : 4,
  "f" : 5,
  "g" : 6,
  "h" : 7
}
chess_map_from_index_to_alpha = {
  0 : "a",
  1 : "b",
  2 : "c",
  3 : "d",
  4 : "e",
  5 : "f",
  6 : "g",
  7 : "h"
}

def getRookMoves(pos, chessBoard):
  column, row = list(pos.strip().lower())
  row = int(row) - 1
  column = chess_map_from_alpha_to_index[column]
  possibleMoves = []

  for j in range(8):
    if(j != column):
      possibleMoves.append((row, j))
  
  for i in range(8):
    if(i != row):
      possibleMoves.append((i, column))
  possibleMoves = ["".join([chess_map_from_index_to_alpha[i[1]], str(i[0] + 1)]) for i in possibleMoves]
  possibleMoves.sort()
  return possibleMoves
  #print("\n--->  Rook's: \t\t", possibleMoves)

def getBishopMoves(pos, chessBoard):
  column, row = list(pos.strip().lower())
  row = int(row) - 1
  column = chess_map_from_alpha_to_index[column]
  possibleMoves = []
  
  x, y = row, column

  #    First Direction!
  x1 = x - 1
  y1 = y - 1
  while (x1 > 0 and y1 > 0):
    possibleMoves.append((x1, y1))
    y1 -= 1
    x1 -= 1

  #  Second Direction!
  x1 = x + 1
  y1 = y - 1
  while(x1 <= 7 and y1 > 0):
    possibleMoves.append((x1, y1))
    x1 = x1 + 1
    y1 = y1 - 1

  #  Third Direction!
  x1 = x + 1
  y1 = y + 1
  while(x1 <= 7 and y1 <= 7):
    possibleMoves.append((x1, y1))
    x1 = x1 + 1
    y1 = y1 + 1

  #  Fourth Direction!
  x1 = x - 1
  y1 = y + 1
  while(x1 > 0 and y1 <= 7):
    possibleMoves.append((x1, y1))
    x1 = x1 - 1
    y1 = y1 + 1
  possibleMoves = ["".join([chess_map_from_index_to_alpha[i[1]], str(i[0] + 1)]) for i in possibleMoves]
  possibleMoves.sort()
  print("\n--->  Bishop's: \t", possibleMoves)

def getKnightMoves(pos, chessBoard):
  i, j = row, column
  possibleMoves = [(i-1, j-2),
                   (i-2, j-1),
                   (i-2, j+1),
                   (i-1, j+2),
                   (i+1, j-2),
                   (i+1, j+2),
                   (i+2, j-1),
                   (i+2, j+1)
                  ] 
  print("\n--->  Knight's: \t", possibleMoves) 
  
def getQueenMoves(pos, chessBoard):
  # i, j = row, column
  column, row = list(pos.strip().lower())
  row = int(row) - 1
  column = chess_map_from_alpha_to_index[column]
  possibleMoves = []

  # Moves including same row
  for j in range(8):
    if(j != column):
      possibleMoves.append((row, j))
  
  # Moves including same column block
  for i in range(8):
    if(i != row):
      possibleMoves.append((i, column))
  x, y = row, column

  #    First Direction!
  x1 = x - 1
  y1 = y - 1
  while (x1 > 0 and y1 > 0):
    possibleMoves.append((x1, y1))
    y1 -= 1
    x1 -= 1

  #  Second Direction!
  x1 = x + 1
  y1 = y - 1
  while(x1 <= 7 and y1 > 0):
    possibleMoves.append((x1, y1))
    x1 = x1 + 1
    y1 = y1 - 1

  #  Third Direction!
  x1 = x + 1
  y1 = y + 1
  while(x1 <= 7 and y1 <= 7):
    possibleMoves.append((x1, y1))
    x1 = x1 + 1
    y1 = y1 + 1

  #  Fourth Direction!
  x1 = x - 1
  y1 = y + 1
  while(x1 > 0 and y1 <= 7):
    possibleMoves.append((x1, y1))
    x1 = x1 - 1
    y1 = y1 + 1
  possibleMoves = ["".join([chess_map_from_index_to_alpha[i[1]], str(i[0] + 1)]) for i in possibleMoves]
  possibleMoves.sort()
  print("\n--->  Queen's: \t\t", possibleMoves)

def main():
  print("\n\n----------------------Chess Moves Generator-------------------\n\n")

  # Taking data via arguments
  parser = argparse.ArgumentParser()
  parser.add_argument("-p", "--piece", help = "Chess piece name. for eg:- Rook, Bishop, Knight, Queen")
  parser.add_argument("-pos", "--position", help = "Position of the entered piece in chess notation string. for eg:- E4, D5  etc.")
  args = parser.parse_args()

  # Breaking arguments into usable form
  piece = args.piece.strip().lower()
  location = args.position.strip()

  # Call functions according to the piece and also passing their location 
  if(piece == "rook"):
    print(json.dumps({
      "piece" : piece,
      "location" : location,
      "Possible Moves" : getRookMoves(location, chessBoard)
    }))
  
  elif(piece == "bishop"):
    print(json.dumps({
      "piece" : piece,
      "location" : location,
      "Possible Moves" : getBishopMoves(location, chessBoard)
    }))

  elif(piece == "knight"):
    print(json.dumps({
      "piece" : piece,
      "location" : location,
      "Possible Moves" : getKnightMoves(location, chessBoard)
    }))

  elif(piece == "queen"):
    print(json.dumps({
      "piece" : piece,
      "location" : location,
      "Possible Moves" : getQueenMoves(location, chessBoard)
    }))

if __name__ == "__main__":
  main()