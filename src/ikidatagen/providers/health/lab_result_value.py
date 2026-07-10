from ..base_provider import BaseProvider


class LabResultValueProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None):
        if self.get_random_object() < 0.4:
            return str(self.generate_integer(1, 300))
        else:
            return f"{round(self.generate_float(1.0, 300.0), 1)}"
