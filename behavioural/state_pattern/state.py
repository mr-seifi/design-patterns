from abc import ABC, abstractmethod


class State(ABC):

    @abstractmethod
    def render(text: str):
        pass


class Draft(State):

    def render(text: str):
        print('draft: ', text)


class Published(State):

    def render(text: str):
        print(text)
