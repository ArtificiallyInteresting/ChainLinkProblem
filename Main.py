import Game
import datetime
# This should maybe be taken in as a command line argument, but meh
# Represents the number we are going up to
maxStates = 100
game = Game.Game(maxStates)
states = []
states.append(game.getInitialState())
before = datetime.datetime.now()
print("before starting: " + str(before))
bestRoute = []
while len(states) > 0:
    state = states.pop()
    for newState in game.getNextStates(state):
        if (newState == None):
            continue
        if len(newState) > len(bestRoute):
            bestRoute = newState
        states.append(newState)

print("after: " + str(datetime.datetime.now()))
print("diff: " + str(datetime.datetime.now() - before))
print("Winner: " + str(bestRoute))
print("Length: " + str(len(bestRoute)))