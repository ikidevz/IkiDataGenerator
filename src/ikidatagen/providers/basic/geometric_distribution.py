import numpy as np
from ..base_provider import BaseProvider


class GeometricDistributionProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, probability: float = 0.5, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)
        self.p = probability
        try:
            seed = self._rng.randint(0, 2**32 - 1)
        except Exception:
            seed = None
        self._np_rng = np.random.default_rng(seed)

    def generate_non_blank(self, row_data=None):
        return int(self._np_rng.geometric(self.p))
