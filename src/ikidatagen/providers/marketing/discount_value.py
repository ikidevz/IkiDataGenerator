from ..base_provider import BaseProvider


class DiscountValueProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, currency: str = '$', **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)
        self.currency = currency

    def generate_non_blank(self, row_data=None):
        style = self.get_random_data_by_list(["percentage", "flat"])

        if style == "percentage":
            value = self.get_random_data_by_list([5, 10, 15, 20, 25, 30, 40, 50, 60, 75, 80])
            return f"{value}%"

        value = self.generate_integer(1, 500)
        return f"${value} off"
