from macpacking.algorithms.GreedyPartition import GreedyPartition
from macpacking.algorithms.baseline import ConstantBinNumber
from os.path import basename
from macpacking.reader import BinppReader


class FixedBin:
    def __init__(self):
        self.cases = [
            './_datasets/binpp/N1C1W1/N1C1W1_A.BPP.txt',
            './_datasets/binpp/N1C1W4/N1C1W4_B.BPP.txt',
            './_datasets/binpp/N1C2W2/N1C2W2_C.BPP.txt',
            './_datasets/binpp/N1C3W1/N1C3W1_D.BPP.txt',
            './_datasets/binpp/N1C3W4/N1C3W4_E.BPP.txt',
            './_datasets/binpp/N2C1W2/N2C1W2_F.BPP.txt',
            './_datasets/binpp/N2C2W1/N2C2W1_G.BPP.txt',
            './_datasets/binpp/N2C2W4/N2C2W4_H.BPP.txt',
            './_datasets/binpp/N2C3W2/N2C3W2_I.BPP.txt',
            './_datasets/binpp/N3C1W1/N3C1W1_J.BPP.txt',
            './_datasets/binpp/N3C1W4/N3C1W4_K.BPP.txt',
            './_datasets/binpp/N3C2W2/N3C2W2_L.BPP.txt',
            './_datasets/binpp/N3C3W1/N3C3W1_M.BPP.txt',
            './_datasets/binpp/N3C3W4/N3C3W4_N.BPP.txt']
        self.algos = [("GreedyPartition", GreedyPartition()),
                      ("Baseline", ConstantBinNumber())]

    def benchmark(self):
        returnArr = {}
        for i in self.algos:
            binpackerAlgo = i[1]
            result = {"MaxWeight": {}, "MinWeight": {}, "Difference": {}}

            for case in self.cases:
                name = basename(case)
                data = BinppReader(case).offline()
                sol = binpackerAlgo((10, data[1]))
                maxSum = max([sum(i) for i in sol])
                minSum = min([sum(i) for i in sol])
                diff = maxSum - minSum

                result["MaxWeight"][name] = maxSum
                result["MinWeight"][name] = minSum
                result["Difference"][name] = diff

                returnArr[i[0]] = {"MaxWeight": result["MaxWeight"],
                                   "MinWeight": result["MinWeight"],
                                   "Difference": result["Difference"],
                                   "runtime": {}}

        return returnArr
