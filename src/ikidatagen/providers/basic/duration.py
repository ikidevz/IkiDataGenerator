from ..base_provider import BaseProvider


class DurationProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None):
        start_index = self.generate_integer(
            0, len(self.basic['duration_units']) - self.generate_integer(1, 3))
        chosen_units = list(reversed(self.basic['duration_units'][start_index:start_index +
                                                                  self.generate_integer(1, 3)]))
        duration_parts = []
        for unit in chosen_units:
            if unit == "seconds":
                value = self.generate_integer(10, 59)
            elif unit == "minutes":
                value = self.generate_integer(1, 59)
            elif unit == "hours":
                value = self.generate_integer(1, 23)
            elif unit == "days":
                value = self.generate_integer(1, 30)
            elif unit == "weeks":
                value = self.generate_integer(1, 4)
            elif unit == "months":
                value = self.generate_integer(1, 12)
            elif unit == "years":
                value = self.generate_integer(1, 10)
            else:
                value = self.generate_integer(1, 100)

            duration_parts.append(f"{value} {unit}")

        return " ".join(duration_parts)
