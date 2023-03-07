from .. import Solution, WeightStream
from ..model import Online

# NextFit online algorithm


class NextFit(Online):
    def __init__(self) -> None:
        # KPIs for the algorithm
        self.iterations = 0
        self.comparisons = 0
        self.dataAccess = 0

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        # initialize bin index
        bin_index = 0
        # initalize solution
        solution = [[]]
        # the number remaining
        remaining = capacity
        # iterate through the stream
        for w in stream:
            # keep track of the number of KPIs
            self.iterations += 1
            self.comparisons += 1
            # if the remaining capacity is greater than the weight
            if remaining >= w:
                # keep track of the number of KPIs
                self.dataAccess += 1
                # add the weight to the current bin
                solution[bin_index].append(w)
                # update the remaining capacity
                remaining = remaining - w
            else:
                # keep track of the number of KPIs
                bin_index += 1
                # add a new bin
                solution.append([w])
                # update the remaining capacity
                remaining = capacity - w
        return solution

    def resetKPI(self):
        # reset the KPIs after each run
        self.iterations = 0
        self.comparisons = 0
        self.dataAccess = 0

# FirstFit online algorithm


class FirstFit(Online):

    def __init__(self) -> None:
        # KPIs for the algorithm
        self.iterations = 0
        self.comparisons = 0
        self.dataAccess = 0

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        # initialize bin index
        bin_index = 0
        # initalize solution
        solution = [[]]
        # iterate through the stream
        for w in stream:
            # keep track of the number of KPIs
            self.iterations += 1
            bin_index = 0
            self.comparisons += 1
            # while the bin index is less than the length of the solution
            while bin_index < len(solution):
                # keep track of the number of KPIs
                self.iterations += 1
                self.comparisons += 2
                self.dataAccess += 1
                # if the remaining capacity is greater than the weight
                if sum(solution[bin_index]) + w <= capacity:
                    # keep track of the number of KPIs
                    self.dataAccess += 1
                    # add the weight to the current bin
                    solution[bin_index].append(w)
                    break
                # add one to the bin index
                bin_index += 1
            # keep track of the number of KPIs
            self.comparisons += 1
            # if the bin index is equal to the length of the solution
            if bin_index == len(solution):
                solution.append([w])
        return solution

    def resetKPI(self):
        # reset the KPIs after each run
        self.iterations = 0
        self.comparisons = 0
        self.dataAccess = 0

# BestFit online algorithm


class BestFit(Online):

    def __init__(self) -> None:
        # KPIs for the algorithm
        self.iterations = 0
        self.comparisons = 0
        self.dataAccess = 0

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        # initialize bin index
        bin_index = 0
        # initalize solution
        solution = [[]]
        # iterate through the stream
        for w in stream:
            # keep track of the number of KPIs
            self.iterations += 1
            bin_index = 0
            best_fit = 0
            best_fit_index = 0
            self.comparisons += 1
            # while the bin index is less than the length of the solution
            while bin_index < len(solution):
                # keep track of the number of KPIs
                self.iterations += 1
                self.comparisons += 2
                self.dataAccess += 1
                # if the remaining capacity is greater than the weight
                if sum(solution[bin_index]) + w <= capacity:
                    # keep track of the number of KPIs
                    self.comparisons += 1
                    self.dataAccess += 1
                    # if the remaining capacity is greater than the best fit
                    if sum(solution[bin_index]) + w > best_fit:
                        # keep track of the number of KPIs
                        self.dataAccess += 1
                        # update the best fit
                        best_fit = sum(solution[bin_index]) + w
                        best_fit_index = bin_index
                bin_index += 1
            self.comparisons += 1
            # if the best_fit is greater than 0
            if best_fit != 0:
                # keep track of the number of KPIs
                self.dataAccess += 1
                # add the weight to the best fit bin
                solution[best_fit_index].append(w)
            else:
                # add to solution
                solution.append([w])
        return solution

    def resetKPI(self):
        # reset the KPIs after each run
        self.iterations = 0
        self.comparisons = 0
        self.dataAccess = 0

# worst fit online algorithm


