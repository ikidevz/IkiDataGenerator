from ..base_provider import BaseProvider


class WeightProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None):
        unit = self.get_random_data_by_list(self.basic['weight_units'])

        if unit in ["g", "gram"]:
            value = round(self.generate_float(1, 5000), 1)
        elif unit in ["kg", "kilogram"]:
            value = round(self.generate_float(1, 200), 1)
        elif unit in ["oz"]:
            value = round(self.generate_float(1, 5000), 1)
        elif unit in ["lb", "lbs", "pound"]:
            value = round(self.generate_float(1, 440), 1)
        elif unit in ["st"]:
            value = round(self.generate_float(1, 30), 1)
        elif unit in ["ton", "tonne"]:
            value = round(self.generate_float(0.1, 100), 2)
        else:
            value = round(self.generate_float(1, 100), 1)
        return f"{value} {unit}"
