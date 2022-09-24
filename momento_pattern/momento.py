from copy import deepcopy


class Momento:

    def create_state(self):
        return deepcopy(self)

    def restore(self, state):
        _ = [setattr(self, key, val) for key, val in vars(state).items()]