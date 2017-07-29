class Game:
    def __init__(self, maxStates):
        self._max = maxStates

    # My state is just the list of numbers which have already been visited
    def getInitialState(self):
        return []

    # Returns all of the next states I could potentially go to.
    def getNextStates(self, state):
        # State is empty, return all possible states
        if (len(state) == 0):
            return ([x] for x in range(1, self._max+1))
        currentNo = state[-1]
        allStates = range(1, self._max+1)
        nextStates = []
        for potentialState in allStates:
            # Pass if this is already in our history
            if potentialState in state:
                continue
            # Pass if this isn't a multiple or factor
            if not potentialState % currentNo == 0 and not currentNo % potentialState == 0:
                continue
            nextStates.append(state + [potentialState])
        return nextStates
