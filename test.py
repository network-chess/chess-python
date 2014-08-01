#!/usr/bin/python
import chess

game = newgame()
if game == None:
  sys.exit()
p1 = join(game)
if p1 == None:
  sys.exit()
p2 = join(game)
if p2 == None:
  sys.exit()

print "Game:", game
print "Player 1:", p1
print "Player 2:", p2

make_move(p1, "a2a4")
make_move(p2, "a7a5")

print
print "Move log:"
print get(game)
