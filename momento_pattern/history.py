class History:
    states = []

    def push(self, state):
        self.states.append(state)
    
    def pop(self):
        return self.states.pop()
