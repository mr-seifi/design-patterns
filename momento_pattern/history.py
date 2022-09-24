class History:
    _states = []

    def push(self, state):
        self._states.append(state)
    
    def pop(self):
        return self._states.pop()
