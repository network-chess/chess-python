#!/usr/bin/python
import chess

game = chess.Game()
if game == None:
  sys.exit()
p1 = game.join()
if p1 == None:
  sys.exit()
p2 = game.join()
if p2 == None:
  sys.exit()

print "Game:", game
print "Player 1:", p1
print "Player 2:", p2

p1.make_move("a4")
p2.make_move("a5")

print
print "PGN:"
print game.get()
