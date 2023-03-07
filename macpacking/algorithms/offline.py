from .. import Solution, WeightSet
from ..model import Offline
from .online import NextFit as Nf_online
from .online import FirstFit as Ff_online
from .online import BestFit as Bf_online
from .online import WorstFit as Wf_online


class NextFitOffline(Offline):

    def __init__(self) -> None:
        # KPIs for the algorithm
        self.iterations = 0
        self.comparisons = 0
        self.dataAccess = 0

    def _process(self, capacity: int, weights: WeightSet) -> Solution:
        '''An offline version of NextFit, ordering the weigh stream and
        delegating to the online version (avoiding code duplication)'''
        # sort the weights in descending order
        weights = sorted(weights, reverse=True)
        # keep track of the number of KPIs
        self.iterations += len(weights)
        self.comparisons += len(weights)
        self.dataAccess += len(weights)
        # delegating to the online version
        delegation = Nf_online()
        sol = delegation((capacity, weights))
        # keep track of the number of KPIs
        self.iterations += delegation.iterations
        self.comparisons += delegation.comparisons
        self.dataAccess += delegation.dataAccess
        return sol

    def resetKPI(self):
        # reset the KPIs after each run
        self.iterations = 0
        self.comparisons = 0
        self.dataAccess = 0


class FirstFitOffline(Offline):

    def __init__(self) -> None:
        # KPIs for the algorithm
        self.iterations = 0
        self.comparisons = 0
        self.dataAccess = 0

    def _process(self, capacity: int, weights: WeightSet) -> Solution:
        '''An offline version of FirstFit, ordering the weigh stream and
        delegating to the online version (avoiding code duplication)'''
        # sorting the weights in descending order
        weights = sorted(weights, reverse=True)
        # delegating to the online version
        delegation = Ff_online()
        # keep track of the number of KPIs
        self.iterations += len(weights)
        self.comparisons += len(weights)
        self.dataAccess += len(weights)
        # solution with the delegation
        sol = delegation((capacity, weights))
        # keep track of the number of KPIs
        self.iterations += delegation.iterations
        self.comparisons += delegation.comparisons
        self.dataAccess += delegation.dataAccess
        return sol

    def resetKPI(self):
        # reset the KPIs after each run
        self.iterations = 0
        self.comparisons = 0
        self.dataAccess = 0


class BestFitOffline(Offline):

    def __init__(self) -> None:
        # KPIs for the algorithm
        self.iterations = 0
        self.comparisons = 0
        self.dataAccess = 0

    def _process(self, capacity: int, weights: WeightSet) -> Solution:
        '''An offline version of BestFit, ordering the weigh stream and
        delegating to the online version (avoiding code duplication)'''
        # sorting the weights in descending order
        weights = sorted(weights, reverse=True)
        # delegating to the online version
        delegation = Bf_online()
        # keep track of the number of KPIs
        self.iterations += len(weights)
        self.comparisons += len(weights)
        self.dataAccess += len(weights)
        # solution with the delegation
        sol = delegation((capacity, weights))
        # keep track of the number of KPIs
        self.iterations += delegation.iterations
        self.comparisons += delegation.comparisons
        self.dataAccess += delegation.dataAccess
        return sol

    def resetKPI(self):
        # reset the KPIs after each run
        self.iterations = 0
        self.comparisons = 0
        self.dataAccess = 0


class WorstFitOffline(Offline):

    def __init__(self) -> None:
        # KPIs for the algorithm
        self.iterations = 0
        self.comparisons = 0
        self.dataAccess = 0

    def _process(self, capacity: int, weights: WeightSet) -> Solution:
        '''An offline version of WorstFit, ordering the weigh stream and
        delegating to the online version (avoiding code duplication)'''
        # sorting the weights in descending order
        weights = sorted(weights, reverse=True)
        # keep track of the number of KPIs
        self.iterations += len(weights)
        self.comparisons += len(weights)
        self.dataAccess += len(weights)
        # delegating to the online version
        delegation = Wf_online()
        # solution with the delegation
        sol = delegation((capacity, weights))
        # keep track of the number of KPIs
        self.iterations += delegation.iterations
        self.comparisons += delegation.comparisons
        self.dataAccess += delegation.dataAccess
        # return the solution
        return sol

    def resetKPI(self):
        # reset the KPIs after each run
        self.iterations = 0
        self.comparisons = 0
        self.dataAccess = 0
