#!/usr/bin/python3

# Both the Minimax and the Alpha-beta algorithm represent the players
# as integers 0 and 1. The moves by the two players alternate 0, 1, 0, 1, ...,
# so in the recursive calls you can compute the next player as the subtraction
# 1-player.
# The minimizing player is always 0 and the maximizing 1.
# The number of recursive calls to the algorithms is kept track with
# the variable 'calls'. Let your implementation increase this variable
# by one in the beginning of each recursive call. This variable is
# also used as part of the evaluation of the implementations.

calls = 0

def minimax(player,state,depthLeft):
  """
  Perform recursive min-max search of a game tree rooted in `state`.
  
  Returns the best value in the min-max sense starting from `state` for `player`
  using at most `depthLeft`  recursive calls.

  Gives value of state if depthLeft = 0 or the state has no further actions 
  (a leaf in the game-tree).

  Parameters
  ----------
  player : int in {0,1}
     0 is the minimizing player, and 1 maximizing.
  state : Object representing game state. 
     See `gameexamples.py` for examples.
  depthLeft : int >= 0
     Maximum number of recursive levels to perform, including this this call to 
     minmax.

  Returns
  -------
  float
     Best value.

  """
  global calls
  calls += 1
  if depthLeft == 0:
    return state.value()
  ### INSERT YOUR IMPLEMENTATION OF MINIMAX HERE
  ### It should be recursively calling 'minimax'.
  if player == 0:
    player2 = 1
    best = float('inf')
  else:
    player2 = 0
    best = float('-inf')
  for a in state.applicableActions(player):
    state2 = state.successor(player,a)
    v = minimax(player2,state2,depthLeft-1)
    if player == 0:
      best = min(best,v)
    else:
      best = max(best,v)

  return best

def alphabeta(player,state,depthLeft,alpha,beta):
  """
  Perform recursive alpha/beta search of game tree rooted in `state`.

  Returns the best value in the alpha/beta sense starting from `state` for `player`
  using at most `depthLeft`  recursive calls.

  Gives value of state if depthLeft = 0 or the state has no further actions 
  (a leaf in the game-tree).

  Parameters
  ----------
  player : int in {0,1}
     0 is the minimizing player, and 1 maximizing.
  state : Object representing game state. 
     See `gameexamples.py` for examples.
  depthLeft : int >= 0
     Maximum number of recursive levels to perform, including this call to 
     alphabeta.
  alpha : float
     Current alpha cut value.
  beta : float
     Current beta cut value.

  Returns
  -------
  float
     Best value.
 
  """
  global calls
  calls += 1
  if depthLeft == 0:
    return state.value()
  ### INSERT YOUR IMPLEMENTATION OF ALPHABETA HERE
  ### It should be recursively calling 'alphabeta'.
  if player == 0:
    player2 = 1
    best = float('inf')
  else:
    player2 = 0
    best = float('-inf')
  for a in state.applicableActions(player):
    state2 = state.successor(player,a)
    v = alphabeta(player2,state2,depthLeft-1,alpha,beta)
    if player == 0:
      best = min(best,v)
      beta = min(beta,v)
    else:
      best = max(best,v)
      alpha = max(alpha,v)
    if alpha >= beta:
      break

  return best


def gamevalue(startingstate,depth):
  global calls
  calls = 0
  v = minimax(0,startingstate,depth)
  print(str(v) + " value with " + str(calls) + " calls with minimax to depth " + str(depth))
  calls = 0
  v = alphabeta(0,startingstate,depth,0-float("inf"),float("inf"))
  print(str(v) + " value with " + str(calls) + " calls with alphabeta to depth " + str(depth))
  calls = 0
