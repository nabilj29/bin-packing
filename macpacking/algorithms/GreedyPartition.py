# Multi-Way Greedy Algorithm for Bin Packing Problem
# input: a list of items
class GreedyPartition:

    def __init__(self):
        # store the bins
        self.bins = []
        self.counter = []

    # call the process function
    def __call__(self, ws):
        k, item = ws
        return self._process(k, item)

    # filling the bins evenly
    def fillBins(self, k, items):
        # k is the number of bins
        # items is the list of items
        # sort the items in descending order
        items.sort(reverse=True)
        for i in range(k):
            # create k empty bins
            self.bins.append([])
            # create k counters
            self.counter.append(0)
        for i in range(len(items)):
            # find the bin with the least sum and add the item to it
            self.bins[self.counter.index(min(self.counter))].append(items[i])
            # update the counter
            # the counter is the sum of the items in the bin
            self.counter[self.counter.index(min(self.counter))] += items[i]
        return self.bins

    # print the bins
    def printBins(self):
        for i in range(len(self.bins)):
            print("Bin", i, self.bins[i], "sum:", sum(self.bins[i]))
    # calls the fill bins function

    def _process(self, item, k):
        result = self.fillBins(item, k)
        return result
