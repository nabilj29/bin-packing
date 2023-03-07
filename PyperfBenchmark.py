
import pyperf
from os import listdir
from os.path import isfile, join, basename
from macpacking.reader import BinppReader
import macpacking.algorithms.online as online
import macpacking.algorithms.offline as offline


class Benchmark2:
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

        runner = pyperf.Runner(processes=1)

        for case in self.cases:
            name = basename(case)
            data = BinppReader(case).online()

            runner.bench_func(name + "_NF", self.algos[0][1], data)
            runner.bench_func(name + "_FF", self.algos[1][1], data)
            runner.bench_func(name + "_BF", self.algos[2][1], data)
            runner.bench_func(name + "_WF", self.algos[3][1], data)
            runner.bench_func(name + "_TF", self.algos[4][1], data)
            runner.bench_func(name + "_NFO", self.algos[5][1], data)
            runner.bench_func(name + "_FFO", self.algos[6][1], data)
            runner.bench_func(name + "_BFO", self.algos[7][1], data)
            runner.bench_func(name + "_WFO", self.algos[8][1], data)
            runner.bench_func(name + "_RFF", self.algos[9][1], data)
        for i in self.algos:
            i[1].resetKPI()


if __name__ == "__main__":
    bench = Benchmark2()
    bench.benchmark()
