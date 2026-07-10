import json

from ..base_provider import BaseProvider


class JsonArrayProvider(BaseProvider):
    def __init__(self, *, blank_percentage: float = 0.0, min_elements: int = 1, max_elements: int = 3, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)
        self.min_elements = min_elements
        self.max_elements = max_elements

    def _random_value(self):
        return self.get_random_data_by_list([
            None,
            True,
            False,
            self.generate_integer(0, 1000),
            round(self.generate_float(0.0, 1000.0), 2),
            self.get_random_data_by_list(["alpha", "beta", "gamma", "delta"]),
        ])

    def generate_non_blank(self, row_data=None):
        num_elements = self.generate_integer(
            self.min_elements, self.max_elements)
        values = [self._random_value() for _ in range(num_elements)]
        return json.dumps(values)
