from history import History
from momento import Momento


class Editor(Momento):
    
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __str__(self) -> str:
        return f'{self.title}-{self.content}'


def main():
    
    editor = Editor('Title1', 'Content1')
    history = History()

    history.push(editor.create_state())
    editor.title = 'Title2'

    history.push(editor.create_state())

    editor.title = 'Title3'
    print(editor)

    editor.restore(history.pop())
    print(editor)

    editor.restore(history.pop())
    print(editor)


if __name__ == '__main__':
    main()