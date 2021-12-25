import numpy as np
import pandas as pd


class KMeans():
    """
    Classifies datapoints into `k` centroids.

    Attributes:
        x: The input data, should be of size (batch_size, dims...)
        k: The total number of distinct clusters in which to group the
           datapoints, fixed in this case
    """
    def __init__(self, x, k):
        self._x = x
        self._k = k

        # Randomly choose initial centroids
        self._centroids = self._x[np.random.choice(len(self._x),
                                                   k,
                                                   replace=False)]

    def fit(self):
        """
        Fit the optimal configuration given starting centroids.  Follows the
        classic variant where adjustments stop once the cluster ids stop
        changing (could also be given some epsilon (error bound) as well).
        """

        prev_clusters = self.predict(self._x)
        while True:
            self.step()
            new_clusters = self.predict(self._x)

            if (prev_clusters - new_clusters).sum() == 0:
                break
            prev_clusters = new_clusters

    def step(self):
        """
        Steps through one iteration of the classic optimization algorithm.
        """

        # Classification in K-Means is choosing the closest centroid to the
        #   datapoint by some metric, in this case Euclidean Distance.
        y = self.predict(self._x)
        y = np.expand_dims(y, axis=1)  # (batch_size, 1)

        # Optimize centroid locations using some metric, in this case the mean
        #   of all points currently being classified into that centroids will
        #   be used.
        df = pd.DataFrame(np.concatenate([y, self._x], axis=-1))
        centroids = df.groupby([0]).mean()
        self._centroids = np.asarray(centroids)

    def predict(self, x):
        """
        Given the stored centroids, predicts the cluster in which `x` belongs
        to.

        Attributes:
            x: The input data, of size (batch_size, dims...)
        """

        batch_size = x.shape[0]

        # The most straightforward to vectorize is to calculate the metric to
        #   every possible cluster, so the aim is to resize to
        #   (batch_size, k, dims...) for the input and the clusters and then
        #   just the metric starting at dimension 2.
        x = np.expand_dims(x, axis=1)  # (batch_size, 1, dims...)
        x = np.repeat(x, self._k, axis=1)  # (batch_size, k, dims...)

        y = np.expand_dims(self._centroids, axis=0)  # (1, k, dims...)
        y = np.repeat(y, batch_size, axis=0)  # (batch_size, k, dims...)

        # Numpy uses the Frobernius norm, which ends up calculating to be the
        #   equivalent of the Eucliean distance in this case
        distance = np.linalg.norm(x - y, axis=2)

        # Assign cluster as the minimum centroid (k clusters, so dimension 1)
        assignments = np.argmin(distance, axis=1)

        # Output should be of size (batch_size) for simplicity
        return assignments.reshape(batch_size)
