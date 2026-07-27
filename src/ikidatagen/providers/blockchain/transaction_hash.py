from ..base_provider import BaseProvider
import string


class TransactionHashProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, length: int = 64, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)
        self.length = length

    def generate_non_blank(self, row_data=None):
        chars = string.hexdigits.lower()
        body = ''.join(self.get_random_data_by_list(chars)
                       for _ in range(self.length))
        return "0x" + body
