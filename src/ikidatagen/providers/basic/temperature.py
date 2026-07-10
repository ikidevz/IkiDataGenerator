from ..base_provider import BaseProvider
import random


class TemperatureProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, type: str = "celsius", **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)
        self.type = (type or "celsius").lower()

    def generate_non_blank(self, row_data=None):
        if self.type == "fahrenheit":
            temp = round(random.uniform(-4.0, 113.0), 1)
            sign = "°F"
        else:
            # default to celsius for any unknown or misspelled types
            temp = round(random.uniform(-20.0, 45.0), 1)
            sign = "°C"

        return f"{temp}{sign}"
