from ..base_provider import BaseProvider


class BoardingGateProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None):
        if self.get_random_data_by_list([True, False]):
            gate_number = self.generate_integer(1, 60)
            return f"Gate {gate_number}"
        else:
            letter = self.get_random_data_by_list(["A", "B", "C", "D", "E"])
            number = self.generate_integer(1, 50)
            return f"{letter}{number}"
