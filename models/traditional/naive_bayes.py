import numpy as np
import pandas as pd


class GaussianNaiveBayes():
    """
    Calculates P(y|X) using Bayes Theorem.
        P(y|X) = P(X|y)P(y) * (1 / P(X))
    Given the prior distribution, represented by the dataset for
      training, X, which is also called the evidence in other texts,
      predict the posteriori probability of the label, y, using the
      prior probabilities of y and X.
    1 / P(X) can be omitted, as it normalizes the posterior distribution
      to integrate to 1.

    Attributes:
        x: The input data, of size (batch_size, dims...)
        y: The ground truth labels, of size (batch_size, 1)
    """
    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y
        self._n = self._y.shape[0]

    def fit(self):
        """
        A dummy method, not needed in this implementation.  At most,
        this will be used to provide amortized speedups by precomputing
        probabilities.
        """
        pass

    def predict(self, x):
        """
        Predicts the label for the given `x`.

        Attributes:
            x: The input data, of size (batch_size, dims...)
        """

        # Number of samples in the batch
        batch_size = x.shape[0]

        # Calculate the priori probabilities of each class
        df = pd.DataFrame(np.concatenate([self._y, self._x], axis=-1))
        priori = df.groupby([0]).size() / self._n  # relative to dataset
        priori = np.asarray(priori)  # (classes)

        # Calculate the probability of the input data, `x`, given a
        #   target label.  For generality, a normal distribution is
        #   used, for discrete is a subset of continuous, number-wise
        #   at least, categorical variables are not supported.

        # Calculate mean and variance of every feature separated from class
        mean = np.asarray(df.groupby([0]).mean())  # (classes, dims...)
        std = np.asarray(df.groupby([0]).std())  # (classes, dims...)

        # Standardize input data to N(0, 1)
        classes = len(df.groupby([0]))
        x = np.expand_dims(x, axis=1)  # (batch_size, 1, dims...)
        x = np.repeat(x, classes, axis=1)  # (batch_size, classes, dims...)
        x = (x - mean) / std  # (batch_size, classes, dims...)

        # Calculate P(X|y) for every feature
        #   The probability mass function (PMF) of a Guassian (normal)
        #   distribution is:
        #     (1 / (std * sqrt(2 * PI))) *
        #     exp(-1 * (1 / 2) * ((x - mu)^2 / std^2))
        #   Given standardized datapoints and a normal distribution, N(0, 1):
        #     (1 / sqrt(2 * PI)) * exp(-1 * (1 / 2) * x^2)
        x = np.exp(-0.5 * np.power(x, 2)) / np.sqrt(2 * np.pi)

        # P(X1, X2, X3, ..., XN|y) = P(X1|y)P(X2|y)P(X3|y) ... P(XN|y)
        x = np.prod(x, axis=2)  # (batch_size, classes)

        # P(X|y)P(y)
        priori = np.expand_dims(priori, axis=0)  # (1, classes)
        priori = np.repeat(priori, batch_size, axis=0)  # (batch_size, classes)
        x = x * priori  # (batch_size, classes)

        # If probabilities need to be normalized, then it can be done through
        # softmax, although it isn't available with numpy as of this
        # implementation.
        # x = np.softmax(x, axis=1)  # (batch_size, classes)

        # Determine the label by choosing the maximum probability
        return np.argmax(x, axis=1)  # class, which is the 1st dimension
