#!/usr/bin/python
import urllib, sys

_chess_do_debug = False

def debug(value):
  global _chess_do_debug
  _chess_do_debug = value
  if _chess_do_debug:
    print "Debugging messages on"

def debug_print(string):
  global _chess_do_debug
  if _chess_do_debug:
    print string

class Player:
  def __init__(self, game, pid):
    self.game = game
    self.pid = pid

  #TODO: Warn if not the player's turn, other errors
  def make_move(self, move):
    # True on move success, False on move failure
    response = urllib.urlopen(self.game.site+self.game.gid+"/"+self.pid+"/"+move).read()
    debug_print(response)
    if response == "GOOD":
      return True
    else:
      return False

  def poll(self):
    # Return False if there's no new move, and the move if there is one
    response = urllib.urlopen(self.game.site+self.game.gid+"/"+self.pid).read()
    debug_print(response)
    if response == "NO NEW MOVE":
      return False
    else:
      return response.split("\n")[1]

class Game:
  def __init__(self, game_id = "", site="http://54.186.49.211:3000/"):
    self.site=site
    if game_id == "":
      response = urllib.urlopen(site+"new").read()
      debug_print(response)
      if response == "ERROR CREATING":
            self.gid = None
      else: # Strip off "GOOD"
            self.gid = response.split("\n")[1]
    else:
      debug_print("Game ID = " + game_id)
      self.gid = game_id

  def join(self):
    response = urllib.urlopen(self.site+self.gid+"/join").read()
    debug_print(response)
    response = response.split("\n")
    if response[0] == "WHITE" or response[0] == "BLACK":
      return Player(self, response[1])
    else:
      return None

  def get(self):
    # None if game isn't ready to be listed, a transcript if it is
    response = urllib.urlopen(self.site+self.gid).read()
    debug_print(response)
    if response == "NO SUCH GAME": # TODO: Add more error conditions
      return None
    else:
      return response
