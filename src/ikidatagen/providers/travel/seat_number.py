from ..base_provider import BaseProvider


class SeatNumberProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None):
        row = self.generate_integer(1, 60)
        seat_letter = self.get_random_data_by_list(["A", "B", "C", "D", "E", "F"])
        return f"{row}{seat_letter}"
