import numpy as np
from ..base_provider import BaseProvider


class NormalDistributionProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0,  mean: float = 0.0, std_dev: float = 1.0, decimals: int = 2, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)
        self.mean = mean
        self.std_dev = std_dev
        self.decimals = decimals
        try:
            seed = self._rng.randint(0, 2**32 - 1)
        except Exception:
            seed = None
        self._np_rng = np.random.default_rng(seed)

    def generate_non_blank(self, row_data=None):
        return round(self._np_rng.normal(self.mean, self.std_dev), self.decimals)
