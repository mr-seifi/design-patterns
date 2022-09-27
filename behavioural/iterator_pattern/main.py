from iterator import Iterator


class MyFiles:
    student_ids = [1, 2, 3, 4]

    def push(self, id: int) -> None:
        self.student_ids.append(id)
    
    def pop(self, id: int) -> int:
        return self.student_ids.pop()
    
    def create_iterator(self) -> Iterator:
        return Iterator[int](self.student_ids)


class MyFiles2:
    student_ids = {'Amin', 'Ali', 'Reza', 'Hossein'}

    def push(self, id: int) -> None:
        self.student_ids.append(id)
    
    def pop(self, id: int) -> int:
        return self.student_ids.pop()
    
    def create_iterator(self) -> Iterator:
        return Iterator[int](self.student_ids)


def main():
    my_files = MyFiles()

    it = my_files.create_iterator()
    print(it.current)

    it.next()
    print(it.current)

    my_files2 = MyFiles2()

    it = my_files2.create_iterator()
    print(it.current)

    it.next()
    print(it.current)


if __name__ == '__main__':
    main()