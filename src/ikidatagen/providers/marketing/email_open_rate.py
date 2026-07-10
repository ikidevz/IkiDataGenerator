from ..base_provider import BaseProvider


class EmailOpenRateProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None):
        return f"{round(self.generate_float(0, 100), 2)}%"
