from ..base_provider import BaseProvider


class AirportTerminalProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None):
        prefix = self.get_random_data_by_list(["Terminal", 'T'])
        number = int(self.generate_integer(1, 5))

        return f"{prefix} {number}" if prefix == "Terminal" else f"{prefix}{number}"
