from ..base_provider import BaseProvider


class DimensionProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, type: str = "2D", **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)
        self.type = type

    def generate_non_blank(self, row_data=None):
        if self.type == "2D":
            width = round(self.generate_float(1, 5000), 1)
            height = round(self.generate_float(1, 5000), 1)
            return f"{width}x{height}"
        else:
            width = round(self.generate_float(1, 500), 1)
            height = round(self.generate_float(1, 500), 1)
            depth = round(self.generate_float(1, 500), 1)
            return f"{width}x{height}x{depth}"
