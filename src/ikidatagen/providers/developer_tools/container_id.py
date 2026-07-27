from ..base_provider import BaseProvider
import string


class ContainerIdProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self, row_data=None):
        owner_code = ''.join(self.get_random_choices_by_list(string.ascii_lowercase, k=4))
        category = 'U'
        serial = ''.join(self.get_random_choices_by_list(string.digits, k=6))
        check_digit = str(self.generate_integer(0, 9))
        return f"{owner_code}{category}{serial}{check_digit}"
