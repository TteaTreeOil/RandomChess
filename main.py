import chess
import chess.pgn
import random

board = chess.Board()
game = chess.pgn.Game()
whitesTurn = True
moveNumber = 0
node = game

while True:
  legalMoves = list(board.legal_moves)
  randomMove = random.choice(legalMoves)
  board.push_san(str(randomMove))
  node = node.add_variation(randomMove)
  
  print(board)
  moveNumber = moveNumber + 1
  print(moveNumber)
  
  if board.is_stalemate():
    print("1/2-1/2 \n Stalemate! \n \n \n")
    print(game)
    break
  elif board.is_insufficient_material():
      print("1/2-1/2 \n Draw, insufficient material! \n \n \n")
      print(game)
      break
  elif board.is_checkmate():
    if whitesTurn == True:
      print("0-1 \n Checkmate, black wins! \n \n \n")
      print(game)
      break
    else:
      print("1-0 \n Checkmate, white wins! \n \n \n")
      print(game)
      break