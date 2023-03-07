from abc import ABC, abstractmethod
from os import path
from random import shuffle, seed
from . import WeightSet, WeightStream


class DatasetReader(ABC):

    def offline(self) -> WeightSet:
        '''Return a WeightSet to support an offline algorithm'''
        (capacity, weights) = self._load_data_from_disk()
        seed(42)          # always produce the same shuffled result
        shuffle(weights)  # side effect shuffling
        return (capacity, weights)

    def online(self) -> WeightStream:
        '''Return a WeighStream, to support an online algorithm'''
        (capacity, weights) = self.offline()

        def iterator():  # Wrapping the contents into an iterator
            for w in weights:
                yield w  # yields the current value and moves to the next one

        return (capacity, iterator())

    @abstractmethod
    def _load_data_from_disk(self) -> WeightSet:
        '''Method that read the data from disk, depending on the file format'''
        pass


class BinppReader(DatasetReader):
    '''Read problem description according to the BinPP format'''

    def __init__(self, filename: str) -> None:
        if not path.exists(filename):
            raise ValueError(f'Unkown file [{filename}]')
        self.__filename = filename

    def _load_data_from_disk(self) -> WeightSet:
        with open(self.__filename, 'r') as reader:
            nb_objects: int = int(reader.readline())
            capacity: int = int(reader.readline())
            weights = []
            for _ in range(nb_objects):
                weights.append(int(reader.readline()))
            return (capacity, weights)


class JburReader(DatasetReader):
    #formating the JBUR dataset

    def __init__(self, filename: str) -> None:
        if not path.exists(filename):
            raise ValueError(f'Unkown file [{filename}]')
        result = filename.index('p0')
        substring = filename[result:result + 3]
        print(substring)
        self.__filecapacity = '_datasets/jburkardt/' + substring + '_c.txt'
        self.__fileweights = '_datasets/jburkardt/' + substring + '_w.txt'
        self.__optimal_weight = '_datasets/jburkardt/' + substring + '_s.txt'

    def _load_data_from_disk(self) -> WeightSet:
        with open(self.__filecapacity, 'r') as reader:
            capacity: int = int(reader.readline())

        with open(self.__optimal_weight, 'r') as reader:
            optimal_weight = []
            for line in reader:
                optimal_weight.append(int(line))

        with open(self.__fileweights, 'r') as reader:
            weights = []
            for _ in range(len(optimal_weight)):
                weight = int(reader.readline().strip())
                weights.append(weight)
            return (capacity, weights)
