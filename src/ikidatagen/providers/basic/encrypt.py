from ..base_provider import BaseProvider


class EncryptProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None) -> str:
        return ''.join(self.get_random_data_by_list('0123456789abcdef') for _ in range(64))
