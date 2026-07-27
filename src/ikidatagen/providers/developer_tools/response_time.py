from ..base_provider import BaseProvider


class ResponseTimeProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None):
        if self.get_random_object() < 0.7:
            ms = self.generate_integer(10, 1000)
            return f"{ms}ms"
        else:
            s = round(self.generate_float(0.5, 5), 2)
            return f"{s}s"
