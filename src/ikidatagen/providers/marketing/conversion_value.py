from ..base_provider import BaseProvider


class ConversionValueProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None):
        style = self.get_random_data_by_list(["currency", "credits"])

        if style == "currency":
            r = self.get_random_object()
            if r < 0.85:
                amount = round(self.generate_float(1, 500), 2)
            else:
                amount = round(self.generate_float(100, 100000), 2)

            return f"${amount:,.2f}"

        else:
            credits = self.generate_integer(1, 500)
            return f"{credits} credits"
