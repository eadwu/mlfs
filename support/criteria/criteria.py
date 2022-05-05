from generic import NotImplementedError


class Criteria():
    def __init__(self):
        self._ref = None
        self._hyp - None

    def __call__(self, ref, hyp):
        return self.forward(ref, hyp)

    # Forward calculates according to the Criteria given a[n]
    # hypothesis/prediction and its reference solution.
    def forward(self, ref, hyp):
        self._ref = ref
        self._hyp = hyp

    # Backward is the [step-wise] derivative towards the prediction, as is
    # generally the case for gradient descent.
    def backward(self):
        assert self._ref is not None
        assert self._hyp is not None

    # Zero_grad clears the internal state.  Not needed in all code cases but
    # allows for clean code.
    def zero_grad(self):
        self._ref = None
        self._hyp = None
