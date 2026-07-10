from ..base_provider import BaseProvider
import string


class ApiKeyProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, prefix: str = None, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)
        self.prefix = prefix

    def generate_non_blank(self, row_data=None):
        chosen_prefix = self.prefix or self.get_random_data_by_list(self.it['prefix'])
        chars = string.ascii_letters + string.digits
        key_body = ''.join(self.get_random_data_by_list(chars) for _ in range(48))
        return f"{chosen_prefix}{key_body}"
