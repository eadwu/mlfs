import numpy as np
from .criteria import Criteria


class BinaryCrossEntropyLoss(Criteria):
    def __init__(self):
        super().__init__()

    # Forward calculates the Binary Cross Entropy Loss given the
    # prediction and reference probabilities.  As in PyTorch, log
    # outputs are clamped to be greater than or equal to -100.
    def forward(self, ref, hyp):
        super().forward(ref, hyp)

    def backward(self):
        super().backward()
        return 0.
