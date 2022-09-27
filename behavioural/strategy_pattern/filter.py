from abc import ABC, abstractmethod


class Filter(ABC):

    @abstractmethod
    def apply():
        ...


class BWFilter(Filter):

    def apply():
        print('Black & White applied!')


class HighContrastFilter(Filter):

    def apply():
        print('High Contrast applied!')