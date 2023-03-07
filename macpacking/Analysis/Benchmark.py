
from os import listdir
from os.path import isfile, join, basename
import macpacking.algorithms.online as online
import macpacking.algorithms.offline as offline
from macpacking.reader import BinppReader


class Benchmark:
    def __init__(self):
        self.CASES = './_datasets/binpp/N1C1W1'
        self.cases = self.list_case_files(self.CASES)
        self.algos = [
            ("NextFit",
             online.NextFit()),
            ("FirstFit",
             online.FirstFit()),
            ("BestFit",
             online.BestFit()),
            ("WorstFit",
             online.WorstFit()),
            ("TerribleFit",
             online.TerribleFit()),
            ("NextFitOffline",
             offline.NextFitOffline()),
            ("FirstFitOffline",
             offline.FirstFitOffline()),
            ("BestFitOffline",
             offline.BestFitOffline()),
            ("WorstFitOffline",
             offline.WorstFitOffline()),
            ("RefinedFirstFit",
             online.RFF())]

    def list_case_files(self, dir: str) -> list[str]:
        return sorted([f'{dir}/{f}' for f in listdir(dir)
                      if isfile(join(dir, f))])

    def benchmark(self):
        returnArr = {}
        for i in self.algos:
            binpackerAlgo = i[1]
            resultIteration = {}
            resultDataAccess = {}
            resultComparison = {}
            totalOperations = {}

            for case in self.cases:
                name = basename(case)
                data = BinppReader(case).online()
                binpackerAlgo(data)

                totalOperations[name] = binpackerAlgo.iterations + \
                    binpackerAlgo.dataAccess + \
                    binpackerAlgo.comparisons
                resultIteration[name] = binpackerAlgo.iterations
                resultDataAccess[name] = binpackerAlgo.dataAccess
                resultComparison[name] = binpackerAlgo.comparisons

                binpackerAlgo.resetKPI()

                returnArr[i[0]] = {"Operations": totalOperations,
                                   "Iterations": resultIteration,
                                   "Access": resultDataAccess,
                                   "Comparison": resultComparison,
                                   "runtime": {}}

        return returnArr
