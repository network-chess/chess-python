#!/usr/bin/python
import urllib, sys

_chess_do_debug = False

def debug(value):
    global _chess_do_debug
    _chess_do_debug = value
    if _chess_do_debug:
      print "Debugging messages on"

class Player:
  def __init__(self, game, pid):
    self.game = game
    self.pid = pid

  #TODO: Warn if not the player's turn, other errors
  def make_move(self, move):
    global _chess_do_debug
    # True on move success, False on move failure
    response = urllib.urlopen(self.game.site+self.game.gid+"/"+self.pid+"/"+move).read()
    if _chess_do_debug:
      print response
    if response == "GOOD":
      return True
    else:
      return False

  def poll(self):
    global _chess_do_debug
    # Return False if there's no new move, and the move if there is one
    response = urllib.urlopen(self.game.site+self.game.gid+"/"+self.pid).read()
    if _chess_do_debug:
      print response    
    if response == "NO NEW MOVE":
      return False
    else:
      return response.split("\n")[1]

class Game:
  def __init__(self, game_id = "", site="http://54.186.49.211:3000/"):
    global _chess_do_debug
    self.site=site
    if game_id == "":
      response = urllib.urlopen(site+"new").read()
      if _chess_do_debug:
        print response
      if response == "ERROR CREATING":
        self.gid = None
      else: # Strip off "GOOD"
        self.gid = response.split("\n")[1]
    else:
      self.gid = game_id

  def join(self):
    global _chess_do_debug
    response = urllib.urlopen(self.site+self.gid+"/join").read()
    response = response.split("\n")
    if _chess_do_debug:
      print response
    if response[0] == "WHITE" or response[0] == "BLACK":
      return Player(self, response[1])
    else:
      return None

  def get(self):
    global _chess_do_debug
    # None if game isn't ready to be listed, a transcript if it is
    response = urllib.urlopen(self.site+self.gid).read()
    if _chess_do_debug:
      print response
    if response == "NO SUCH GAME": # TODO: Add more error conditions
      return None
    else:
      return response
