from macpacking.reader import BinppReader

import macpacking.algorithms.online as online
import macpacking.algorithms.offline as offline
from macpacking.algorithms.baseline import BenMaier

from os.path import basename


class OptimalCompare:
    def __init__(self):

        self.CASES = './_datasets/binpp/N1C1W1'
        # the cases to be tested
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
        # the algorithms to be tested
        self.algos = [
            ("BenMaierOffline",
             BenMaier()),
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
             offline.WorstFitOffline())]
        # the data we will use to graph later
        self.compareData = {
            "Optimal": {},
            "BenMaierOffline": {},
            "NextFit": {},
            "FirstFit": {},
            "BestFit": {},
            "WorstFit": {},
            "TerribleFit": {},
            "NextFitOffline": {},
            "FirstFitOffline": {},
            "BestFitOffline": {},
            "WorstFitOffline": {}}

        # Initialise the data to be used
        for i in self.compareData:
            self.compareData[i]["Difference"] = {}
            self.compareData[i]["Bins"] = {}
            self.compareData[i]["Percent"] = {}

    def extract_optimal_Bins(self, file):
        # extract the optimal Bins from the csv file
        data = {}
        with open(file) as f:
            # read the csv file
            f.readline()
            # skip the first line
            for line in f:
                x = line.rstrip('\n').split(',')
                # assign the optimal Bins to the data dictionary
                data[x[0]] = int(x[1])
        return data

    def measure(self):
        # measure the difference between the optimal Bins
        # and the Bins of the algorithms
        # store the optimal Bins in a dictionary
        dict = self.extract_optimal_Bins('_datasets/binpp.csv')
        # for each algorithm
        for i in self.algos:
            binpackerAlgo = i[1]
            print(i[0])

            # running the algorithm on each case
            for case in self.cases:
                name = str(case[25:33])
                output = basename(case)
                if "Offline" in i[0]:
                    data = BinppReader(case).offline()
                else:
                    data = BinppReader(case).online()
                sol = binpackerAlgo(data)
                # print the comparison for each case
                print(
                    "For case: ",
                    name,
                    i[0],
                    "the Bins is: ",
                    len(sol),
                    " and the optimal Bins is: ",
                    dict[name])
                # store the difference between the optimal Bins and the Bins of
                # the algorithm
                self.compareData[i[0]]["Difference"][output] = len(
                    sol) - dict[name]
                # store the Bins of the algorithm
                self.compareData[i[0]]["Bins"][output] = len(sol)
                # store the percentage of the difference between the optimal
                # Bins and the Bins of the algorithm
                self.compareData[i[0]]["Percent"][output] = (
                    dict[name] / len(sol)) * 100

                # storing the optimal solutions for each characteristic
                self.compareData["Optimal"]["Difference"][output] = 0
                self.compareData["Optimal"]["Bins"][output] = dict[name]
                self.compareData["Optimal"]["Percent"][output] = 100
                # Check if solution is optimal
                if dict[name] == str(len(sol)):
                    print("The optimal Bins is found")
                else:
                    print("The optimal Bins is not found")
