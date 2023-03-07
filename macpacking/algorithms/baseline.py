from .. import Solution
from ..model import Offline
import binpacking as bp


class BenMaier(Offline):

    def _process(self, capacity: int, weights: list[int]) -> Solution:
        return bp.to_constant_volume(weights, capacity)


# adding the constant bin size algorithm
class ConstantBinNumber():
    def __call__(self, ws):
        capacity, stream = ws
        return self._process(capacity, stream)

    def _process(self, numBins, list) -> Solution:
        return bp.to_constant_bin_number(list, numBins)
