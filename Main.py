import Game
import datetime
# This should maybe be taken in as a command line argument, but meh
# Represents the number we are going up to
# maxStates = 100
for maxStates in range(1, 100):
    print("Max States is " + str(maxStates))
    game = Game.Game(maxStates)
    states = game.getInitialState()
    # states.remove([43])
    # states.append([43])
    before = datetime.datetime.now()
    print("before starting: " + str(before))
    bestRoute = []
    while len(states) > 0:
        state = states.pop()
        if game.seenState(state):
            continue
        for newState in game.getNextStates(state):
            if (newState == None):
                continue
            if len(newState) > len(bestRoute):
                bestRoute = newState
                # print("New best route! Length: " + str(len(bestRoute)) + ", Route: " + str(bestRoute))
            states.append(newState)

    # print("after: " + str(datetime.datetime.now()))
    print("Time Taken: " + str(datetime.datetime.now() - before))
    print("Winner: " + str(bestRoute))
    print("Length: " + str(len(bestRoute)))