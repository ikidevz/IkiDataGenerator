from ..base_provider import BaseProvider


class ServingSizeProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None):
        quantity = self.generate_integer(1, 3)
        units = [
            "cup", "cups", "tbsp", "tsp", "g", "mg", "slice", "plate", "bowl"
        ]

        unit = self.get_random_data_by_list(units)
        if unit in ["g", "mg"]:
            return f"{self.generate_integer(50, 500)}{unit}"

        return f"{quantity} {unit}"
