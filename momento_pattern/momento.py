from copy import deepcopy
from history import History


class Momento:

    __history = History()

    def __create_state(self):
        return deepcopy(self)

    def __restore(self, state):
        _ = [setattr(self, key, val) for key, val in vars(state).items()]

    def save_state(self):
        self.__history.push(self.__create_state())

    def undo(self):
        self.__restore(self.__history.pop())
