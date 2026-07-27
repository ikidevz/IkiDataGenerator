import numpy as np
from ..base_provider import BaseProvider


class ExponentialDistributionProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, lam: float = 1.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)
        self.lam = lam
        try:
            seed = self._rng.randint(0, 2**32 - 1)
        except Exception:
            seed = None
        self._np_rng = np.random.default_rng(seed)

    def generate_non_blank(self, row_data=None):
        return self._np_rng.exponential(1.0 / self.lam)
