from abc import ABC, abstractmethod


class Compressor(ABC):

    @abstractmethod
    def compress():
        ...
    

class JPGCompressor(Compressor):

    def compress():
        print('JPG compressed!')


class PNGCompressor(Compressor):

    def compress():
        print('PNG compressed!')
