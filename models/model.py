from generic import NotImplementedError


class Model():
    def __init__(self):
        self._x = None
        self._y = None

    def __call__(self, x):
        return self.forward(x)

    def forward(self, x):
        return NotImplementedError("forward is not implemented")

    def backward(self):
        return NotImplementedError("backward is not implemented")

    def zero_grad(self):
        return NotImplementedError("zero_grad is not implemented")
