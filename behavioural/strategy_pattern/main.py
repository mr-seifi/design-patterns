from compress import Compressor, JPGCompressor
from filter import Filter, HighContrastFilter



class ImageStorage:

    def __init__(self, compressor: Compressor, filter: Filter) -> None:
        self.compressor = compressor
        self.filter = filter
    

    def store(self):
        self.compressor.compress()
        self.filter.apply()

        print('Image stored!')



def main():

    storage = ImageStorage(compressor=JPGCompressor, filter=HighContrastFilter)
    storage.store()



if __name__ == '__main__':
    main()