import numpy as np


class LinearRegression():
    """
    Performs general linear regression fitting on the provided data.
    Categorical data is not supported here, even though it is
      supported through indicator variables in the generic version.
    Keeping it simple, no interaction terms are provided as well.
    The general linear regression formula can be expressed as:
      Y = B0 + B1X1 + B2X2 + ... + BNXN
      given predictors { B0, B1, ... BN }. A simple transformation
      yields: Y = sum BiXi where X0 = 1.

    Attributes:
        x: The input data, of size (batch_size, dims...)
        y: The ground truth labels, of size (batch_size, 1)
    """
    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y

        self._coefficients = None

    def fit(self):
        """
        Solves for each of the predictor variables.  For a fixed `p`
        predictors, solving the derivatives individually is possible,
        but since this is basically a collection of vectorized
        algorithms, this is equivalent to b + xA = y.

        This can be simplified to x'A' = y, where x is prepended with
        an input of all 1s and A' is prepended with a dimension of
        `b`s.
        """

        # Polyfill matrix for B0X0 = B0 when X0 = 1
        x = np.insert(self._x, 0, 1, axis=1)

        # Calculate Monroe-Penrose pseudoinverse to ensure calculation
        # succeeds.
        pseudoinverse = np.linalg.inv(np.transpose(x) @ x)
        pseudoinverse = pseudoinverse @ np.transpose(x)

        # Calculate coefficients
        self._coefficients = pseudoinverse @ self._y

    def predict(self, x):
        """
        Predicts the expected value for a given `x`.

        Attributes:
            x: The input data, of size (batch_size, dims...)
        """

        # Ensure coefficients were calculated
        if self._coefficients is None:
            self.fit()

        # Polyfill for B0 before calculating Y = Ax
        x = np.insert(x, 0, 1, axis=1)
        return x @ self._coefficients
