from ..base_provider import BaseProvider


class BankRoutingNumberProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None) -> str:
        digits = [self.generate_integer(0, 9) for _ in range(8)]
        checksum = sum(digits) % 10  # simplified checksum
        digits.append(checksum)
        return ''.join(str(d) for d in digits)
