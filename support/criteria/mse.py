import numpy as np
from .criteria import Criteria


class MeanSquaredError(Criteria):
    def __init__(self):
        super().__init__()

    # Forward calculates the Mean Squared Error given the prediction and the
    # reference solution.  `ref` and `hyp` should have the same shape.
    def forward(self, ref, hyp):
        super().forward(ref, hyp)
        return np.mean(np.power(ref - hyp, 2))

    def backward(self):
        super().backward()
        return -np.mean(2 * (self._ref - self._hyp))
