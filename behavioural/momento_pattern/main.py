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
    editor.save_state()

    editor.title = 'Title2'
    editor.save_state()

    editor.title = 'Title3'
    print(editor)

    editor.undo()
    print(editor)

    editor.undo()
    print(editor)


if __name__ == '__main__':
    main()