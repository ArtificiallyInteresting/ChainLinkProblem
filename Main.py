import Game

# This should maybe be taken in as a command line argument, but meh
# Represents the number we are going up to
maxStates = 100
game = Game.Game(maxStates)
states = game.getInitialState()
bestRoute = []
while len(states) > 0:
    state = states.pop()
    if game.seenState(state):
        continue
    for newState in game.getNextStates(state):
        if len(newState) > len(bestRoute):
            bestRoute = newState
        states.append(newState)

print("Winner: " + str(bestRoute))
print("Length: " + str(len(bestRoute)))