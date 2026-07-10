from ..base_provider import BaseProvider


class AccountNumberProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None):
        return "".join(str(self.generate_integer(0, 9)) for _ in range(12))
