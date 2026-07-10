from ..base_provider import BaseProvider


class InsurancePolicyIdProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None):
        prefix = self.get_random_data_by_list(["POL", "INS", "HMO", "LIFE", "AUTO",
                               "HOME", "TRVL", "HLTH", "DIS", "LIAB", "DENT", "VET"])
        number = self.generate_integer(100000, 999999)
        return f"{prefix}-{number}"
