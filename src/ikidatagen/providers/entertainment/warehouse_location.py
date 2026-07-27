from ..base_provider import BaseProvider


class WarehouseLocationProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def _warehouse_code(self):
        prefix = self.get_random_data_by_list(
            ["WH", "WHS", "DC", "FUL", "LGC"])
        return f"{prefix}-{self.generate_integer(100, 9999)}"

    def _warehouse_city(self):
        return self.get_random_data_by_list([
            "Manila", "Cebu", "Davao", "Clark", "Iloilo",
            "Singapore", "Jakarta", "Bangkok", "Kuala Lumpur"
        ])

    def _zone(self):
        return f"Zone-{self.generate_integer(1, 20)}"

    def generate_non_blank(self, row_data=None):
        generators = [
            lambda: self._warehouse_code(),
            lambda: f"{self._warehouse_code()} | {self._warehouse_city()}",
            lambda: f"{self._warehouse_city()} - {self._zone()}",
            lambda: f"{self._warehouse_code()} / {self._zone()}",
        ]

        return self.get_random_data_by_list(generators)()
