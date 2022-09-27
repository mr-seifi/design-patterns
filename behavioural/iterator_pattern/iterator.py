from typing import Generic, TypeVar


T = TypeVar('T')
class Iterator(Generic[T]):

    _current = None

    def __init__(self, data) -> None:
        self.data = data
        self.iter = iter(data)
        
        self.next()

    def next(self) -> None:
        self._current = next(self.iter, None)
    
    @property
    def current(self) -> T:
        return self._current
    
    def is_done(self) -> bool:
        return self._current == None