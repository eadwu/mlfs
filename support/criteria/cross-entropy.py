import numpy as np
from .criteria import Criteria


class CrossEntropyLoss(Criteria):
    def __init__(self):
        super().__init__()

    # Forward calculates the Cross Entropy Loss given the prediction and
    # the reference solution.  `ref` should only contain the class labels.
    def forward(self, ref, hyp):
        super().forward(ref, hyp)

    def backward(self):
        super().backward()
        return 0.
