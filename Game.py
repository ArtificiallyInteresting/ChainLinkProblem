class Game:
    def __init__(self, maxStates):
        self._max = maxStates
        self._cache = {}

    def seenState(self, state):
        return self.getCacheKey(state) in self._cache

    def getCacheKey(self, state):
        priorStates = state[:-1]
        cacheKey = "|".join(str(x) for x in sorted(priorStates))
        cacheKey += "|" + str(state[-1])
        return cacheKey

    # My state is just the list of numbers which have already been visited
    def getInitialState(self):
        return list([x] for x in range(1, self._max+1))

    # Returns all of the next states I could potentially go to.
    def getNextStates(self, state):
        self._cache[self.getCacheKey(state)] = True
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
