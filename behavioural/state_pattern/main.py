from state import State, Draft, Published


class Post:

    def __init__(self, text, state=State) -> None:
        self._state = state
        self.text = text

    def set_state(self, state: State):
        self._state = state
    
    @property
    def state(self) -> State:
        return self._state

    def render(self):
        self.state.render(self.text)


def main():

    post = Post('Post Text')
    
    post.set_state(Draft)
    post.render()

    post.set_state(Published)
    post.render()

    post.set_state(Draft)
    post.render()


if __name__ == '__main__':
    main()