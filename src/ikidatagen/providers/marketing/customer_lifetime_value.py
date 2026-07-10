from ..base_provider import BaseProvider


class CustomerLifetimeValueProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, min: int = 1000, max: int = 1_000_000, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)
        self.min = min
        self.max = max

    def generate_non_blank(self, row_data=None):
        value = self.generate_integer(self.min, self.max)
        return f"${value:,}"
