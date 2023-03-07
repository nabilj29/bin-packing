from os.path import isfile, join
from os import listdir
from macpacking.reader import BinppReader
import macpacking.algorithms.offline as offline

offline_algorithms = [
    offline.NextFitOffline(),
    offline.FirstFitOffline(),
    offline.BestFitOffline(),
    offline.WorstFitOffline(),

]


def list_case_files(dir: str) -> list[str]:
    return sorted([f'{dir}/{f}' for f in listdir(dir) if isfile(join(dir, f))])


CASES = './_datasets/binpp/N1C1W1'
cases = list_case_files(CASES)


def test_offline():
    for case in cases:
        data = BinppReader(case).offline()
        capacity = data[0]
        for algo in offline_algorithms:
            ans = algo(data)
            for algoBin in ans:
                assert sum(algoBin) <= capacity
