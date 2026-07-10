from ..base_provider import BaseProvider


class ClickDepthProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None):
        r = self.get_random_object()
        if r < 0.70:
            return self.generate_integer(1, 4)
        elif r < 0.95:
            return self.generate_integer(5, 8)
        else:
            return self.generate_integer(9, 12)