class WorstFit(Online):
    def __init__(self) -> None:
        # KPIs for the algorithm
        self.iterations = 0
        self.comparisons = 0
        self.dataAccess = 0

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        # initialize bin index
        bin_index = 0
        # initalize solution
        solution = [[]]
        # iterate through the stream
        for w in stream:
            # keep track of the number of KPIs
            self.iterations += 1
            bin_index = 0
            worst_fit = 0
            worst_fit_index = 0
            self.comparisons += 1
            # while the bin index is less than the length of the solution
            while bin_index < len(solution):
                # keep track of the number of KPIs
                self.iterations += 1
                self.comparisons += 2
                self.dataAccess += 1
                # if the remaining capacity is greater than the weight
                if sum(solution[bin_index]) + w <= capacity:
                    self.comparisons += 1
                    # if the sum of the bin is greater than the worst fit
                    if sum(solution[bin_index]) + w > worst_fit:
                        # keep track of the number of KPIs
                        self.dataAccess += 1
                        # update the worst fit
                        worst_fit = sum(solution[bin_index]) + w
                        worst_fit_index = bin_index
                # keep track of the number of KPIs
                bin_index += 1
            self.comparisons += 1
            # if the worst fit is greater than 0
            if worst_fit != 0:
                # keep track of the number of KPIs
                self.dataAccess += 1
                # add the weight to the worst fit bin
                solution[worst_fit_index].append(w)
            else:
                # add to solution
                solution.append([w])
        return solution

    def resetKPI(self):
        # reset the KPIs after each run
        self.iterations = 0
        self.comparisons = 0
        self.dataAccess = 0

# terribe fit online algorithm


class TerribleFit(Online):
    def __init__(self) -> None:
        # KPIs for the algorithm
        self.iterations = 0
        self.comparisons = 0
        self.dataAccess = 0

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        solution = []
        # iterate through the stream
        for w in stream:
            # keep track of the number of KPIs
            self.iterations += 1
            # add each weight to a bin
            solution.append([w])
        return solution

    def resetKPI(self):
        # reset the KPIs after each run
        self.iterations = 0
        self.comparisons = 0
        self.dataAccess = 0

# refined first fit online algorithm


class RFF(Online):
    def __init__(self) -> None:
        # KPIs for the algorithm
        self.iterations = 0
        self.comparisons = 0
        self.dataAccess = 0

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        # initialize solution
        solution = []
        # initialize bin index for different classes
        classAarr = []
        classA = []
        classB = []
        classC = []
        classD = []

        # modulus we will use to determine the class
        mods = [6, 7, 8, 9]
        # class counter to determine if we need to add a different class
        classC_Count = 0

        # iterate through the stream
        for w in stream:
            # keep track of the number of KPIs
            self.iterations += 1
            # compare the weight divided by capapcity
            compare = w / capacity
            # keep track of the number of KPIs
            self.comparisons += 2
            # if compare is greater than 0.5 and less than 1
            if compare > 1 / 2 and compare <= 1:
                # keep track of the number of KPIs
                self.comparisons += 1
                # if sum of class A is less than capacity
                if sum(classA) + w <= capacity:
                    # add to class A
                    classA.append(w)
                else:
                    # add to solution
                    classAarr.append(classA)
                    classA = [w]

            #if compare is greater than 0.25 and less than 0.5
            elif compare > 2 / 5 and compare <= 1 / 2:
                self.comparisons += 3
                self.dataAccess += 1
                if sum(classB) + w <= capacity:
                    classB.append(w)
                else:
                    solution.append(classB)
                    classB = [w]
            #if compare is greater than 0.125 and less than 0.25
            elif compare > 1 / 3 and compare <= 2 / 5:
                classC_Count += 1
                self.comparisons += 2
                self.dataAccess += 1
                for i in mods:
                    self.iterations += 1
                    self.comparisons += 1
                    if classC_Count % i == 0:
                        bin_index = 0
                        self.comparisons += 1
                        while bin_index < len(classAarr):
                            self.iterations += 1
                            self.comparisons += 2
                            self.dataAccess += 1
                            if sum(classAarr[bin_index]) + w <= capacity:
                                self.dataAccess += 1
                                classAarr[bin_index].append(w)
                                break
                            bin_index += 1
                self.comparisons += 1
                if sum(classC) + w <= capacity:
                    classC.append(w)
                else:
                    solution.append(classC)
                    classC = [w]
            #if compare is greater than 0 and less than 0.125
            elif compare > 0 and compare <= 1 / 3:
                self.comparisons += 3
                self.dataAccess += 1
                if sum(classD) + w <= capacity:
                    classD.append(w)
                else:
                    solution.append(classD)
                    classD = [w]
        solution += classAarr
        solution.append(classA)
        solution.append(classB)
        solution.append(classC)
        solution.append(classD)
        return solution

    def resetKPI(self):
        self.iterations = 0
        self.comparisons = 0
        self.dataAccess = 0
