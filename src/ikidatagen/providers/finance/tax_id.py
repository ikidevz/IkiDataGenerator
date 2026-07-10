from ..base_provider import BaseProvider


class TaxIdProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, type: str = "SSN", **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)
        self.type = type

    def generate_non_blank(self, row_data=None):
        if self.type == "EIN":
            # Format: XX-XXXXXXX
            return f"{self.generate_integer(10, 99)}-{self.generate_integer(1000000, 9999999)}"

        # Default: SSN format XXX-XX-XXXX
        return f"{self.generate_integer(100, 999)}-{self.generate_integer(10, 99)}-{self.generate_integer(1000, 9999)}"
