from ..base_provider import BaseProvider


class MedicalDeviceIdProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None):
        prefixes = ["MD", "EQ", "ME", "DEV", "ICU", "SURG", "LAB"]
        prefix = self.get_random_data_by_list(prefixes)
        number = self.generate_integer(10000, 99999)
        return f"{prefix}-{number}"
