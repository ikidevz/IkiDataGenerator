import string
from ..base_provider import BaseProvider


class BankLeiProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)
        self.prefixes = [
            "5493", "2138", "5299", "8156", "8888", "3001", "1000", "9900"
        ]

    def _random_alphanumeric(self, length: int) -> str:
        chars = string.ascii_uppercase + string.digits
        return ''.join(self.get_random_choices_by_list(chars, k=length))

    def generate_non_blank(self, row_data=None) -> str:
        prefix = self.get_random_data_by_list(self.prefixes)
        middle = self._random_alphanumeric(14)
        suffix = ''.join(self.get_random_choices_by_list(string.digits, k=2))
        return prefix + middle + suffix
