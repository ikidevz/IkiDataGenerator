from ..base_provider import BaseProvider


class MemoryFootprintProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None):
        unit = self.get_random_data_by_list(["MB", "GB"])

        if unit == "MB":
            value = self.generate_integer(50, 3000)
            return f"{value}MB"

        else:
            value = self.generate_float(0.5, 32.0)
            formatted = f"{value:.1f}".rstrip("0").rstrip(".")
            return f"{formatted}GB"
